# Задача 2: Найдите сумму цифр трехзначного числа.

print("Введите число: ")
a = int(input())

s = round(a%10) + round((a/10)%10) + round((a/100)%10)

print(s)