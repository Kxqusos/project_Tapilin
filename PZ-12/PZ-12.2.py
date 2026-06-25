#Вариант 16
"""
В матрице найти сумму элементов второй половины матрицы.
"""

import random

row = int(input("Введите количество строк: "))
col = int(input("Введите количество столбцов: "))

#генерируем матрицу
matrix = [
    [random.randint(0, 9) for _ in range(col)] for _ in range(row)
    ]

#превращаем матрицу в 1 список
arr = [z for row in matrix for z in row]

#середина
half = len(arr) // 2

#вторая половина
second = arr[half:]

print("Матрица:")
for row in matrix:
    print(row)

print(f"Сумма второй половины: {sum(second)}")
