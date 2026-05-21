# class Person:
#     name = ('Maria')
#     age = 17
#
#     def set_data(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_data(self):
#         return f"Имя: {self.name}, Возраст: {self.age}"
#
# person1 = Person()
# person2 = Person()
#
# person1.set_data("Maria", 37)
# person2.set_data("Katya", 33)
#
# print(person1.get_data())
# print(person2.get_data())
from typing import reveal_type


# class Point:
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return f'x: {self.x} y: {self.y}'
#
# p = Point()
# p.set_coords(7, 12)
# print(p.get_coords())
#
# p.set_coords(-3, 5)
# print(p.get_coords())
#
# method = getattr(p, 'get_coords')
# print(method())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         return f"Имя: {self.name}, возраст: {self.age}"
#
#     def __del__(self):
#         print(f'Удален объект: {self.name}')
#
# p = Person("Anna", 36)
# print(p.show_info())
#
# del p


# class Rectangle:
#     def __init__(self, width=1, height=1):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# # без аргумента
# r1 = Rectangle()
# print(r1.area())
#
# # с аргументами
# r2 = Rectangle(5, 10)
# print(r2.area())


# 7. Создай класс Logger, который всегда возвращает один и тот же объект.
# При создании экземпляра в __new__ выводи Создание логгера,
# а при вызове __init__ — Инициализация логгера.

# class Loger:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             print ("Создание логгера")
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         print("Инициализация логгера")
#
# l1 = Loger()
# l2 = Loger()
#
# print(id(l1))
# print(id(l2))
# print(l1 is l2)


# __new__ → создаёт объект
# _instance → настраивает/хранит объект
# return → отдаёт блокнот
# is → проверяет, тот же самый или нет

# __new__ — создаёт объект
# __init__ — настраивает объект

# cls — это сам класс.
#
# То есть в нашем случае cls — это Logger.
#
# Можно думать так:
#
# self — это объект
# cls — это класс


# *args — дополнительные обычные аргументы
# **kwargs — дополнительные именованные аргументы

# if cls._instance is None:
# Это проверка: Создан уже объект или ещё нет?
# Если перевести на обычный язык: если в _instance ничего нет значит, объект ещё не создавали значит, надо создать


# class GameSettings:
#     _instance = None
#     volume = 50
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             print("Создание настроек")
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         print("Инициализация настроек")
#
# s1 = GameSettings()
# s2 = GameSettings()
#
# s1.volume = 10
# print(s2.volume)
# print(s1 is s2)
