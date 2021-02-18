import matplotlib.pyplot as plt

#plot giá trị thực tế (không lấy cột bias 1 đầu)
# X[:,1] là giá trị x-axis của biểu đồ, không lấy cột đầu;;
#y là y-axism, rx là red x , plot dữ liệu bằng dấu x màu đỏ
plt.plot(X[:, 1], y, 'rx')