# LING-L 445: Course Project
# Dante Razo, drazo, 4/20/2019
import tensorflow as tf

# sess = tf.Session()
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

with tf.device('/gpu:0'):
    print("placeholder")
