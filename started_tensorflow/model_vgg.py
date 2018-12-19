# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

# VGGNetのモデル定義。CIFAR-10には適用できない

NUM_CLASSES = 10


def _get_weights(shape, stddev=1.0):
  var = tf.get_variable('weights', shape,
                        initializer=tf.truncated_normal_initializer(stddev=stddev))
  return var


def _get_biases(shape, value=0.0):
  var = tf.get_variable('biases', shape,
                        initializer=tf.constant_initializer(value))
  return var


def _conv(name, input_layer, weights_shape, biases_size):
  with tf.variable_scope(name) as scope:
    weights = _get_weights(shape=weights_shape, stddev=1e-2)
    conv = tf.nn.conv2d(input_layer, weights, [1, 1, 1, 1], padding='SAME')
    biases = _get_biases([biases_size], value=0.1)
    bias = tf.nn.bias_add(conv, biases)
    return tf.nn.relu(bias, name=scope.name)


def _pool(name, input_layer, ksize):
  return tf.nn.max_pool(input_layer, ksize=ksize, strides=[1, 2, 2, 1],
                        padding='SAME', name=name)


def _fc(name, input_layer, weights_shape, biases_size, keep_prob):
  with tf.variable_scope(name) as scope:
    weights = _get_weights(shape=weights_shape, stddev=0.04)
    biases = _get_biases([biases_size], value=0.1)
    fc = tf.nn.relu(tf.matmul(input_layer, weights) + biases, name=scope.name)
    fc = tf.nn.dropout(fc, keep_prob)
    return fc


def inference(image_node, keep_prob):
  conv1_1 = _conv('conv1_1', image_node, [3, 3, 3, 64], 64)
  conv1_2 = _conv('conv1_2', conv1_1, [3, 3, 64, 64], 64)
  pool1 = _pool('pool1', conv1_2, [1, 2, 2, 1])

  conv2_1 = _conv('conv2_1', pool1, [3, 3, 64, 128], 128)
  conv2_2 = _conv('conv2_2', conv2_1, [3, 3, 128, 128], 128)
  pool2 = _pool('pool2', conv2_2, [1, 2, 2, 1])

  conv3_1 = _conv('conv3_1', pool2, [3, 3, 128, 256], 256)
  conv3_2 = _conv('conv3_2', conv3_1, [3, 3, 256, 256], 256)
  conv3_3 = _conv('conv3_3', conv3_2, [3, 3, 256, 256], 256)
  pool3 = _pool('pool3', conv3_3, [1, 2, 2, 1])

  conv4_1 = _conv('conv4_1', pool3, [3, 3, 256, 512], 512)
  conv4_2 = _conv('conv4_2', conv4_1, [3, 3, 512, 512], 512)
  conv4_3 = _conv('conv4_3', conv4_2, [3, 3, 512, 512], 512)
  pool4 = _pool('pool4', conv4_3, [1, 2, 2, 1])

  conv5_1 = _conv('conv5_1', pool4, [3, 3, 512, 512], 512)
  conv5_2 = _conv('conv5_2', conv5_1, [3, 3, 512, 512], 512)
  conv5_3 = _conv('conv5_3', conv5_2, [3, 3, 512, 512], 512)
  pool5 = _pool("pool_5", conv5_3, [1, 2, 2, 1])

  reshape = tf.reshape(pool5, [1, -1])
  dim = reshape.get_shape()[1].value

  fc6 = _fc('fc6', reshape, [dim, 4096], 4096, keep_prob)
  fc7 = _fc('fc7', fc6, [4096, 4096], 4096, keep_prob)

  # output
  with tf.variable_scope('output') as scope:
    weights = _get_weights(shape=[4096, NUM_CLASSES], stddev=1 / 4096.0)
    biases = _get_biases([NUM_CLASSES], value=0.0)
    logits = tf.add(tf.matmul(fc7, weights), biases, name='logits')

  return logits
