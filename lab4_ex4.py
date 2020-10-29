def prost_func(a, b, n):
    nn = (b - a) // n
    N = []
    y = 0
    for i in range(a, b,nn):
        y = i ** 2
        N.append(y)
    return N
t = prost_func(1, 10, 2)
print(t)