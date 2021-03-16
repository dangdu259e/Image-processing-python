# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:06:36 2018

@author: hndung
"""

import numpy as np

# numpy nhanh hơn nhiều so với python thuần túy
# xem
#   https://www.scipy-lectures.org/intro/numpy/array_object.html#numpy-arrays
# hoặc
#   https://www.scipy-lectures.org/intro/numpy/operations.html
L = range(1000)
# %timeit [i**2 for i in L]

a = np.arange(1000)
# %timeit a**2

############################
# Các loại mảng
# https://www.scipy-lectures.org/intro/numpy/array_object.html#numpy-arrays
############################
# 1d array
a = np.array([0, 1, 2, 3])
print(a)
# số chiều của mảng
a.ndim
# shape: https://www.hackerrank.com/challenges/np-shape-reshape/problem
# kích thước của mảng
a.shape
len(a)
a[0]

# 2 dimensional array: 2 x 3 array
b = np.array([[0, 1, 2], [3, 4, 5]])
print(b)
# số chiều của mảng
b.ndim
# kích thước của mảng
b.shape
# returns the size of the first dimension
len(b)
# returns the size of the second dimension
len(b[0])
b[0,0]
b[0,2] # first line, third column
b[1,1] # second line, second column

# 3D array
c = np.array([[[1], [2]], [[3], [4]]])
# số chiều của mảng
c.ndim
# kích thước của mảng
c.shape

############################
# Tạo mảng
############################
# thực tế ta thường không đánh vào từng giá trị của mảng mà sử dụng các hàm
# hoặc đọc vào từ dữ liệu
# 0 .. n-1
a = np.arange(10)
a

# start, end (exclusive), step
b = np.arange(1, 9, 2) # start, end (exclusive), step
b

# start, end, num-points
c = np.linspace(0, 1, 6)
c

# mảng 1 chiều các số 1
a = np.ones(3)
a

# mảng 2 chiều 2x3 các số 1
a = np.ones((2,3))
a

# mảng 1 chiều các số 0
b = np.zeros(3)
b

# mảng 2 chiều 3x2 các số 1
b = np.zeros((3,2))
b

# mảng (ma trận) đơn vị
c = np.eye(4)
c

# ma trận đường chéo
d = np.diag(np.array([1, 2, 3, 4]))
d

d = np.diag(np.arange(1,5))
d

# random
# uniform in [0, 1]
a = np.random.rand(4)
a

# Gaussian
b = np.random.randn(4)
b

# cố định random seed
np.random.seed(1234)

############################
# slicing:
# https://www.scipy-lectures.org/intro/numpy/array_object.html#indexing-and-slicing
############################
a = np.arange(10)
a
a[-1]    # last element
a[-3]    # 3.rd element from the last element

a[2:8:3] # [start:end:step]  (>=start, <end)
a[1:3]   # [start:end:1]
a[:3]    # [0:end:1]
a[3:]    # [start:last:1]
a[-1:]
a[:-1]
a[-2:]
a[:-2]

# reversing a sequence
a[::-1]
a[::-2]

# assignment and slicing
a = np.arange(10)
a
a[5:] = 10
a

b = np.arange(5)
a[5:] = b[::-1]
a

############################
# data type
# https://www.scipy-lectures.org/intro/numpy/array_object.html#basic-data-types
############################
a = np.array([1, 2, 3])
a.dtype

b = np.array([1., 2., 3.])
b.dtype

# b cần nhiều bộ nhớ hơn a
from sys import getsizeof
getsizeof(a)
getsizeof(b)

# có thể đưa ra chính xác loại data-type mình muốn có
c = np.array([1, 2, 3], dtype=float)
c.dtype

d = np.array([True, False, False, True])
d.dtype


############################
# Operations
# https://www.scipy-lectures.org/intro/numpy/operations.html
############################
a = np.array([1, 2, 3, 4])
a
# Operations with scalar
a + 1
2**a

# Elementwise operations
b = np.ones(4) + 1
a - b
a * b

j = np.arange(5)
2**(j + 1) - j

# Chú ý: nhân mảng không phải là nhân ma trận, nó là phép nhân từng phần tử với nhau
c = np.ones((3, 3))
c * c

# Nhân ma trận
c.dot(c)

A = np.array([[1,2,3],[1,1,0],[0,1,1]])
A

b = np.array([1,1,0])
b

A.dot(b)

# Transposition - Chuyển vị
A.T
b.T

# Chú ý:
# The transposition is a view
# As a results, the following code is wrong and will not make a matrix symmetric:
# It will work for small arrays (because of buffering) but fail for large one, in unpredictable ways.
A += A.T
A

# Note Linear algebra
# The sub-module numpy.linalg implements basic linear algebra, such as solving
# linear systems, singular value decomposition, etc. However, it is not guaranteed
# to be compiled using efficient routines, and thus we recommend the use of
# scipy.linalg, as detailed in section Linear algebra operations: scipy.linalg

# So sánh từng phần tử
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])

a == b

a > b

# So sánh cả mảng
np.array_equal(a,b)

# Hàm logic
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)

np.logical_and(a, b)

# Transcendental functions:
a = np.arange(5)
a
np.sin(a)
np.log(a)
np.exp(a)

# sum 1d array
x = np.array([1, 2, 3, 4])
np.sum(x)
x.sum()

# sum 2d array
x = np.array([[1, 2], [3, 4]])
x
x.sum(axis=0)   # columns (first dimension)
x[:, 0].sum(), x[:, 1].sum()
x.sum(axis=1)   # rows (second dimension)
x[0, :].sum(), x[1, :].sum()

# min/max of array
x = np.array([1, 3, 2])
x.min()
x.max()
x.argmin()  # index of minimum
x.argmax()  # index of maximum

# Logical operations:
np.all([True, True, False])
np.any([True, True, False])

# Sử dụng phép toán trên để so sánh mảng
a = np.zeros((100, 100))
np.any(a != 0)
np.all(a == a)

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
a <= b
b <= c
((a <= b) & (b <= c)).all()

# Sinh viên tự đọc
#   https://www.scipy-lectures.org/intro/numpy/operations.html#broadcasting
#   https://www.scipy-lectures.org/intro/numpy/operations.html#array-shape-manipulation
#   https://www.scipy-lectures.org/intro/numpy/operations.html#sorting-data


############################
# polynomial
# https://www.scipy-lectures.org/intro/numpy/advanced_operations.html#polynomials
############################
p = np.poly1d([3, 2, -1])
p(0)
p.roots
