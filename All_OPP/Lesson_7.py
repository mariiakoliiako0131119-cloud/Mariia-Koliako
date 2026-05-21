# 1. Создай три класса: Cat, Dog, Duck.
# В каждом реализуй метод speak(), возвращающий уникальную строку.
# Создай список из экземпляров этих классов и вызови метод speak()
# в цикле.
from idlelib.debugger_r import close_subprocess_debugger
from shlex import split
from unittest import expectedFailure

# class Cat:
#     def speak(self):
#         return "Мяу!"
#
# class Dog:
#     def speak(self):
#         return "Гаф!"
#
# class Duck:
#     def speak(self):
#         return "Кря!"
#
# animals = [Cat(), Dog(), Duck()]
#
# for animal in animals:
#     print(animal.speak())


# 2. Создай базовый класс Shape
# Создай три класса-наследника: Square, Rectangle, Triangle,
# в каждом реализуй метод get_pr().
# Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
# можно обойти в цикле и вызвать get_pr() у каждого.

# class Shape:
#     def get_pr(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side= side
#
#     def get_pr(self):
#         return self.side * 4
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_pr(self):
#         return (self.width + self.height) * 2
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return self.a + self.b + self.c
#
# shapes = [Square(5), Rectangle(4, 6), Triangle(3, 4, 5)]
#
# for shape in shapes:
#     print(shape.get_pr())

# 3. Сделай класс Shape абстрактным.
# Переопредели get_pr() как @abstractmethod.
# Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def get_pr(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side= side
#
#     def get_pr(self):
#         return self.side * 4
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_pr(self):
#         return (self.width + self.height) * 2
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return self.a + self.b + self.c

# shapes = [Square(5), Rectangle(4, 6), Triangle(3, 4, 5)]
#
# for shape in shapes:
#     print(shape.get_pr())
# s = Shape()
# print(dir())
# try:
#     s = Shape()
# except TypeError as e:
#     print(f"Ошибка {e}")


# 4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.

# class A():
#     def __init__(self):
#         print("init A")
#         super().__init__()
#
# class B():
#     def __init__(self):
#         print("init B")
#         super().__init__()
#
# class C():
#     def __init__(self):
#         print("init C")
#         super().__init__()
#
# class D(A, B, C):
#     def __init__(self):
#         print("init D")
#         super().__init__()

# print(D.__mro__)
# print("---")
# d = D()

# 7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
# Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
# и выведи сообщение: "На ноль делить нельзя!"

# try:
#     a = float(input("Введите первое число: "))
#     b = float(input("Введите второе число: "))
#     print(f"Результат {a / b}")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# 8. Расширь программу из Задания 1:
# Добавь обработку ошибки (как называется ошибка найди сам),
# если пользователь ввёл не числа, а текст.
# Выведи сообщение: "Ошибка ввода: введите два числа через пробел"

# try:
#     a = float(input("Введите первое число: "))
#     b = float(input("Введите второе число: "))
#     print(f"Результат {a / b}")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# except ValueError:
#     print("Ошибка: введите число, а текст!")
# else:
#     try:
#         a, b = map(int,input("Введите два числа через пробел: ").split())
#         print(f"Результат {a + b}")
#     except ValueError:
#         print("Ошибка ввода: введите два числа через пробел")

