# Вариант 18
# В матрице элементы кратные 3 увеличить в 3 раза.

# Создание матрицы
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Проход по матрице и увеличение элементов, кратных 3, в 3 раза
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] *= 3

# Вывод матрицы на экран
for row in matrix:
    print(row)
