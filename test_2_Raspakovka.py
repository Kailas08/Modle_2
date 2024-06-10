my_list = [[[1, 2, 3], ["one", 5, 6]], [{"seven":7, "восемь":8, "девять":9}, (0, 33, 77)]]
print(my_list)
list_1 = []
for i in my_list:
    for j in i:
        for k in j:
            a = "".join(str(k))
            list_1.append(a)
print(list_1)
print(" ".join(list_1))