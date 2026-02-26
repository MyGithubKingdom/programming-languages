import math as m

x1 = int(input())
x2 = int(input())
h = int(input())

a = 2.8
b = -0.3
c = 4

for i in range(x1, x2 + 1, h):
    if i < 2:
        print(a*i**2 + b*i + c)
    elif i > 3:
        print((a + b*i)/m.sqrt(i**2 + 1))
    else:
        print(a/i + m.sqrt(i**2 + 1))


