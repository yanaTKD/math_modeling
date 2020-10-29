from random import random
N = 10
def my_func(arr):
    s = 1
    for i in range(N):
        s *= arr[i]
    return s
tmp = my_func(arr)
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
print(arr)
print(tmp)