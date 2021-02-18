import cv2

img = cv2.imread('digits.png',0)
print(img.shape)
(width,heigth)= img.shape
print(width)