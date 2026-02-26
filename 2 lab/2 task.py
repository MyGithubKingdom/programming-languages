n = int(input())

summ = 0
for i in range(n + 1):
    summ += (2 * i) / ((i ** 2 + 1) * (i + 2))

print(summ)
