import numpy as np

_A = [[1, 2, 3, 4,5,6],
      [4, 5, 6, 7,8,9],
      [7, 8, 9, 10,11,12],
      [7, 8, 9, 10,11,12]
      ]
A = np.array(_A, dtype=None)
print("matrix A : \n" + str(A))
print("--------------")
print("begin matrix: \n" + str(np.hsplit(A, 3)[0]))
print("end matrix: \n" + str(np.hsplit(A, 2)[1]))
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print (np.vsplit(A,2))