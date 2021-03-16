import numpy as np
import time
import matplotlib.pyplot as plt

def selectionSort(a):
    for i in range(0, len(a) - 1):
        min_index = i
        for j in range(i, len(a)):
            if (a[j] < a[min_index]):
                min_index = j
                temp = a[i]
                a[i] = a[min_index]
                a[min_index] = temp
    return a

def runTime(a):
    start = time.time()
    a_sorted = selectionSort(a)
    end = time.time()
    a_runtime = end - start
    return a_runtime


# a = [9, 8, 7, 6, 5, 3, 2,2]
# print(selectionSort(a))
dl1 = np.random.randint(0, 1000, size=10)  # tri gia 10 so
a = np.random.randint(0, 1000, size=90)
b = np.random.randint(0, 1000, size=900)

dl2 = np.append(dl1, a)  # tri gia 100 so
dl3 = np.append(dl2, b)  # tri gia 1000 so

dl1_runtime = runTime(dl1)
dl2_runtime = runTime(dl2)
dl3_runtime = runTime(dl3)
print(dl3_runtime)
print(type(dl3_runtime))

# Data for plotting
input_size = (len(dl1), len(dl2), len(dl3))
run_time = (dl1_runtime, dl2_runtime, dl3_runtime)

fig, ax = plt.subplots()
print(fig)
ax.plot(input_size, run_time)

ax.set(xlabel='input size', ylabel='run time (s)',
       title='Runtime selection sort with input size')
ax.grid()

fig.savefig("test.png")
plt.show()
