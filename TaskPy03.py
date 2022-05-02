# 3.Вывести на экран числа от -N до N
n = abs(int(input()))
for i in range(-n, n + 1):
    print(i, end = ' ')