package hex.schemas;

import hex.tree.isofor.IsolationForest;
import hex.tree.isofor.IsolationForestModel;
import water.api.API;

public class IsolationForestV3 extends SharedTreeV3<IsolationForest, IsolationForestV3, IsolationForestV3.IsolationForestParametersV3> {

    public static final class IsolationForestParametersV3 extends SharedTreeV3.SharedTreeParametersV3<IsolationForestModel.IsolationForestParameters, IsolationForestParametersV3> {
        static public String[] fields = new String[]{
                "model_id",
                "training_frame",
                "score_each_iteration",
                "score_tree_interval",
                "ignored_columns",
                "ignore_const_cols",
                "ntrees",
                "max_depth",
                "min_rows",
                "max_runtime_secs",
                "seed",
                "build_tree_one_node",
                "mtries",
                "sample_size",
                "sample_rate",
                "col_sample_rate_change_per_level",
                "col_sample_rate_per_tree",
                "categorical_encoding",
                "stopping_rounds",
                "stopping_metric",
                "stopping_tolerance",
                "export_checkpoints_dir",
                "contamination",
                "response_column"
        };

        // Input fields
        @API(help = "Number of randomly sampled observations used to train each Isolation Forest tree. Only one of parameters sample_size and sample_rate should be defined. If sample_rate is defined, sample_size will be ignored.", gridable = true)
        public long sample_size;

        @API(help = "Rate of randomly sampled observations used to train each Isolation Forest tree. Needs to be in range from 0.0 to 1.0. If set to -1, sample_rate is disabled and sample_size will be used instead.", gridable = true)
        public double sample_rate;

        @API(help = "Number of variables randomly sampled as candidates at each split. If set to -1, defaults (number of predictors)/3.", gridable = true)
        public int mtries;

        @API(help = "Contamination ratio - the proportion of anomalies in the input dataset. If undefined (-1) the predict function will not mark observations as anomalies and only anomaly score will be returned. Defaults to -1 (undefined).")
        public double contamination;

    }
}
