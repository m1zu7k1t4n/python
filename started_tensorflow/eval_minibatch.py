# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob

import tensorflow as tf

from reader import Cifar10Reader

import numpy as np

# 指定したディレクトリ下にあるグラフ＋変数のファイルをテストデータで順次評価する

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('graph_dir', None, "処理するグラフファイルのあるパス")
tf.app.flags.DEFINE_string('test_data', './data/test_batch.bin',
                           "テストデータのパス")
tf.app.flags.DEFINE_integer('batch_size', 64, "バッチサイズ")


def eval(graph_file):
  # 現在のグラフをリセット
  tf.reset_default_graph()

  with tf.gfile.FastGFile(graph_file, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

  labels = tf.placeholder(tf.int32, shape=[FLAGS.batch_size], name='label')
  logits = tf.get_default_graph().get_tensor_by_name('output/logits:0')

  top_k_op = tf.nn.in_top_k(logits, labels, 1)

  with tf.Session() as sess:
    image_reader = Cifar10Reader(FLAGS.test_data)

    batch_byte_array = []
    batch_label = []

    true_count = 0

    # バッチごとに評価
    for index in range(10000):
      image = image_reader.read(index)

      batch_byte_array.append(image.byte_array)
      batch_label.append(image.label[0])

      if len(batch_byte_array) < FLAGS.batch_size:
        continue

      predictions = sess.run(top_k_op,
                             feed_dict={
                               'input_image:0': batch_byte_array,
                               labels: batch_label,
                             })

      true_count += np.sum(predictions)

      batch_byte_array.clear()
      batch_label.clear()

    # バッチサイズで割りきれないテストデータで評価
    for index in range(len(batch_byte_array)):
      byte_array = [batch_byte_array[index]] * FLAGS.batch_size
      label = [batch_label[index]] * FLAGS.batch_size
      predictions = sess.run(top_k_op,
                             feed_dict={
                               'input_image:0': byte_array,
                               labels: label,
                             })

      true_count += (np.sum(predictions) / FLAGS.batch_size)

    batch_byte_array.clear()
    batch_label.clear()

    print('%s, %.3f' % (graph_file, (true_count / 10000.0)))

    image_reader.close()


if __name__ == '__main__':
  file_list = glob.glob(FLAGS.graph_dir + '/*.pb')
  for file in file_list:
    eval(file)
