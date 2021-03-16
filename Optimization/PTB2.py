import math
import matplotlib.pyplot as plt

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

# a = []
# y = a*(math.pow(x,2)) + b*x + c
