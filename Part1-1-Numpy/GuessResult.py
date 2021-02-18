import numpy as np

# import toàn bộ file univariate.txt  cột đầu là dân số, cột 2 là lợi nhuận
# mỗi dòng gồm 1 bộ (dân số, lợi nhuận)
X = np.loadtxt('univariate.txt', dtype=float, delimiter=",")
# print (X)
# print(np.size(X))

# import theta từ file univariate_theta.txt
theta = np.loadtxt('univariate_theta.txt', dtype=float, delimiter=',')
# print(theta)

# Lưu cột y lại
y = np.copy(X[:, -1])
# print(y)

# Chuyển cột đầu tiên sang cột thứ 2
X[:, 1] = X[:, 0]

# đổi cột đầu tiên thành số 1
X[:, 0] = 1
# print (X[:,0])

#Tính lợi nhuận (đơn vị: 10000$)
predict = X@theta
# print (predict)

#Chuyển lợi nhuận về đơn vị đô la
predict = predict * 10000

#in cặp dân số lợi nhuận đầu tiên (đơn vị dân số: người)
print(X[0,1])
print (predict[0])
print ('%d người: %.2f' %(X[0,1]*10000, predict[0]))

print("----------------------")
np.savetxt("predict_value.txt", predict , fmt = '%.2f')

import matplotlib.pyplot as plt

#plot giá trị thực tế (không lấy cột bias 1 đầu)
# X[:,1] là giá trị x-axis của biểu đồ, không lấy cột đầu;;
#y là y-axism, rx là red x , plot dữ liệu bằng dấu x màu đỏ
plt.plot(X[:, 1], y, 'rx')

#plot dự đoán
plt.plot (predict/10000, y, '-b')

plt.show()
