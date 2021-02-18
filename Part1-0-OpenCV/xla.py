import cv2
import numpy as np

img = cv2.imread("img.png", 1)

# print(img.shape)
(h,w,d)= img.shape
print(h,w,d)