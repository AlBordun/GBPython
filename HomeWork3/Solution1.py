# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

n= int(input('количество элементов в массиве '))
A = [random.randint(0, 10) for i in range(n)]
print(A)
x = int(input('Число для поиска '))
print(A.count(x))