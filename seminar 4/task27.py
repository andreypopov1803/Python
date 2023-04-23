# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = input() + " "
count = 0
unical = set()
for i in range (len(text)):
    if text[i] == " ":
        if " " not in (text[count: i]):
            unical.add(text[count: i])
            count = i + 1
print(len(unical))

