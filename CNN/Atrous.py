import numpy as np
import tensorflow as tf

x = np.array([[1, 0, 1, 0, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1]], dtype=np.float32)
x_pad = np.pad(x, pad_width=2)  # thêm padding = 2
print("x_pad")
print(x_pad)
print('---------------------------')
x_in = x_pad.reshape((1, 9, 9, 1))  # lấy theo từng cột đặt vào list x_in
print("x_in")
print(x_in)
print('-----------------------')
kernel = np.ones(shape=(3, 3, 1, 1), dtype=np.float32)
print("kernel")
print(kernel)
output = tf.nn.atrous_conv2d(x_in, kernel, rate=2, padding='VALID')
print(output)
