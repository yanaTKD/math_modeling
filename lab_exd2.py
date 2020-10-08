a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует')
    if a == b or a == c or c == b:
        print('Треугольник равнобедренный')
    elif a == b and b == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не может существовать')