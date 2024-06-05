def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ("Салют", False, 3.14)
values_dict = {"a":"One", "b":"Two", "c":"Three"}
values_list_2 = [1.732, "Пирамида"]


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 78)


