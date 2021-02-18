import cv2
img = cv2.imread('dave.jpg', 1)
# cv2.imshow('image', img)
# cv2.line(img, (0,0), (300,300),(0,0,255),5)
# cv2.imwrite('dave.jpg', img)
# cv2.waitKey()
# cv2.destroyAllWindows()
# px = img[0][0]
# img[0][0] = [255, 255, 255]
# cv2.imwrite('dave.jpg', img)
#
# px = img[0,0]
# for i in range (0, 100):
#     img[i][i] = [0,0,0]
#
# cv2.imwrite('dave.jpg', img)
# print(px)

for i in range (200):
    for j in range(200):
        if(img[i,j,0]>30):
            img[i,j]=1
cv2.imwrite('dave.jpg', img)

