def delenie_na_3(chislo):
    if chislo % 3 == 0:
        return True
    else:
        return False

a = int(input("Введите число: "))
if delenie_na_3(a):
    print("Число делится на 3")
else:
    print("Число не делится на 3")
##



##
def delenie(chislo):
    return 100 / chislo

try:
    b = float(input("Введите число: "))
    rezultat = delenie(b)
    print("Результат:", rezultat)
except ValueError:
    print("Ошибка! Нужно ввести число")
except ZeroDivisionError:
    print("Ошибка! На ноль делить нельзя")

##
def magic_date(data):
    den = int(data[0:2])
    mes = int(data[3:5])
    god = int(data[6:10])
    poslednie_dve = god % 100

    if den * mes == poslednie_dve:
        return True
    else:
        return False


d = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if magic_date(d):
    print("Дата магическая!")
else:
    print("Дата не магическая")

##
def schastliviy_bilet(nomer):
    dlinna = len(nomer)
    polovina = dlinna // 2

    summa1 = 0
    for i in range(polovina):
        summa1 = summa1 + int(nomer[i])

    summa2 = 0
    for i in range(polovina, dlinna):
        summa2 = summa2 + int(nomer[i])

    if summa1 == summa2:
        return True
    else:
        return False


n = input("Введите номер билета: ")
if schastliviy_bilet(n):
    print("Счастливый билет!")
else:
    print("Несчастливый билет")