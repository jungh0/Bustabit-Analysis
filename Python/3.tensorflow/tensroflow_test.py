
import tensorflow as tf

print(tf.__version__)

import platform
print(platform.python_version())
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))



