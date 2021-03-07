# request1: Convert images from one color-space to another, like BGR <=> Gray, BGR <=> HSV etc
#   có nhiều hơn 150 cách chuyển màu trong openCV nhưng 2 phương pháp BGR <=> gray với cả BGR <=> HSV là được dùng nhiều nhất


# request2: Create application which extracts a colored object in video
# Note: learn following function: cv2.cvtColor(), cv2.inRange() etc.


import cv2

# Cách chuyển màu
#cv2.cvtColor(input_image, flag)

# flags are all color conversion in cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
print(len(flags))

#Để chuyển từ BGR => GRAY conversion, sử dụng:  cv2.COLOR_BGR2GRAY
#Để chuyển từ BGR => HSV conversion, sử dụng:  cv2.COLOR_BGR2HSV
#example
img = cv2.imread('../Resource/people.jpg',1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#đảo ngược màu BGR <=> RGB
img_transfer = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow("IMG", img)
cv2.imshow("IMG GRAY", img_gray)
cv2.imshow("IMG HSV", img_hsv)
cv2.imshow("IMG Trasfer", img_transfer)

cv2.waitKey()
cv2.destroyAllWindows()


#Note: For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].
# Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges



