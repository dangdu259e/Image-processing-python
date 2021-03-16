# application extract a blue colored object

# request
#   1: take each frame of video
#   2: Convert from BGR to HSV color-space
#   3: Threshold the HSV Image for range of BlueColor
#   4: Extract the blue Object alone

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(cap)

while (1):
    # take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # threshold HSV image to get only Blue Colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # bitwise_AND mask and original img
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    print (k)
    if (k == 27):
        break
cv2.destroyAllWindows()
