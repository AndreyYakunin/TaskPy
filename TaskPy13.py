# 13.	Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# Вариант 1

from itertools import count

value1 = str(input('Введите данные: '))
value2 = str(input('Введите данные: '))

def determ_occur(val1, val2):
    return val2.count(val1)

print(determ_occur(value1, value2))

# Вариант 2

str1 = input("Введите первую строку для проверки:")
str2 = input("Введите вторую строку для поиска в первой строке:")

print(f"Вторая строка входит в первую {str1.count(str2)} раз(а).")


# Вариант 3

from itertools import count
import os
os.system('cls')

str1 = '''Один из наиболее известных русских писателей и мыслителей, 
            один из величайших писателей-романистов мира. Участник обороны Севастополя. 
            Просветитель, публицист, религиозный мыслитель, его авторитетное мнение 
            послужило причиной возникновения нового религиозно-нравственного течения - толстовства. 
            За свои взгляды был отлучён от РПЦ. Член-корреспондент Императорской Академии наук, 
            почётный академик по разряду изящной словесности. Был номинирован на 
            Нобелевскую премию по литературе. Впоследствии отказался от дальнейших номинаций. 
            Классик мировой литературы.'''
str2 = 'из'


print('Количество вхождений второй строки в первую: ',
      str1.count(str2), '\n')