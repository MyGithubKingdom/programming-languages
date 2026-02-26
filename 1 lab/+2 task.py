import math as m

x = float(input("В ведите x: "))
y = float(input("В ведите y: "))

if ((x**2 + y**2 >= 0.5**2) and (x**2 + y**2 <= 1**2)):
    print("Точка в области")
else:
    print("Точка не в области")