#Задача №21. Решение в группах
#Напишите программу для печати всех уникальных
#значений в словаре.
#Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#{"VI": "S005"}, {"VII": " S005 "},
#{" V ":" S009 "}, {" VIII":" S007 "}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009

dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII " :" S007 "}]

x = set()
for i in dict_1:
    x.add(list(i.values())[0].strip())
print(x)