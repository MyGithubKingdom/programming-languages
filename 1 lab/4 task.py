import math as m

x = float(input("x = "))
y = float(input("y = "))

s = (m.e**x + m.cos(m.e**y)**2) / (x + y)**2
z = m.sqrt(x + y) * (m.sin(x)**3 + m.cos(y)**2)


print("s = ", s)
print("z = ", z)