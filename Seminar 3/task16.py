# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1


import random

def STask16():
    count = 0
    n = int(input("Введите количество элементов в массиве: "))
    print(n)
    listn = list()
    for i in range (0, n):
        listn.append(random.randint(-5, 5))
    print(listn)
    x = int(input("Введите искомое число: "))
    for i in range(len(listn)):
        if listn[i] == x:
            count += 1
    print(count)
STask16()