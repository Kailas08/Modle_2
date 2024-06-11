data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(dict_):
    total_sum = 0
    if isinstance(dict_, (int, float)):
        return dict_
    elif isinstance(dict_, str):
        return len(dict_)
    elif isinstance(dict_, (list, tuple, set)):
        for item in dict_:
            total_sum += calculate_structure_sum(item)
    elif isinstance(dict_, dict):
        for key, value in dict_.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    return total_sum
itogo = calculate_structure_sum(data_structure)
print(itogo)