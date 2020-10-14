import dask.dataframe as dd
import numpy as np
import tensorflow as tf

from src.logger import get_logger

logger = get_logger(__name__)


def dd_tfrecord(df, tfrecord_path):
    feature_func = {
        np.int64: lambda value: tf.train.Feature(int64_list=tf.train.Int64List(value=[value])),
        np.float64: lambda value: tf.train.Feature(float_list=tf.train.FloatList(value=[value])),
        np.object_: lambda value: tf.train.Feature(bytes_list=tf.train.BytesList(value=[tf.compat.as_bytes(value)]))
    }

    # convert types to tf base types
    df = df.copy()
    for col in df.columns:
        # convert non numeric types to string
        if df[col].dtype.type not in {np.int64, np.float64}:
            df[col] = df[col].astype(str)
    logger.debug("data column types: %s.", list(df.dtypes.items()))

    # configure feature specification base on column type
    col_func = {col_name: feature_func[col_type.type]
                for col_name, col_type in df.head().dtypes.items()}

    # save tfrecord
    with tf.python_io.TFRecordWriter(tfrecord_path) as writer:
        for row in df.itertuples():
            example = tf.train.Example(
                features=tf.train.Features(
                    feature={
                        name: func(getattr(row, name))
                        for name, func in col_func.items()
                    }))
            writer.write(example.SerializeToString())
    logger.info("tfrecord saved: %s.", tfrecord_path)


def tf_csv_dataset(csv_path, label_col, col_defaults, shuffle=False, batch_size=32):
    df = dd.read_csv(csv_path)
    # use col_defaults if specified for col, else use defaults base on col type
    type_defaults = {np.int64: 0, np.float64: 0.0, np.object_: ""}
    record_defaults = [[col_defaults.get(col_name, type_defaults.get(col_type.type, ""))]
                       for col_name, col_type in df.dtypes.items()]

    def parse_csv(value):
        columns = tf.decode_csv(value, record_defaults)
        features = dict(zip(df.columns.tolist(), columns))
        label = features[label_col]
        return features, label

    # read, parse, shuffle and batch dataset
    dataset = tf.data.TextLineDataset(csv_path).skip(1)  # skip header
    if shuffle:
        dataset = dataset.shuffle(buffer_size=1024)
    dataset = dataset.map(parse_csv, num_parallel_calls=8)
    dataset = dataset.batch(batch_size)
    return dataset


def dd_create_categorical_column(df, col, default_value=-1, num_oov_buckets=1):
    return tf.feature_column.categorical_column_with_vocabulary_list(
        col,
        df[col].unique().compute().sort_values().tolist(),
        default_value=default_value,
        num_oov_buckets=num_oov_buckets
    )
