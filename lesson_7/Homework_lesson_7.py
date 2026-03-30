""" Задание 1 """
from io import text_encoding
from xxsubtype import bench

# n = int(input('Введите число N: '))
# i = 1
# while i <= n:
#     print(i)
#     i += 1

""" Задание 2 """
# n = int(input('Введите число N: '))
# i = 1
# s = 0
# while i <= n:
#     if i % 2 == 0:
#         s += i
#     i += 1
# print(s)

""" Задание 3 """
# n = int(input('Введите число: '))
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1
# print(count)

""" Задание 4 """




# Задание 5 """
# correct_password = "qwerty123"
# input_password = input("Введите пароль: ")
#
# while input_password != correct_password:
#     print("Пароль введен не верно! ")
#     input_password = input("Введите пароль: ")
# print("Доступ разреш")

""" Задание 1 """

# numbers = [23, 40, 75, 80, 51, 62]
# result = []
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print("Первое четное число:",numbers[i])
#         break
#     i += 1
# else:
#     print("Четное число не найдено")

""" Задание 2 """
# num = 1
# rest_sum = 0
# while num != 0:
#     num = int(input("Введите целое число или 0 для выхода: "))
#     if num % 2 == 0:
#         continue
#     rest_sum += num
# print(rest_sum)

""" Задание 3 """
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# i = a
# while i <= b:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

""" Задание 4 """
# n = int(input('Введите число N: '))
# i = 2
# while i < n:
#     if n % i == 0:
#         print("Число не простое")
#         break
#     i += 1
# else:
#     print("Число простое")

""" Задание 5 """


""" Задание 1 """

# text = input("Введите строку: ")
#
# chars = list(text)
# chars.reverse()
#
# for ch in chars:
#     print(ch, end="")

""" Задание 2 """
# numbers = [23, 43, 75, 33, 80, 51, 62]
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = 0
# print(numbers)

""" Задание 3 """
# n = int(input("Введите число N: "))
# num = []
# for i in range(n + 1):
#     num.append(2 ** 1)
# print(num)

""" Задание 4 """
# a = int(input("Введите A: "))
# b = int(input("Введите B: "))
# k = int(input("Введите K: "))
# for i in range(a,b + 1, k):
#     print(i)


