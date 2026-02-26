import math as m

while (True):
    a = input("Ввидите значение аргумента из диапазона [1;2]: ")
    try:
        x = float(a)
        if (1 <= x <= 2):
            break
        else:
            print(f"Ошибка число {x} не в деапазоне [1;2]")
    except ValueError:
        print("Ошибка введите числовое значение")


y = m.cos(x) - m.e ** (-x**2/2) + x - 1
print(y)