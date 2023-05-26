# with open('example.txt', 'r', encoding='utf-8') as file:
# text = file.read()
# for letter in text:
# print(letter)


# with open('example.txt', 'r', encoding='utf-8') as file:
# while True:
# line = file.readline()
# if not line:
# break
# print(line[:-1])

# with open('example.txt', 'r', encoding='utf-8') as file:
# line = file.readline()
# while line:
# print(line[:-1])
# line = file.readline()


# with open('example.txt', 'r', encoding='utf-8') as file:
# text = file.read()
# print(text.splitlines())

# with open('example.txt', 'r', encoding='utf-8') as file:
# text = file.readlines()
# print(text)

# fp = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# search_string = 'Анна'
# with open("directory.txt") as f:
#     n = 0
#     for line in f:
#         n += 1
#         if search_string in line:
#             print(search_string, 'found on line', n)
# Путь к текстовому файлу - замените на путь, по которому расположен файл на Вашем компьютере


def find_string_numbers(path_to_file, required_text):
    string_numbers = []
    with open(path_to_file, encoding='utf-8') as file:
        text = file.read()
        print(text)
        for num_line, line in enumerate(text):
            if required_text in line:
                print(num_line)
                string_numbers.append(num_line)
        if(len(string_numbers) > 0):
            return(string_numbers)
        else:
            return("Ни одной строки с заданным содержанием не нашлось.")
    
string_numbers = find_string_numbers("directory.txt", 'n')
print(string_numbers)


search_string = 'mytext'
with open("myfile.txt") as f:
  n = 0
  for line in f:
    n += 1
    if search_string in line:
      print(search_string, 'found on line', n)