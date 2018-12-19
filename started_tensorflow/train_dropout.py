# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time

import numpy as np
import tensorflow as tf

import model_normalized_dropout as model
from reader import Cifar10Reader

# TensorFlow 0.10よりパッケージ変更
# from tensorflow.python.client import graph_util
from tensorflow.python.framework import graph_util

from tensorflow.python.platform import gfile

# モデルにドロップアウトを設定。モデルはmodel_normalized_dropout.py参照

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer('epoch', 30, "訓練するEpoch数")
tf.app.flags.DEFINE_float('learning_rate', 0.0005, "学習率")
tf.app.flags.DEFINE_string('data_dir', './data/', "訓練データのディレクトリ")
tf.app.flags.DEFINE_string('checkpoint_dir', './checkpoints/',
                           "チェックポイントを保存するディレクトリ")
tf.app.flags.DEFINE_string('test_data', None, "テストデータのパス")
tf.app.flags.DEFINE_string('graph_dir', './graphs/',
                           "グラフを保存するディレクトリ")


def _loss(logits, label):
  labels = tf.cast(label, tf.int64)
  cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
    logits, labels, name='cross_entropy_per_example')
  cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
  return cross_entropy_mean


def _train(total_loss, global_step):
  opt = tf.train.GradientDescentOptimizer(learning_rate=FLAGS.learning_rate)
  grads = opt.compute_gradients(total_loss)
  train_op = opt.apply_gradients(grads, global_step=global_step)
  return train_op


filenames = [
  os.path.join(FLAGS.data_dir, 'data_batch_%d.bin' % i) for i in range(1, 6)
  ]


def main(argv=None):
  global_step = tf.Variable(0, trainable=False)

  train_placeholder = tf.placeholder(tf.float32,
                                     shape=[32, 32, 3], name='train_image')
  label_placeholder = tf.placeholder(tf.int32, shape=[1], name='label')
  keepprob_placeholder = tf.placeholder_with_default(tf.constant(1.0),
                                                     shape=[],
                                                     name='keep_prob')

  distorted_image = _distort(train_placeholder)

  # eval用のエントリポイント
  input_image = tf.placeholder_with_default(distorted_image,
                                            [32, 32, 3], name="input_image")
  whiten_image = tf.image.per_image_whitening(input_image)

  # (height, width, depth) -> (batch, height, width, depth)
  image_node = tf.expand_dims(whiten_image, 0)

  logits = model.inference(image_node, keepprob_placeholder)
  total_loss = _loss(logits, label_placeholder)
  train_op = _train(total_loss, global_step)

  top_k_op = tf.nn.in_top_k(logits, label_placeholder, 1)

  saver = tf.train.Saver(tf.all_variables())

  with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())

    total_duration = 0

    # _restore(saver, sess)
    _export_graph(sess, 0)

    for epoch in range(1, FLAGS.epoch + 1):
      start_time = time.time()

      for file_index in range(5):
        print('Epoch %d: %s' % (epoch, filenames[file_index]))
        reader = Cifar10Reader(filenames[file_index])

        for index in range(10000):
          image = reader.read(index)

          _, loss_value = sess.run([train_op, total_loss],
                                   feed_dict={
                                     train_placeholder: image.byte_array,
                                     label_placeholder: image.label,
                                     keepprob_placeholder: 0.5
                                   })

          assert not np.isnan(loss_value), 'Model diverged with loss = NaN'

          if index % 1000 == 0:
            print('loss_value : %.3f' % loss_value)

        reader.close()

      duration = time.time() - start_time
      total_duration += duration

      prediction = _eval(sess, top_k_op,
                         train_placeholder, label_placeholder)
      print('epoch %d duration = %d sec, prediction = %.3f'
            % (epoch, duration, prediction))

      tf.train.SummaryWriter(FLAGS.checkpoint_dir, sess.graph)
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


def _eval(sess, top_k_op, input_image, label_placeholder):
  if not FLAGS.test_data:
    return np.nan

  image_reader = Cifar10Reader(FLAGS.test_data)
  true_count = 0
  for index in range(10000):
    image = image_reader.read(index)

    predictions = sess.run([top_k_op],
                           feed_dict={
                             input_image: image.byte_array,
                             label_placeholder: image.label,
                           })
    true_count += np.sum(predictions)
  image_reader.close()

  return (true_count / 10000.0)


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
