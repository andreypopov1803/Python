# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество и номер телефона - 
# данные, которые должны находиться в файле.
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(например имя или фамилию человека)
# 4. Использование функций (ваша программа не должна быть линейной)

def imp(file):
    num_strings = int(input("Введите количество человек, вносимых в базу: "))
    string_list = []
    print("Введите данные: ")
    for string in range(num_strings):
        string_list.append(input(f'{string}: ')+ '\n')
    with open('directory.txt', 'a', encoding='utf-8') as file:
        file.writelines(string_list)
imp('directory.txt')

def exp(file):
    with open('directory.txt', 'r', encoding='utf-8') as file:
        file_text = file.read().split('\n')
    for i in range(len(file_text)):
        print(file_text[i])
exp ('directory.txt')

def search_number_of_string(file):
    with open(file, 'r', encoding='utf-8') as file:
        name = input('Введите имя искомого человека: ')
        for num, line in enumerate(file, 2):
            if name in line:
                print ('Данные искомого человека: ',line)
search_number_of_string('directory.txt')