# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


class Cifar10Record(object):
  width = 32
  height = 32
  depth = 3

  def set_label(self, label):
    self.label = tf.cast(label, tf.int32)

  def set_image(self, image):
    reshaped_image = tf.reshape(image,
                                [self.depth, self.height, self.width])

    # Convert from [depth, height, width] to [height, width, depth].
    reshaped_image = tf.transpose(reshaped_image, [1, 2, 0])

    self.byte_array = tf.cast(reshaped_image, tf.float32)


class Cifar10Reader(object):
  filename_queue = None

  def __init__(self, filenames):
    self.filename_queue = tf.train.string_input_producer(filenames)

  def close(self):
    pass

  def read(self):
    result = Cifar10Record()

    label_bytes = 1
    image_bytes = result.height * result.width * result.depth
    record_bytes = label_bytes + image_bytes

    self.reader = tf.FixedLengthRecordReader(record_bytes=record_bytes)
    key, value = self.reader.read(self.filename_queue)

    byte_buffer = tf.decode_raw(value, tf.uint8)

    result.set_label(tf.slice(byte_buffer, [0], [label_bytes]))
    result.set_image(tf.slice(byte_buffer, [1], [image_bytes]))

    return result
