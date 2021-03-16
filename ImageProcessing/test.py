# import cv2
#
# img = cv2.imread('../Resource/people.jpg',1)
#
# print(img[0,0])
# #BGR\

import math


def areaTriangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print(areaTriangle(3,4,5))



















