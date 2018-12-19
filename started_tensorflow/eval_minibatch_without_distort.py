# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob

import math
import numpy as np
import tensorflow as tf

# 指定したディレクトリ下にあるグラフ＋変数のファイルをテストデータで順次評価する
from reader_minibatch import Cifar10Reader

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('graph_dir', None, "処理するグラフファイルのあるパス")
tf.app.flags.DEFINE_string('test_data', './data/test_batch.bin',
                           "テストデータのパス")
tf.app.flags.DEFINE_integer('batch_size', 64, "バッチサイズ")


def eval(graph_file):
  # 現在のグラフをリセット
  tf.reset_default_graph()

  reader = Cifar10Reader([FLAGS.test_data])
  record = reader.read()

  whiten_image = tf.image.per_image_whitening(record.byte_array)

  batch_image, batch_label = tf.train.batch(
    [whiten_image, record.label],
    FLAGS.batch_size)
  batch_label = tf.reshape(batch_label, [FLAGS.batch_size], 'batch_label')

  with tf.gfile.FastGFile(graph_file, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

  input_image = tf.get_default_graph().get_tensor_by_name('input_image:0')
  label_placeholder = tf.placeholder(dtype=tf.int32, shape=[FLAGS.batch_size])

  logits = tf.get_default_graph().get_tensor_by_name('output/logits:0')
  top_k_op = tf.nn.in_top_k(logits, label_placeholder, 1)

  coord = tf.train.Coordinator()

  with tf.Session() as sess:
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    true_count = 0

    num_iter = math.ceil(10000 / FLAGS.batch_size)
    step_of_epoch = num_iter * FLAGS.batch_size

    try:
      # バッチごとに評価
      for step in range(num_iter):
        whitten_image, labels = sess.run([batch_image, batch_label])
        predictions = sess.run(top_k_op,
                               feed_dict={
                                 input_image: whitten_image,
                                 label_placeholder: labels
                               })

        true_count += np.sum(predictions)

    except Exception as e:
      coord.request_stop(e)

    coord.request_stop()
    coord.join(threads, stop_grace_period_secs=10)

    print('%s, %.3f' % (graph_file, (true_count / step_of_epoch)))


if __name__ == '__main__':
  file_list = glob.glob(FLAGS.graph_dir + '/*.pb')
  for file in file_list:
    print(file)
    eval(file)
