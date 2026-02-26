import math as m

a = int(input("Катет а = "))
b = int(input("Катет b = "))

print("Периметр: ", m.sqrt(a**2 + b**2) + a + b)
print("Площадь: ", a*b/2)