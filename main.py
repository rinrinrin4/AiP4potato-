Pass=input("Введите пароль: ")
Dpass=input("Подтвердите пароль: ")
if len(Pass) < 6:
    print("Ошибка, мало символов")

if Dpass == Pass :
    print("Пароль принят.")
else:
    print("Пароль не принят.")



    nv= int(input("Ввидите номер места: "))

    if nv % 2 == 0:
        print("Ваше место на верхней полке")
    else:
        print("Ваше место на нижней полке")

    if nv < 36 and nv < 55:
        print("Ваше место - боковое")
    else:
        print("места не существует")

    if int(nv) <= 0 :
            print("места не существует")




    year=int(input("Введите год: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год", year , "- високосный")
    else:
        print("Этот год не високосный")


cmy = ["красный", "синий", "желтый"]
color1= input("Введите первый цвет:")
color2= input("Введите второй цвет:")

if color1 not in cmy or color2 not in cmy:
    print("Введён неправильный цвет")
else:
    if (color1 == "красный" and color2 == "синий") or \
            (color1 == "синий" and color2 == "красный"):
        print("фиолетовый")

    elif (color1 == "синий" and color2 == "желтый") or \
            (color1 == "желтый" and color2 == "синий"):
        print("зеленый")

    elif (color1 == "красный" and color2 == "желтый") or \
            (color1 == "желтый" and color2 == "красный"):
        print("оранжевый")
    else:
        print("Цвета не смешиваются")




