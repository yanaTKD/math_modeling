import math

figure = input()

def krug_func(r):
    S = math.pi * (r ** 2)
    return S

def pr_func(a, b):
    S = a * b
    return S

def tr_func(c, d, f):
    p = (c + d + f) / 2
    S = math.sqrt((p * (p - c) * (p - d) * (p - f)))
    return S

if figure == 'круг':
    i = krug_func(int(input()))
    print(i)
elif figure == 'прямоугольник':
    j = pr_func(int(input()),int(input()))
    print(j)
elif figure == 'треугольник':
    h = tr_func(int(input()),int(input()),int(input()))
    print(h)