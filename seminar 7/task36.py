
# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    matrix = []
    for i in range(1, num_rows+1):
        matrix.append(list([i]))
        if i == 1:
            matrix[i - 1] += list(range(2, num_columns+1))
        else:
            matrix[i - 1] += list(map(operation, range(2, num_columns + 1), [i] * num_rows))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t')
        print()

print_operation_table(lambda x, y: x * y)