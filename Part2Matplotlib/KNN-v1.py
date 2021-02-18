# thuật toán láng giềng gần nhất, K-nearest-neibour

# tập dữ liệu truyền vào

import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
print(trainData)

ketqua = np.random.randint(0, 2, (25, 1)).astype(np.float32)
print(ketqua)

red = trainData[ketqua.ravel() == 1]
blue = trainData[ketqua.ravel() == 0]
# print(red)
# print(blue)

#Đối tượng cần xét
newMember = np.random.randint(0,100,(1,2)).astype(np.float32)
print("newMember: " , newMember)
# print(red[:, 1])

plt.scatter(red[:, 1], red[:, 0], 100, 'r', 's')
plt.scatter(blue[:, 1], blue[:, 0], 100, 'b', '^')
plt.scatter(newMember[:, 1], newMember[:, 0], 100, 'g', 'o')
knn = cv2.ml.KNearest_create()
knn.train(trainData,0,ketqua)
results = knn.findNearest(newMember,4)
print("results: ",results)
temp, result, hangxom, khoangcach = knn.findNearest(newMember,10)

print("result: {}\n".format(result))
print("hangxom: {}\n".format(hangxom))
print("khoangcach: {}\n".format(khoangcach))
plt.show()
