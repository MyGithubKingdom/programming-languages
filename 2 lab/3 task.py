eps = float(input())

k = 1
a = (2 * k)/((k**2 + 1)*(k + 2))
summ = 0

while abs(a) >= eps:
    summ += a
    k += 1
    a = (2 * k)/((k**2 + 1)*(k + 2))
    print(a)

print("Сумма", summ)
