# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print("Введите общее количество сделанных журавликов: ")


s = int (input())

if (s % 4) == 0:
    a = s/4
    b = s/4
    c = s/2
    print(a)
    print(b)
    print(c)
else:
    print("Введите корректное число: ")



