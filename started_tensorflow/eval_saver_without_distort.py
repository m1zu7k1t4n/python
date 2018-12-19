# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import numpy as np
import tensorflow as tf

# 指定したディレクトリ下にあるグラフ＋変数のファイルをテストデータで順次評価する
from reader_minibatch import Cifar10Reader

import model_normalized_dropout_minibatch as model

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('checkpoint_dir', None, "チェックポイントのディレクトリ")
tf.app.flags.DEFINE_string('test_data', './data/test_batch.bin',
                           "テストデータのパス")
tf.app.flags.DEFINE_integer('batch_size', 64, "バッチサイズ")


def _loss(logits, label):
  print(logits.get_shape())
  print(label.get_shape())

  labels = tf.cast(label, tf.int64)
  cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
    logits, labels, name='cross_entropy_per_example')
  cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
  return cross_entropy_mean


def _restore(sess, saver):
  ckpt = tf.train.get_checkpoint_state(FLAGS.checkpoint_dir)
  if ckpt and ckpt.model_checkpoint_path:
    saver.restore(sess, ckpt.model_checkpoint_path)
    return ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]

  return None


def main(argv=None):
  reader = Cifar10Reader([FLAGS.test_data])
  record = reader.read()

  whiten_image = tf.image.per_image_whitening(record.byte_array)

  batch_image, batch_label = tf.train.batch(
    [whiten_image, record.label],
    FLAGS.batch_size)
  batch_label = tf.reshape(batch_label, [FLAGS.batch_size], 'batch_label')

  logits = model.inference(batch_image, 1.0, batch_size=FLAGS.batch_size)

  top_k_op = tf.nn.in_top_k(logits, batch_label, 1)

  saver = tf.train.Saver()

  coord = tf.train.Coordinator()

  with tf.Session() as sess:
    global_step = _restore(sess, saver)
    assert global_step, 'checkpoint is not found.'

    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    true_count = 0

    num_iter = math.ceil(10000 / FLAGS.batch_size)
    step_of_epoch = num_iter * FLAGS.batch_size

    try:
      # バッチごとに評価
      for step in range(num_iter):
        predictions = sess.run(top_k_op)

        true_count += np.sum(predictions)

    except Exception as e:
      coord.request_stop(e)

    coord.request_stop()
    coord.join(threads, stop_grace_period_secs=10)

    print('Epoch %s, %.3f' % (global_step, (true_count / step_of_epoch)))


if __name__ == '__main__':
  tf.app.run()
