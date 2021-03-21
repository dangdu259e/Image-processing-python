import numpy as np
from scipy import linalg
from scipy.sparse import csr_matrix, csc_matrix


def random_vector(n):  # tao vector n chieu
    a = np.random.randint(-10, 10, size=(n), dtype=int)
    return a


def random_matrix(n):  # tao ma tran vuong n*n cac ptu ngau nhien [0-10]
    a = np.random.randint(0, 10, size=(n, n), dtype=int)
    return a


def matrix_multiply_vector(matrix, vector):
    result = matrix.dot(vector)
    return result


def det_matrix(matrix):
    return linalg.det(matrix)


def matrannghichdao(matrix):
    # Ma trận có ít nhất 1 dòng không (hoặc cột không) đều không khả nghịch.
    kichthuoc = matrix.shape
    # battheohang
    hang = csr_matrix(matrix)
    for i in range(kichthuoc[0]):
        if (hang[i].size == 0):
            return None
    # battheocot
    cot = csc_matrix(matrix)
    for i in range(kichthuoc[1]):
        if (cot[:, i].size == 0):
            return None
    return linalg.inv(matrix)


n = 3
vector = random_vector(n)
matrix = random_matrix(n)
print("vector: " + str(vector))
print()
print("matrix: \n" + str(matrix))
print("*******************")
print("matrix_multiply_vector: " + str(matrix_multiply_vector(matrix, vector)) + "\n")
print("det_matrix: " + str(det_matrix(matrix)) + "\n")
print("ma tran nghich dao: \n" + str(matrannghichdao(matrix)))
