import numpy as np

_A = [[1, 2, 3], [4, 5, 6], [7,8,9]]
A = np.array(_A)
print("matrix A: \n" + str(A))
print("*******************")
# _B = [1, 2, 3, 4, 5, 6, 7, 8]
# B = np.array(_B)
# print("vector: " + str(B))

# inra
print("A[0,1] :" + str(A[0, 1]))
print("A[:,0] :" + str(A[:, 0]))
print("A[0,:] :" + str(A[0, :]))

print ("____________________")
A_i = np.linalg.pinv(A)
print(A_i)