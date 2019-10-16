""" Example utils """

import tensorflow as tf

class UndefinedModelFnError(Exception):
  """
  UndefinedModelFnError

  Occurs if a data owner or model owner hasn't defined
  a model function
  """

def split_dataset(data_root, num_data_owners, rows):
  """
  Helper function to help split the dataset evenly between
  data owners. USE FOR SIMULATION ONLY.
  """

  print("WARNING: Splitting dataset for {} data owners. "
        "This is for simulation use only".format(num_data_owners))

  all_dataset = tf.data.TFRecordDataset([data_root + "/train.tfrecord"])

  split = rows // num_data_owners
  index = 0
  for i in range(num_data_owners):
    dataset = all_dataset.skip(index)
    dataset = all_dataset.take(split)

    filename = '{}/train{}.tfrecord'.format(data_root, i)
    writer = tf.data.experimental.TFRecordWriter(filename)
    writer.write(dataset)
