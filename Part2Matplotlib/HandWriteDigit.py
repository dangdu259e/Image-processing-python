# Nhận dạng chữ viết tay bằng python

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread('digits.png', 0)
# cv2.imshow('Du lieu', img)

# (width , weight) img
(width, height) = img.shape

# cắt ảnh ra
# mảng nhiều chiều và nhét vào biến
cells = [np.hsplit(row, 50) for row in np.vsplit(img, 50)]

# cách viết lại biểu thức cell
cells = []
a = np.vsplit(img, 50)  #cắt ảnh gốc ra 50
for i in a:
    b = np.hsplit(i,50)
    cells.append(b)


# kiểm tra
cv2.imwrite("anhtest1chu.jpg", cells[6][0])

#chuyển về mảng trong numpy
# x = np.array(cells)

#in ra được hình chữ O
# xx ở đây vẫn đóng vai trò mảng 2 chiều
# xx=x[0,0]
# print(xx)

#chuyển xx về mảng 1 chiều của x qua hàm reshape
# xx = x[0,0].reshape(-1,400)
# print(xx)






