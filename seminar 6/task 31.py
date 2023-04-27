# Палиндром или нет рекурсией


txt = input("Please, enter the text: ")

def polindrom_check(txt):
    if len(txt) < 2:
        return True
    if txt[0] != txt[-1]:
        return False
    print(txt[1:-1])
    return polindrom_check(txt[1:-1])



print(polindrom_check(txt)) 