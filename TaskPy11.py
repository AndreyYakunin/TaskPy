# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д

# Вариант 1
n = int(input('Введите число: '))

def get_degree(n):
    return [((-3)**i) for i in range(n)]

print (get_degree(n))

# Вариант 2
# list = []
# N = int(input('Введите количество членов последовательности: '))
# for i in range(N):
#     if i % 2 == 0:
#         list.append(3**i)
#     else:
#         list.append(-3**i)
# print(list)
# Вариант 3
# import os
# os.system("cls")
#
# def sub (x):
#     if x in [0,1]:
#         return 1
#     else:
#         return sub (x-1)*-3
# list = []
# for N in range (1,10):
#     list.append (sub(N)) # Добавление элемента в конец списка
# print (list)