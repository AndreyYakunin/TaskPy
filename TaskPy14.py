# 14. Подсчитать сумму цифр в вещественном числе.


# Вариант 1
from random import uniform

n = round(uniform(1, 100), 3)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))
print('Задано число:', n)
print('Сумма цифр данного числа равна:', sum_digit(n))

# Вариант 2
import  os
import random
os.system("cls")

# Задаем случайное вещественное число из диапазона
n = random.uniform(1, 1001)
print('Задано число:', n)

n = str(n).replace('.', '') # переводим в строковый тип, убираем точку

summa = sum(map(int, n))  # переводим в числовой тип, сумму
print('Сумма цифр данного числа равна:', summa, '\n')