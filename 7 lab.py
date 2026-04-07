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
days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', )

weekends_count = int(input("Сколько выходных на неделе вы хотите? "))

# Проверка
if 1 <= weekends_count <= 7:
    # Выходные дни - последние N дней из кортежа
    weekends = list(days_of_week[-weekends_count:])
    
    # Рабочие дни - остальные дни
    workdays = list(days_of_week[:-weekends_count])
    
    print(f"Ваши выходные дни: {', '.join(weekends)}")
    print(f"Ваши рабочие дни: {', '.join(workdays)}")
else:
    print("Пожалуйста, введите число от 1 до 7")

# 
group1 = ['Иванов', 'Петров', 'Сидоров', 'Козлов', 'Соколов', 'Михайлов', 'Федоров', 'Николаев', 'Алексеев', 'Дмитриев']
group2 = ['Волков', 'Зайцев', 'Морозов', 'Кузнецов', 'Новиков', 'Васильев', 'Павлов', 'Сергеев', 'Андреев', 'Тарасов']
team = tuple(group1[:5] + group2[:5])

#  исходные списки 
print("Первая группа:", group1)
print("Вторая группа:", group2)
print("Спортивная команда:", team)
print(f"Длина кортежа: {len(team)}")

sorted_team = tuple(sorted(team))
print("Отсортированная команда:", sorted_team)

count_ivanov = team.count('Иванов')
if count_ivanov > 0:
    print(f"Студент 'Иванов' входит в команду. Встречается {count_ivanov} раз(а).")
else:
    print("Студент 'Иванов' не входит в команду.")
