#Вариант 16
"""
В матрице найти суммы элементов каждой строки и поместить их в новый массив. 
Выполнить замену элементов третьего столбца исходной матрицы на полученные 
суммы.
"""

import random

row = int(input("Введите количество строк: "))
col = int(input("Введите количество столбцов: "))

#генерируем матрицу
matrix = [
    [random.randint(0, 9) for _ in range(col)] for _ in range(row)
    ]

#функция считающая сумму каждой строки
def str_sum(matrix):
    sum_arr = []
    for row in matrix:
        sum_arr.append(sum(row))
    return sum_arr



#выводим сгенерированную матрицу
print("Изначальная матрица:")
for row in matrix:
    print(row)

#генерируем массив нового столбца
new_col = str_sum(matrix)
print(f"Суммы каждой строки: {new_col}")

#заменяем столбец
for i, row in enumerate(matrix):
    row[2] = new_col[i]
print("Измененная матрица:")
for row in matrix:
    print(row)
    