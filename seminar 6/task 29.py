# Определить рекурсией простое число или нет
def Simple(number, divider):
    if divider == 1:
        return "yes"
    elif number % divider == 0:
        return "no"
    else:
        return Simple(number, divider - 1)

def task29():
    number = int(input("Please, enter the number: "))
    print(Simple(number, number // 2))
task29()