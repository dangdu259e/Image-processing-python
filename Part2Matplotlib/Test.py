import cv2
import numpy as np
import matplotlib.pyplot as plt

# đọc ảnh
img1 = cv2.imread('digits.png', 0)

# lấy kích thước
(widthImg, heightImg) = img1.shape
print("widthImg: ", widthImg)
print("heightImg: ", heightImg)

# cắt ảnh lấy chữ

print(img1[:, 0])
print(img1[:, 0].size)
