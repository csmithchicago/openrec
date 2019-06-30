# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.0.0] - 2018-08-31

Introducing new modular interfaces for OpenRec.

### Major changes:

- A new paradigm for defining, extending, and building recommenders.
  - Remove boilerplate class structure of recommenders.
  - Introduce a macro-based recommender construction paradigm.
  - Disentangle module construction and connection.
  - Support module construction directly using Tensorflow and Keras APIs.
  
- A more efficient and customizable pipeline for recommender training and evaluation.
  - A new Dataset class for complex data input.
  - A customizable ModelTrainer handling complex training/evaluation scenarios.
  - Caching mechanism to speed up evaluation of complex recommenders.
  
- Provide model training and evaluation examples for new interfaces.

## [0.1.0b] - 2017-11-29  

- Initial Release:

  * [OpenRec legacy tutorials](https://github.com/csmithchicago/openrec/tree/master/legacy_tutorials)
  * [OpenRec legacy examples](https://github.com/csmithchicago/openrec/tree/master/legacy_examples)