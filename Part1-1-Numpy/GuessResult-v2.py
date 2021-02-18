import numpy as np

# import toàn bộ file univariate.txt  cột đầu là dân số, cột 2 là lợi nhuận
# mỗi dòng gồm 1 bộ (dân số, lợi nhuận)
_X = np.loadtxt('multivariate.txt', dtype=float, delimiter=",")
# print (X)
# print(np.size(X))

# import theta từ file univariate_theta.txt
theta = np.loadtxt('multivariate_theta.txt', dtype=float, delimiter=',')
# print(theta)

# tạo ma trận X kích thước bằng ma trận _X
X = np.zeros((np.size(_X, 0), np.size(_X, 1)))

# thêm cột đầu bằng một
X[:, 0] = 1

# thêm các cột từ X1 - Xn
n = np.size(_X, 1) - 1
X[:, 1:] = _X[:, 0:n]
# print(X)

# Tính lợi nhuận (đơn vị: 10000$)
predict = X @ theta
# print (predict)

# Chuyển lợi nhuận về đơn vị đô la
predict = predict * 10000

print('%.2f feet-vuông, : %d phòng ngủ %.1f$:' % (X[0, 1], X[0, 2], predict[0]))

print("----------------------")
np.savetxt('predict_value_v2.txt', predict, fmt='%.6f')
