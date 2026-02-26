import math as m

a = int(input())
b = int(input())
h = int(input())

for i in range(a, b + 1, h):
    print(i, m.fabs(i**2 - 5*i + 6) - 0.5)

