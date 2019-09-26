#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OIsolationForestEstimator(H2OEstimator):
    """
    Isolation Forest

    Builds an Isolation Forest model. Isolation Forest algorithm samples the training frame
    and in each iteration builds a tree that partitions the space of the sample observations until
    it isolates each observation. Length of the path from root to a leaf node of the resulting tree
    is used to calculate the anomaly score. Anomalies are easier to isolate and their average
    tree path is expected to be shorter than paths of regular observations.
    """

    algo = "isolationforest"
    param_names = {"model_id", "training_frame", "score_each_iteration", "score_tree_interval", "ignored_columns",
                   "ignore_const_cols", "ntrees", "max_depth", "min_rows", "max_runtime_secs", "seed",
                   "build_tree_one_node", "mtries", "sample_size", "sample_rate", "col_sample_rate_change_per_level",
                   "col_sample_rate_per_tree", "categorical_encoding", "stopping_rounds", "stopping_metric",
                   "stopping_tolerance", "export_checkpoints_dir"}

    def __init__(self, **kwargs):
        super(H2OIsolationForestEstimator, self).__init__()
        self._parms = {}
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in self.param_names:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars_if = H2OIsolationForestEstimator(seed = 1234)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars_if = H2OIsolationForestEstimator(score_each_iteration = True,
        ...                                       ntrees = 55,
        ...                                       seed = 1234)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def score_tree_interval(self):
        """
        Score the model after every so many trees. Disabled if set to 0.

        Type: ``int``  (default: ``0``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars_if = H2OIsolationForestEstimator(score_tree_interval = 5,
        ...                                       seed = 1234)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("score_tree_interval")

    @score_tree_interval.setter
    def score_tree_interval(self, score_tree_interval):
        assert_is_type(score_tree_interval, None, int)
        self._parms["score_tree_interval"] = score_tree_interval


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = airlines.columns[:9]
        >>> col_list = ['DepTime','CRSDepTime','ArrTime','CRSArrTime']
        >>> airlines_if = H2OIsolationForestEstimator(ignored_columns = col_list,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars["const_1"] = 6
        >>> cars["const_2"] = 7
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_if = H2OIsolationForestEstimator(seed = 1234,
        ...                                       ignore_const_cols = True)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def ntrees(self):
        """
        Number of trees.

        Type: ``int``  (default: ``50``).

        :examples:

        >>> titanic = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
        >>> predictors = titanic.columns
        >>> tree_num = [20, 50, 80, 110, 140, 170, 200]
        >>> label = ["20", "50", "80", "110", "140", "170", "200"]
        >>> for key, num in enumerate(tree_num):
        ...     titanic_if = H2OIsolationForestEstimator(ntrees = num,
        ...                                              seed = 1234)
        ...     titanic_if.train(x = predictors,
        ...                      training_frame = titanic) 
        ...     print(label[key], 'training score', titanic_if.mse(train = True))
        """
        return self._parms.get("ntrees")

    @ntrees.setter
    def ntrees(self, ntrees):
        assert_is_type(ntrees, None, int)
        self._parms["ntrees"] = ntrees


    @property
    def max_depth(self):
        """
        Maximum tree depth.

        Type: ``int``  (default: ``8``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars_if = H2OIsolationForestEstimator(max_depth = 2,
        ...                                       seed = 1234)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("max_depth")

    @max_depth.setter
    def max_depth(self, max_depth):
        assert_is_type(max_depth, None, int)
        self._parms["max_depth"] = max_depth


    @property
    def min_rows(self):
        """
        Fewest allowed (weighted) observations in a leaf.

        Type: ``float``  (default: ``1``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars_if = H2OIsolationForestEstimator(min_rows = 16,
        ...                                       seed = 1234)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("min_rows")

    @min_rows.setter
    def min_rows(self, min_rows):
        assert_is_type(min_rows, None, numeric)
        self._parms["min_rows"] = min_rows


    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``  (default: ``0``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars_if = H2OIsolationForestEstimator(max_runtime_secs = 10,
        ...                                       ntrees = 10000,
        ...                                       max_depth = 10,
        ...                                       seed = 1234)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def seed(self):
        """
        Seed for pseudo random number generator (if applicable)

        Type: ``int``  (default: ``-1``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> isofor_w_seed = H2OIsolationForestEstimator(seed = 1234) 
        >>> isofor_w_seed.train(x = predictors,
        ...                     training_frame = airlines)
        >>> isofor_wo_seed = H2OIsolationForestEstimator()
        >>> isofor_wo_seed.train(x = predictors,
        ...                      training_frame = airlines)
        >>> isofor_w_seed.model_performance()
        >>> isofor_wo_seed.model_performance()
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def build_tree_one_node(self):
        """
        Run on one node only; no network overhead but fewer cpus used.  Suitable for small datasets.

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars_if = H2OIsolationForestEstimator(build_tree_one_node = True,
        ...                                       seed = 1234)
        >>> cars_if.train(x = predictors,
        ...               training_frame = cars)
        >>> cars_if.model_performance()
        """
        return self._parms.get("build_tree_one_node")

    @build_tree_one_node.setter
    def build_tree_one_node(self, build_tree_one_node):
        assert_is_type(build_tree_one_node, None, bool)
        self._parms["build_tree_one_node"] = build_tree_one_node


    @property
    def mtries(self):
        """
        Number of variables randomly sampled as candidates at each split. If set to -1, defaults (number of
        predictors)/3.

        Type: ``int``  (default: ``-1``).

        :examples:

        >>> covtype = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/covtype/covtype.20k.data")
        >>> predictors = covtype.columns[0:54]
        >>> cov_if = H2OIsolationForestEstimator(mtries = 30, seed = 1234)
        >>> cov_if.train(x = predictors,
        ...              training_frame = covtype)
        >>> cov_if.model_performance()
        """
        return self._parms.get("mtries")

    @mtries.setter
    def mtries(self, mtries):
        assert_is_type(mtries, None, int)
        self._parms["mtries"] = mtries


    @property
    def sample_size(self):
        """
        Number of randomly sampled observations used to train each Isolation Forest tree. Only one of parameters
        sample_size and sample_rate should be defined. If sample_rate is defined, sample_size will be ignored.

        Type: ``int``  (default: ``256``).

        :examples:

        >>> train = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/anomaly/ecg_discord_train.csv")
        >>> test = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/anomaly/ecg_discord_test.csv")
        >>> isofor_model = H2OIsolationForestEstimator(sample_size = 5,
        ...                                            ntrees=7)
        >>> isofor_model.train(training_frame = train)
        >>> isofor_model.model_performance()
        >>> isofor_model.model_performance(test)
        """
        return self._parms.get("sample_size")

    @sample_size.setter
    def sample_size(self, sample_size):
        assert_is_type(sample_size, None, int)
        self._parms["sample_size"] = sample_size


    @property
    def sample_rate(self):
        """
        Rate of randomly sampled observations used to train each Isolation Forest tree. Needs to be in range from 0.0 to
        1.0. If set to -1, sample_rate is disabled and sample_size will be used instead.

        Type: ``float``  (default: ``-1``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> airlines_if = H2OIsolationForestEstimator(sample_rate = .7,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("sample_rate")

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        assert_is_type(sample_rate, None, numeric)
        self._parms["sample_rate"] = sample_rate


    @property
    def col_sample_rate_change_per_level(self):
        """
        Relative change of the column sampling rate for every level (must be > 0.0 and <= 2.0)

        Type: ``float``  (default: ``1``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> airlines_if = H2OIsolationForestEstimator(col_sample_rate_change_per_level = .9,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("col_sample_rate_change_per_level")

    @col_sample_rate_change_per_level.setter
    def col_sample_rate_change_per_level(self, col_sample_rate_change_per_level):
        assert_is_type(col_sample_rate_change_per_level, None, numeric)
        self._parms["col_sample_rate_change_per_level"] = col_sample_rate_change_per_level


    @property
    def col_sample_rate_per_tree(self):
        """
        Column sample rate per tree (from 0.0 to 1.0)

        Type: ``float``  (default: ``1``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> airlines_if = H2OIsolationForestEstimator(col_sample_rate_per_tree = .7,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("col_sample_rate_per_tree")

    @col_sample_rate_per_tree.setter
    def col_sample_rate_per_tree(self, col_sample_rate_per_tree):
        assert_is_type(col_sample_rate_per_tree, None, numeric)
        self._parms["col_sample_rate_per_tree"] = col_sample_rate_per_tree


    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        One of: ``"auto"``, ``"enum"``, ``"one_hot_internal"``, ``"one_hot_explicit"``, ``"binary"``, ``"eigen"``,
        ``"label_encoder"``, ``"sort_by_response"``, ``"enum_limited"``  (default: ``"auto"``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> encoding = "one_hot_explicit"
        >>> airlines_if = H2OIsolationForestEstimator(categorical_encoding = encoding,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding


    @property
    def stopping_rounds(self):
        """
        Early stopping based on convergence of stopping_metric. Stop if simple moving average of length k of the
        stopping_metric does not improve for k:=stopping_rounds scoring events (0 to disable)

        Type: ``int``  (default: ``0``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> airlines_if = H2OIsolationForestEstimator(stopping_metric = "auto",
        ...                                           stopping_rounds = 3,
        ...                                           stopping_tolerance = 1e-2,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("stopping_rounds")

    @stopping_rounds.setter
    def stopping_rounds(self, stopping_rounds):
        assert_is_type(stopping_rounds, None, int)
        self._parms["stopping_rounds"] = stopping_rounds


    @property
    def stopping_metric(self):
        """
        Metric to use for early stopping (AUTO: logloss for classification, deviance for regression and anonomaly_score
        for Isolation Forest). Note that custom and custom_increasing can only be used in GBM and DRF with the Python
        client.

        One of: ``"auto"``, ``"anomaly_score"``  (default: ``"auto"``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> airlines_if = H2OIsolationForestEstimator(stopping_metric = "auto",
        ...                                           stopping_rounds = 3,
        ...                                           stopping_tolerance = 1e-2,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("stopping_metric")

    @stopping_metric.setter
    def stopping_metric(self, stopping_metric):
        assert_is_type(stopping_metric, None, Enum("auto", "anomaly_score"))
        self._parms["stopping_metric"] = stopping_metric


    @property
    def stopping_tolerance(self):
        """
        Relative tolerance for metric-based stopping criterion (stop if relative improvement is not at least this much)

        Type: ``float``  (default: ``0.01``).

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> airlines_if = H2OIsolationForestEstimator(stopping_metric = "auto",
        ...                                           stopping_rounds = 3,
        ...                                           stopping_tolerance = 1e-2,
        ...                                           seed = 1234)
        >>> airlines_if.train(x = predictors,
        ...                   training_frame = airlines)
        >>> airlines_if.model_performance()
        """
        return self._parms.get("stopping_tolerance")

    @stopping_tolerance.setter
    def stopping_tolerance(self, stopping_tolerance):
        assert_is_type(stopping_tolerance, None, numeric)
        self._parms["stopping_tolerance"] = stopping_tolerance


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.

        :examples:

        >>> import tempfile
        >>> from os import listdir
        >>> airlines = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip", destination_frame="air.hex")
        >>> predictors = ["DayofMonth", "DayOfWeek"]
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> air_if = H2OIsolationForestEstimator(max_depth = 3,
        ...                                      seed = 1234,
        ...                                      export_checkpoints_dir = checkpoints_dir)
        >>> air_if.train(x = predictors,
        ...              training_frame = airlines)
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir


