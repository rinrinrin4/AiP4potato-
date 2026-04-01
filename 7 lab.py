lacky_list=[1,5,8,4]
ask=int(input("Попробуйте угадать число"))
if ask in lacky_list:
    print("Поздравляю, Вы угадали число! Ваше число: ", ask, "есть в списке:", lacky_list)
else:
    print("Нет такого числа! Вашего числа: ", ask, "нет в списке:", lacky_list)


##
from collections import Counter

list=["огурец", "огурец", "капуста", "морковка", "томат", "папайа", "томат",]

Counter = Counter(list)
duplicates=[(word, count) for word, count in Counter.items() if count>1]
print(f"Список слов: {list}")
if duplicates:
     print(f"\n Найдены повторяющиеся слова: {[w for w, _ in duplicates]}")
else:
    print("Повторяющихся слов нет!")

##