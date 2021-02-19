import cv2

img = cv2.imread('picture.jpg', 0)

(h,w) = img.shape
center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, 45,  1.0)
retated = cv2.warpAffine(img,M ,(w,h))

cv2.imshow('title', retated)
cv2.waitKey()