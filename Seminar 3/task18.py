# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5
import math
import random

def STask18():
    n = int(input("Введите количество элементов в массиве: "))
    print(n)
    listn = list()
    for i in range (0, n):
        listn.append(random.randint(0, 10))
    print(listn)
    x = int(input("Введите число: "))
    listm = list()
    for i in range(len(listn)):
        listn[i] = math.sqrt((listn[i]-x)*(listn[i]-x))
    for i in range(len(listn)):
        min = listn[i]
        if listn[i] < min:
            min = listn[i]
    # print(min)
    for i in range(len(listn)):
        if listn[i] == min:
            print("Ближайшее число к заданному: ", listn[i], " c индексом", i)
STask18()