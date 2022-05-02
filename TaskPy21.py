# 21. Определить позицию второго вхождения строки в списке либо сообщить, что его нет.

value1 = 'qwe'
value2 = 'qwe asd zxc qwe ertqwe'

n = 3
def get_sec_entry(val1, val2):
    start = val2.find(val1)
    return val2.find(val1, start + 1)

print(get_sec_entry(value1, value2))