# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import math

import numpy as np
import tensorflow as tf

# import model_vgg_lite_minibatch as model
import model_normalized_dropout_minibatch as model

# TensorFlow 0.10よりパッケージ変更
# from tensorflow.python.client import graph_util
from tensorflow.python.framework import graph_util

from tensorflow.python.platform import gfile

# 軽量化版のVGGモデルで学習する
# ミニバッチに対応
from reader_minibatch import Cifar10Reader

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer('epoch', 100, "訓練するEpoch数")
tf.app.flags.DEFINE_float('learning_rate', 0.001, "学習率")
tf.app.flags.DEFINE_string('data_dir', './data/', "訓練データのディレクトリ")
tf.app.flags.DEFINE_string('checkpoint_dir', './checkpoints/',
                           "チェックポイントを保存するディレクトリ")
tf.app.flags.DEFINE_string('test_data', None, "テストデータのパス")
tf.app.flags.DEFINE_string('graph_dir', './graphs/',
                           "グラフを保存するディレクトリ")
tf.app.flags.DEFINE_integer('batch_size', 64, "ミニバッチサイズ")


def _loss(logits, label):
  print(logits.get_shape())
  print(label.get_shape())

  labels = tf.cast(label, tf.int64)
  cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
    logits, labels, name='cross_entropy_per_example')
  cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
  return cross_entropy_mean


def _train(total_loss, global_step):
  opt = tf.train.AdamOptimizer(learning_rate=FLAGS.learning_rate)
  grads = opt.compute_gradients(total_loss)
  train_op = opt.apply_gradients(grads, global_step=global_step)

  return train_op


filenames = [
  os.path.join(FLAGS.data_dir, 'data_batch_%d.bin' % i) for i in range(1, 6)
  ]


def main(argv=None):
  global_step = tf.Variable(0, trainable=False)

  keepprob_placeholder = tf.placeholder_with_default(tf.constant(1.0),
                                                     shape=[],
                                                     name='keep_prob')

  reader = Cifar10Reader(filenames)
  record = reader.read()

  distorted_image = _distort(record.byte_array)
  whiten_image = tf.image.per_image_whitening(distorted_image)

  batch_image, batch_label = tf.train.batch(
    [whiten_image, record.label],
    FLAGS.batch_size)
  tf.image_summary('images', batch_image)

  batch_label = tf.reshape(batch_label, [FLAGS.batch_size], 'batch_label')

  # eval用のエントリポイント
  input_image = tf.placeholder_with_default(
    batch_image,
    [FLAGS.batch_size, 32, 32, 3], name="input_image")

  logits = model.inference(input_image,
                           keepprob_placeholder, batch_size=FLAGS.batch_size)
  total_loss = _loss(logits, batch_label)
  train_op = _train(total_loss, global_step)

  saver = tf.train.Saver(tf.all_variables())
  summary_op = tf.merge_all_summaries()

  with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())

    total_duration = 0

    # _restore(saver, sess)
    _export_graph(sess, 0)

    summary_writer = tf.train.SummaryWriter(FLAGS.checkpoint_dir, sess.graph)
    tf.train.start_queue_runners(sess=sess)

    epoch_step = math.ceil(10000 * 5 / FLAGS.batch_size)
    for step in range(epoch_step * (FLAGS.epoch + 1)):
      _, loss_value = sess.run([train_op, total_loss],
                               feed_dict={
                                 keepprob_placeholder: 0.5
                               })

      assert not np.isnan(loss_value), \
        'Model diverged with loss = NaN'

      if step % 10 == 0:
        print('loss_value : %.3f' % loss_value)

      if step % 100 == 0:
        summary_str = sess.run(summary_op)
        summary_writer.add_summary(summary_str, step)

      if step % epoch_step == 0:
        epoch = int(step / epoch_step)
        saver.save(sess, FLAGS.checkpoint_dir, global_step=epoch)
        _export_graph(sess, epoch)

    print('Total duration = %d sec' % total_duration)


def _distort(image_placeholder):
  padded_image = tf.pad(image_placeholder, ((4, 4), (4, 4), (0, 0)))
  croped_image = tf.random_crop(padded_image, [32, 32, 3])
  flipped_image = tf.image.random_flip_left_right(croped_image)
  distorted_image = tf.image.random_brightness(flipped_image, max_delta=63)
  distorted_image = tf.image.random_contrast(distorted_image, lower=0.2,
                                             upper=1.8)
  return distorted_image


def _restore(saver, sess):
  checkpoint = tf.train.get_checkpoint_state(FLAGS.checkpoint_dir)
  if checkpoint and checkpoint.model_checkpoint_path:
    saver.restore(sess, checkpoint.model_checkpoint_path)


def _export_graph(sess, epoch):
  constant_graph_def = graph_util.convert_variables_to_constants(
    sess, sess.graph_def, ["output/logits"])

  file_path = os.path.join(FLAGS.graph_dir, 'graph_%02d_epoch.pb' % epoch)
  with gfile.FastGFile(file_path, 'wb') as f:
    f.write(constant_graph_def.SerializeToString())


if __name__ == '__main__':
  tf.app.run()
