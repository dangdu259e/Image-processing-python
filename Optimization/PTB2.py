import math
import matplotlib.pyplot as plt
import numpy as np


def get_type_of_quadratic(a, b, c):
    denta = math.pow(b, 2) - 4 * a * c
    result = ""
    if (denta < 0):
        result = "vô nghiệm"
    elif (denta == 0):
        result = "có đúng 1 nghiệm"
    else:
        result = "có hai nghiệm phân biệt"
    return result


# print(get_type_of_quadratic(1, -3, 2))
# print(get_type_of_quadratic(1, 1, -6))
# print(get_type_of_quadratic(1, 2, 1))

def draw(a, b, c):
    # x = np.random.randint(-100, 100, size=100)
    # x = np.arange(start=-100, stop=100, step=5, dtype=int)
    x = np.linspace(-10, 10, 1000)
    # print(x)
    y = a * x ** 2 + b * x + c
    # y = a * math.pow(x,2) + b * x + c
    # print(y)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='x', ylabel='y',
           title='Đồ thị hàm số bậc 2 \n {}x^2 + {}bx + c '.format(a, b, c))
    ax.grid()
    return plt.show()


draw(1, 4, -12)

# x = np.random.randint(1,10,size= 6)
# print(x)


# a= 1
# b= 2
# c= 1
# x = np.linspace(-2,2,100)
# y =a* math.pow(x,2)+ b*x +c
# y =a* x**2+ b*x +c
# plt.plot(x,y)
# plt.show()
