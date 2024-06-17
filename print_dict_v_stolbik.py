string_ = '2025-12-31'
list_ = ['year', 'month', 'day']
list_1 = list(map(int, string_.split("-")))
print(list_1)
dict_ = dict(zip(list_, list_1))
for k, v in dict_.items():
    print(f'{k} : {v}')