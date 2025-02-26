from openrec.legacy.recommenders import PMF
from openrec.legacy.modules.extractions import MultiLayerFC
from openrec.legacy.modules.fusions import Average


class UserPMF(PMF):
    def __init__(
        self,
        batch_size,
        max_user,
        max_item,
        dim_embed,
        dims,
        user_f_source,
        test_batch_size=None,
        item_serving_size=None,
        dropout_rate=None,
        l2_reg=None,
        l2_reg_mlp=None,
        opt="SGD",
        sess_config=None,
    ):

        self._dims = dims
        self._dropout_rate = dropout_rate
        self._user_f_source = user_f_source
        self._item_serving_size = item_serving_size

        self._l2_reg_mlp = l2_reg_mlp

        super(UserPMF, self).__init__(
            batch_size=batch_size,
            max_user=max_user,
            max_item=max_item,
            dim_embed=dim_embed,
            l2_reg=l2_reg,
            test_batch_size=test_batch_size,
            opt=opt,
            sess_config=sess_config,
        )

    def _build_user_inputs(self, train=True):

        super(UserPMF, self)._build_user_inputs(train)
        if train:
            self._add_input(
                name="user_feature",
                dtype="float32",
                shape=[self._batch_size, self._user_f_source.shape[1]],
            )
        else:
            self._add_input(
                name="user_feature",
                dtype="float32",
                shape=[None, self._user_f_source.shape[1]],
                train=False,
            )

    def _input_mappings(self, batch_data, train):

        default_input_map = super(UserPMF, self)._input_mappings(
            batch_data=batch_data, train=train
        )
        default_input_map[
            self._get_input("user_feature", train=train)
        ] = self._user_f_source[batch_data["user_id_input"]]

        return default_input_map

    def _build_user_extractions(self, train=True):

        super(UserPMF, self)._build_user_extractions(train)

        self._add_module(
            "user_f",
            MultiLayerFC(
                in_tensor=self._get_input("user_feature", train=train),
                train=train,
                dims=self._dims,
                l2_reg=self._l2_reg_mlp,
                dropout_mid=self._dropout_rate,
                scope="user_MLP",
                reuse=not train,
            ),
            train=train,
        )

    def _build_default_fusions(self, train=True):

        self._add_module(
            "user_vec",
            Average(
                scope="user_average",
                reuse=not train,
                module_list=[
                    self._get_module("user_vec", train=train),
                    self._get_module("user_f", train=train),
                ],
                weight=2.0,
            ),
            train=train,
        )
