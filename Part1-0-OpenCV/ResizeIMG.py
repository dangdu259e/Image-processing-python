import cv2

#   Đọc hình
img = cv2.imread('picture.jpg', 0)

#   Kiểm tra hình
# cv2.imshow('title', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

#   thay đổi kích thước
(h, w) = img.shape  # lấy kích thước ảnh gốc
r = 300.0 / w
newsize = (300, int(h * r))
# newsize = (300, 300)
print(newsize)

imgresized = cv2.resize(img, newsize)

# kích thước ảnh mới
print("kích thước ảnh mới: ", imgresized.shape)
print("height ảnh mới: ", imgresized.shape[0])
print("width ảnh mới: ", imgresized.shape[1])

# show ảnh sau khi resize
cv2.imshow('title', imgresized)
cv2.waitKey()
cv2.destroyAllWindows()
