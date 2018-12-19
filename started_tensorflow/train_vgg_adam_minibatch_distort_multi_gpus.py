# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import math
from datetime import datetime

import numpy as np
import tensorflow as tf

# import model_vgg_lite_minibatch as model
import model_normalized_dropout_minibatch as model

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
tf.app.flags.DEFINE_integer('num_gpus', 1, "使用するGPUの数")

TOWER_NAME = 'tower'
KEY_LOSSES = 'losses'

filenames = [
  os.path.join(FLAGS.data_dir, 'data_batch_%d.bin' % i) for i in range(1, 6)
  ]


def _loss(logits, label):
  print(logits.get_shape())
  print(label.get_shape())

  labels = tf.cast(label, tf.int64)
  cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
    logits, labels, name='cross_entropy_per_example')
  cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
  return cross_entropy_mean


def _average_gradients(tower_grads):
  average_grads = []
  for grad_and_vars in zip(*tower_grads):
    grads = []
    for g, _ in grad_and_vars:
      expanded_g = tf.expand_dims(g, 0)

      grads.append(expanded_g)

    grad = tf.concat(0, grads)
    grad = tf.reduce_mean(grad, 0)

    v = grad_and_vars[0][1]
    grad_and_var = (grad, v)
    average_grads.append(grad_and_var)
  return average_grads


def main(argv=None):
  print('started at %s' % __datetime())

  global_step = tf.Variable(0, trainable=False)

  keepprob_placeholder = tf.placeholder_with_default(tf.constant(1.0),
                                                     shape=[],
                                                     name='keep_prob')

  opt = tf.train.AdamOptimizer(learning_rate=FLAGS.learning_rate)

  tower_grads = []
  for i in range(FLAGS.num_gpus):
    with tf.device('/gpu:%d' % i):
      with tf.name_scope('%s_%d' % (TOWER_NAME, i)) as scope:
        reader = Cifar10Reader(filenames)
        record = reader.read()

        distorted_image = _distort(record.byte_array)
        whiten_image = tf.image.per_image_whitening(distorted_image)

        batch_image, batch_label = tf.train.batch(
          [whiten_image, record.label],
          FLAGS.batch_size,
          num_threads=6)
        tf.image_summary('images', batch_image)

        batch_label = tf.reshape(batch_label, [FLAGS.batch_size], 'batch_label')

        logits = model.inference(batch_image,
                                 keepprob_placeholder, batch_size=FLAGS.batch_size)
        loss = _loss(logits, batch_label)
        tf.add_to_collection(KEY_LOSSES, loss)

        tf.get_variable_scope().reuse_variables()

        losses = tf.get_collection(KEY_LOSSES, scope)

        # nameを指定しないと'cross_entropy'と名前が重複してエラーになる
        total_loss = tf.add_n(losses, name='total_loss')

        grads = opt.compute_gradients(total_loss)
        tower_grads.append(grads)

  avg_grads = _average_gradients(tower_grads)

  train_op = opt.apply_gradients(avg_grads, global_step=global_step, name='train')

  saver = tf.train.Saver(tf.all_variables())

  config = tf.ConfigProto(
    allow_soft_placement=True)

  with tf.Session(config=config) as sess:
    sess.run(tf.initialize_all_variables())

    total_duration = 0

    tf.train.start_queue_runners(sess=sess)

    num_steps_of_epoch = math.ceil(10000 * 5 / FLAGS.batch_size)
    for step in range(num_steps_of_epoch * (FLAGS.epoch + 1)):
      _, loss_value = sess.run([train_op, total_loss],
                               feed_dict={
                                 keepprob_placeholder: 0.5
                               })

      assert not np.isnan(loss_value), \
        'Model diverged with loss = NaN'

      if step % 10 == 0:
        print('loss_value : %.3f' % loss_value)

      if step % num_steps_of_epoch == 0:
        epoch = int(step / num_steps_of_epoch)
        file_name = os.path.basename('%s_model.ckpt' % (__file__))
        checkpoint_path = os.path.join(FLAGS.checkpoint_dir, file_name)
        saver.save(sess, checkpoint_path, global_step=epoch)

        print('Epoch %d at %s' % (epoch, __datetime()))

    print('Total duration = %d sec' % total_duration)

    print('finished at %s' % __datetime())


def __datetime():
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


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


if __name__ == '__main__':
  tf.app.run()
