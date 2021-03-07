import cv2

import numpy as np

img = cv2.imread("../Resource/people.jpg")
print(img.shape) #(649, 529, 3) = (height, width, number channel which is RGB)

imgResize = cv2.resize(img, (1000, 200))
print(imgResize.shape)

imgCropped = img [0: 300, 0: 100]
# cv2.imwrite('imgCrop', imgCropped)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)