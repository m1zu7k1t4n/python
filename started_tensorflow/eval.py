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


def eval(graph_file):
  # 現在のグラフをリセット
  tf.reset_default_graph()

  with tf.gfile.FastGFile(graph_file, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

  labels = tf.placeholder(tf.int32, shape=[1], name='label')
  logits = tf.get_default_graph().get_tensor_by_name('output/logits:0')

  top_k_op = tf.nn.in_top_k(logits, labels, 1)

  with tf.Session() as sess:
    image_reader = Cifar10Reader(FLAGS.test_data)

    true_count = 0
    for index in range(10000):
      image = image_reader.read(index)

      predictions = sess.run(top_k_op,
                             feed_dict={
                               'input_image:0': image.byte_array,
                               labels: image.label,
                             })
      true_count += np.sum(predictions)

    print('%s, %.3f' % (graph_file, (true_count / 10000.0)))

    image_reader.close()


if __name__ == '__main__':
  file_list = glob.glob(FLAGS.graph_dir + '/*.pb')
  for file in file_list:
    eval(file)
