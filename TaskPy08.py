# 8.Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

# Вариант 1
from random import randint

x = randint(-100, 100)
y = randint(-100, 100)

def get_quarter_number(x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            if x > 0:
                return 1
            else:
                return 3
        else:
            if x < 0:
                return 2
            else:
                return 4
    else:
        if x == 0:
            return 'OY'
        else:
            return 'OX'

print(f'Точка: {x, y}')
print(f'Четверть: {get_quarter_number(x, y)}')

# Вариант 2
x = int(input('Введите координаты точки X: '))
y = int(input('Введите координаты точки Y: '))

if x > 0 and y > 0:
    print(f' Точка с координатами {x, y} находится в 1 четверти')
if x < 0 and y > 0:
    print(f' Точка с координатами {x, y} находится в 2 четверти')
if x < 0 and y < 0:
    print(f' Точка с координатами {x, y} находится в 3 четверти')
if x < 0 and y > 0:
    print(f' Точка с координатами {x, y} находится в 4 четверти')
if x == 0 and not y == 0:
    print(f' Точка с координатами {x, y} находится на оси x')
if not x == 0 and y == 0:
    print(f' Точка с координатами {x, y} находится на оси y')
if y == 0 and x == 0:
    print(f' Точка с координатами {x, y} находится в начале координат')