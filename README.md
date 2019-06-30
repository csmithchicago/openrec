# Very Much a Work in Progress

# Recommender Systems

An open-source python library used for making recommendation systems.

This project initally started as a pytorch port of the [**OpenRec**](http://www.openrec.ai/) library, an open-source and modular library for neural network-inspired recommendation algorithms. 


Each recommender is modeled as a computational graph that consists of a structured ensemble of reusable modules connected through a set of well-defined interfaces. OpenRec is built to ease the process of extending and adapting state-of-the-art neural recommenders to heterogeneous recommendation scenarios, where different users', items', and contextual data sources need to be incorporated.

## Installation

First, clone OpenRec using `git`:

```sh
git clone https://github.com/csmithchicago/OpenRecTorch
```

Then, `cd` to the OpenRec folder and run the install command:

```sh
cd openrec
python setup.py install
```

## Dataset download

Use `download_dataset.sh` script.

## Get started

* [OpenRec website](http://www.openrec.ai/)


## License

[MIT](LICENSE)




