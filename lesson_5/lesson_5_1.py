""" Списки """
# streets = ["Ломоносова", "Ленина", "Артюхиной"]
# ages = [23, 54, 26]
"""
       0           1           2
["Ломоносова", "Ленина", "Артюхиной"]
     -3            -2          -1
"""
# print(streets[-2])
# print(streets[0])
# print(streets[-1])
# print(streets[3]) # такого индекса нет, будет ошибка

# avg_age = sum(ages) / len(ages) # вычисление среднего возраста и длина строки
# print(avg_age)
# avg_age = int(sum(ages) / len(ages)) # если хотим получить целое число
# print(avg_age)

""" Список это изменяемый тип данных """
# ages[1] = 31 # можно изменить цифру
# print(ages)
# lst = ['Волгоград', 332, 21.344, True, False, [2, 3, 4, 'вапрвл']] # в списках можно хранить любые значения
# lst = [] # как создать пустой список
# lst2 = list() # 2-й вариант
# lst3 = list('Волгоград') # из строки создать отдельный список
# print(lst3)

""" Основные функции"""
# print(len(lst3))
# print(max(ages))
# print(min(ages))
# print(sum(ages))
# print(sum(ages)) # суммирует только int
# print(sorted(lst3)) # меняет текущий список по алфавиту
# print(sorted(ages))
# print(sorted(ages, reverse=True)) # наоборот

""" Объединение 2-х списков """
# streets = ["Ломоносова", "Ленина", "Артюхиной"]
# ages = [23, 54, 26]
# result = streets + ages
# print(result )

# print(result  + ['A'])# можно складывать только список со списком
# print(result  * 2) # дублирование списков
# print('Ломоносова' in result) # содержится  в списке
# print('носова' in result) # содержится списки в списке
# print(54 in result) содержится в...
# result.append('12334') # добавлять элемент
# print(result)
# result.append([2, 5]) # добавить список
# print(result)
# print([2, 5] in result) # найти вхождение в целом списке
# del result[-1]# удаление
# del result[1]
# del result[1]
# print(result)
