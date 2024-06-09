data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(func_):
    a = len(func_[3])
    for i in func_[0]:
        a = a + i
    b = sum(func_[1].values())
    for i in list(func_[1].keys()):
        b = b + len(i)
    c = func_[2][0] + sum(func_[2][1].values())
    for i in list(func_[2][1].keys()):
        c = c + len(i)
    for i in func_[4]:
        for j in i:
            for k in j:
                #print(k)
                d = k[0] + len(k[1]) + len(k[2][0]) + k[2][1]

    return a + b + c + d

result = calculate_structure_sum(data_structure)
print(result)
