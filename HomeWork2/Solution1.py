# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

import random
n = int(input("Кол-во монеток: "))
v = [random.randint(0, 1) for i in range(n)]
count = 0
for i in range(n):
    if v[i] == 1:
        count += 1
print(v)
print(count if count<n/2 else n-count)