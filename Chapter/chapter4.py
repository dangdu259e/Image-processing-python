import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
img = np.zeros((512, 1024, 3), np.uint8)
(height, width, dim) = img.shape
# print(img)
# img[:] = 255, 0, 0

# img.shape[1], img.shape[0]: tọa độ trong hình
# đường chéo từ trên xuống (trên trái xuống góc phải)

# img.shape[1] = width = 1024
# img.shape[0] = height = 512
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 30)

# đường chéo từ dưới lên (góc trái lên trên phải)
start_point = (0, img.shape[0])  # (0, height) = (0, 512)
end_point = (img.shape[1], 0)  # (width, 0) = (1024,0)
cv2.line(img, start_point, end_point, (255, 0, 0), 3)

cv2.imshow("img", img)

cv2.waitKey()
