import math as m

R = float(input("В ведите R: "))

x = float(input("В ведите x: "))
y = float(input("В ведите y: "))

if ((x**2 + y**2 <= R ** 2) and (x * y <= 0)):
    print("Точка в области")
else:
    print("Точка не в области")