from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import argparse
import os
import json
import glob
import random
import collections
import math
import time
import base64
from PIL import Image

im_path = "data_test/test.jpg"


def convert_image_to_base64(im_path):
    with open(im_path, 'rb') as f:
        im_base64 = base64.b64encode(f.read())
    return im_base64


def generator_from_saver(image):
    tmp_graph = tf.Graph()
    checkpoint = "/home/zyt/project/Archi/pix2pix-tensorflow/saved_generator2/"
    with tmp_graph.as_default():
        ckpt= tf.train.latest_checkpoint(checkpoint)
        saver = tf.train.import_meta_graph(ckpt + ".meta")
        with tf.Session() as sess:
            saver.restore(sess, ckpt)

            for op in tmp_graph.get_operations():
                print(op.name, " ", op.type)

            """
            outputs = tf.get_collection("outputs")
            for o in outputs:
                print(sess.run(o))
            """
            g_image = sess.run(tf.get_default_graph().get_tensor_by_name('EncodePng:0'), feed_dict={'Placeholder:0': image})
            return g_image


def main():
    with open(im_path, 'r') as f:
        image = f.read()
    fake_image = generator_from_saver(image)

    with open("data_test/output2.png", 'wb') as f:
        f.write(fake_image)

    print("successfully")

main()
