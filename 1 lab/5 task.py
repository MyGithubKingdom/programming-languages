import math as m

radius = float(input("Радиус в метрах: "))
hight = float(input("Высота в метрах: "))

q = 2500 #кг/м^2

a = radius * m.sqrt(3)
S_osnovania = (a ** 2 * m.sqrt(3))/4
V = S_osnovania * hight
S_bokovi = a * hight
S = S_osnovania * 2 + S_bokovi * 3
m = q * V

print("Масса: ", m)
print("Площадь поверхности: ", S)
print("Объём: ", V)