""" Задание 1 """
cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Строка", "True", 3.14]

""" Задание 2 """
print(cities[0])
print(numbers[-1])
print(cities[10]) # такого индекса не существует

""" Задание 3 """
numbers[2] = 10
print(numbers)
mixed[3] = "Python"
print(mixed)

""" Задание 4 """
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

""" Задание 5 """
lst_1 =  [1, 2, 3]
lst_2 = [4, 5]
result = lst_1 + lst_2
print(result)
lst_3 = ["Python", "is", "awesome"] * 3
print(lst_3)

""" Задание 6 """
print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)

""" Задание 7 """
del numbers[3]
del cities[-1]
print(numbers)
print(cities)

""" Задание 8 """
lst_4 = list("Python")
print(lst_4)
print(max(lst_4))
print(min(lst_4))
print(sum(lst_4)) # можно складывать только int

""" Срезы списков - задание 1 """
cities_1 = ["Москва", "Ставрополь", "Сахалин", "Санкт-Петербург", "Владикавказ"]
cities_2 = cities_1[:]
print(id(cities_1))
print(id(cities_2))

""" Задание 2 """
print(cities_1[2:4])
print(cities_1[3:])
print(cities_1[:4])
print(cities_1[::3])
print(cities_1[-2:])

""" Задание 3 """
print(cities_1[::2])
print(cities_1[::-1])
print(cities_1[::-2])

""" Задание 4 """
cities_1[2:5] = ["Сочи", "Нижний Новгород"]
print(cities_1)
cities_1[1::2] = ["Город"] * len(cities_1[1::2])
print(cities_1)
cities_1[1:3] = ["Волгоград", "Омск"]
print(cities_1)

""" Задание 5 """
lst_5 = [1, 2, 3]
lst_6 = [4, 5, 6]
lst_7 = [10, 5, 3]
lst_9 = [1, 2, "abc"]
# result_1 = lst_5 + lst_6
# print(result_1)
lst_7 = ["Python", "rocks"]
lst_8 = lst_7[:]
print(id(lst_7))
print(id(lst_8))

""" Задание 6 """
print(lst_5 == lst_5)
print(lst_7 > lst_7)
print(lst_5 == lst_9)

""" Задание 7 """
chars = list("Python")
print(max(chars))
print(min(chars))
print(sum(chars)) # можно сложить только int

""" добавление элементов - задание 1 """
numbers_1 = [5, 10, 15]
numbers_1.append(20)
print(numbers_1)
numbers_1.insert(1, 7)
print(numbers_1)
numbers_1.append("Python")
print(numbers_1)

""" Задание 2 """
numbers_1.remove(10)
print(numbers_1)
last_el = numbers_1.pop()
print(last_el)
index_el = numbers_1.pop(1)
print(index_el)
numbers_1.clear()
print(numbers_1)

""" Задание 3 """
letters = ["a", "b", "c"]
letters_2 = list(letters)
letters_2 = letters.copy()
print(id(letters))
print(id(letters_2))

""" Задание 4 """
marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
print(marks.index(5))
print(marks.index(True, 6))

""" Задание 5 """
nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

""" Задание 6 """
cities_2 = ["Москва", "Ставрополь", "Сахалин", "Санкт-Петербург", "Владикавказ"]
cities_2.sort()
print(cities_2)
sorted_cities = sorted(cities_2)
print(sorted_cities)
print(cities_2)

""" Задание 7 """
chars = list("programming")
print(chars.count("g"))
chars.reverse()
print(chars)
chars.sort()
print(chars) # сортировка от меньшего с большему

""" Создание вложенного списка """

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11 ,12]
]
print(matrix)
print(matrix[1])
print(matrix[2][0])

""" Изменение элементов вложенного списка """
matrix[0] = [0, 0, 0]
print(matrix)

matrix[1][-1] = "Python"
print(matrix)
