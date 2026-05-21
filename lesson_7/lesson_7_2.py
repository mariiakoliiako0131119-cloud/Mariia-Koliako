""" Цикл for используется для перебора коллекций """
# numbers = [23, 43, 75, 33, 80, 51, 62]
# for numbers in numbers:
#     print("Печатаем", numbers)

# for letter in "Мария":
#     print("Буква:", letter)

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for number in numbers:
#     number = 0
# print(numbers)

""" range(start, stop, step) генерация последовательносте"""
# print(range(10))
# print(list(range(10)))
# print(list(range(0, 10, 2))) # прибавить шаг

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for i in range(len(numbers)): # i - обычно указывается индекс
#     numbers[i] = 0
# print(numbers)

# words = ["Привет,", "Мария!", "Как дела?"]
# result_str = ""
# for word in words:
#     result_str += " " + word
# print(result_str.lstrip()) # убрать пробел впереди

# found = None
# for i in "Урок":
#     if i == "л":
#         found = True
#         break
# else:
#     found = False
#
# print(found)
