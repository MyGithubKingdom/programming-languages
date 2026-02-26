A = int(input())
B = int(input())

summ = 0

for i in range(100, 1000):
    if sum(map(int, str(i))) == A and i % 10 == B:
        summ += 1

print(summ)