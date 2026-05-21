""" Срезы """
streets = ["Ломоносова", "Ленина", "Артюхиной", "Карла Маркса", "Доваторцев"]
# ages = [23, 54, 26]
# print(streets[2:4]) # 4-й индекс не считается
# print(streets[2:])
# streets_2 = streets # скопировать тот же объект
# streets_2 = streets[:]
# streets_2 = streets[:2]
# print(id(streets))
# print(id(streets_2))
# print((streets_2))
# streets_3 = list(streets) # скопировать тот же объект другой вариант
# print(streets)
# print(streets_3)
# print(id(streets))
# print(id(streets_3))

# присваивание списка не дает копию
# streets_3 = streets[:]
# streets[0] = 'Фотиевой'
# print(streets)
# print(streets_3)
# print(id(streets))
# print(id(streets_3))

""" срезы можно делать с шагами как и в строках """
# print(streets)
# print(streets[::2]) # хотим вывести каждый второй элемент
# print(streets[1::2])
# print(streets[:-1])

# print(streets[::-1])# развернуть строки

# streets[2:4] = [34, 65] # замена несколько элемнентов сразу
# print(streets)

# сравнивать списки между собой
# a = [1 , 2, 3]
# b = [1 , 2, 3]
# print(a == b)
# print(a != b)
# print(a > b)

# a = [1 , 2, '3']
# b = [1 , 2, 3]
# print(a > b) # нельзя сравнить что больше, а что меньше str и int
# print(a == b) # так можно


