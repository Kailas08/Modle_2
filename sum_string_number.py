# Преобразование строки чисел разделенных запятой
# в список чисел
string_ = "12,34,56"
list_ = list(map(int, string_.split(',')))
print(list_)
a = 0
for i in list_:
    a = a + i
    print(a)