# 1. По двум заданным числам проверить, является ли одно квадратом другого

a = int(input('Введите число: '))
b = int(input('Введите число: '))

if a ** 2 == b or b ** 2 == a:

   print('true')
else:
   print('False')