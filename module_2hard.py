number = int(input("Введите код - целое число от 3 до 20  "))
list = []
for j in range(1, 10):
    for k in range(1, 20):
        if ((number % (j + k) == 0) and (j + k) <= number and (j < k)):
            list.append([j, k])
password = list
outlst = [''.join([str(c) for c in lst]) for lst in password]
print("Пароль для открывания дверей ", *outlst)
