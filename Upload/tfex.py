# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:54:00 2019

@author: MAYANK SHAW
"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

node1 = tf.constant(3, dtype=tf.int32)
node2 = tf.constant(5, dtype=tf.int32)
node3 = tf.add(node1, node2)

sess = tf.Session()

print("Sum of node1 and node2 is : ",sess.run(node3))

sess.close()