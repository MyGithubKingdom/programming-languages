import math as m

x = float(input("Ввидите значение аргумента из диапазона [1;2]: "))
y = m.cos(x) - m.e ** (-x**2/2) + x - 1
print(y)
print(f"{y:.3f}")