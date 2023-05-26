# Пользователь вводит кол-во строк, затем сами строки. Нужно записать в новый текстовый файл все эти строки
# Далее пользователь вводит символ, нужно найти кол-во этого символа в новом файле.

num_strings = int(input("Введите количество строк: "))
string_list = []
print("Введите строки: ")
for string in range(num_strings):
    string_list.append(input(f'{string}:')+ '\n')
with open('article.txt', 'w', encoding='utf-8') as file:
    file.writelines(string_list)
user_sign = input("Введите символ: ")
with open('article.txt', 'r', encoding='utf-8') as file:
    find_sign = file.read()
    print(find_sign)
count = 0

for i in find_sign:
    if user_sign == i:
        count += 1
print (f"Количество символов '{user_sign}' равно: {count}")
