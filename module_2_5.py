def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([value])
        matrix[i] = [value] * m
    total = matrix
    print(total)

get_matrix(4, 2, 13)