

#N=int(input("Ввeдите количество слов: "))
#result = ""
#i=0
#while i < N:
 #   word = input(f"Введите слово {i + 1}: ")
  #  i += 1
   # result += word  # Добавляем слово
    #if i < N :  # Добавляем пробел, если это не последнее слово
     #   result += " "

#print("Результат:", result)


    #i=0
#result = ""
#while True:
    #word = input(f"Введите слово {i + 1}: ")
    #if word.lower() == "stop":  # .lower() для обработки в любом регистре
    #    break
    #i += 1
    #result += word  # Добавляем слово
    #result += " "


#print("Результат:", result)

#n=0
#slowo = input("Введите слово для подсчета его редкости: ").lower()
#for i in slowo:
 #   if i == "ф":
  #      n+=1


#if n >0:
  # print("Ого! Это редкое слово!")
#else:
 #  print("Эх, это не очень редкое слово...")


go=0
points=0
while go<3:
    import random

    ch1 = int(random.uniform(0, 100))
    ch2 = int(random.uniform(0, 100))

    print( f"{ch1}+{ch2}=", end="")
    o= int(input())
    potw = ch1+ch2

    if o==potw:
        points += 1
        print("Правильно!")
    else:
        go+=1
        print("Ответ неверный")

print("Игра окончена. Правильных ответов: ", points)











