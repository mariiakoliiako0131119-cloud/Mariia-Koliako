# 1. Создай класс LengthValidator, который:
# принимает в __init__ минимальную и максимальную длину строки;
# в __call__ проверяет, что длина переданной строки в заданном диапазоне;
# выбрасывает ValueError, если условие не выполнено.
# Пример:
# validator = LengthValidator(3, 10)
# print(validator("python"))  # True
# print(validator("hi"))      # ValueError

# class LengthValidator:
#     def __init__(self, min_length: int, max_length: int):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, value): # позволяет вызывать объект как функцию
#         if not isinstance(value, str):
#             raise ValueError("Не строка")
#
#         length = len(value)
#         if self.min_length <= length <= self.max_length:
#             return True
#         raise ValueError(f"длина строки должна быть от {self.min_length} до {self.max_length}")
#
# validator = LengthValidator(3, 10)
# print(validator("python"))
# print(validator("hi"))


# 2. Создай класс Sumator, который:
# при первом вызове принимает число;
# каждый следующий вызов увеличивает сумму;
# хранит и возвращает текущую сумму.

# class Sumator:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, value):
#         self.count += value
#         return self.count
#
# s = Sumator()
# print(s(5))   # 5
# print(s(10))  # 15
# print(s(-2))  # 13

# 3. Создай класс HasText, который:
# в __init__ принимает ожидаемую подстроку;
# в __call__ принимает текст и возвращает True, если подстрока найдена.
# Подумай как сделать так, чтобы работало как и в примере?
# Пример:
# assert HasText("Success")("Test passed: Success")  # True
# assert HasText("Error")("All OK")  # False

# class HasText:
#     def __init__(self, text: str):
#         self.text = text
#     def __call__(self, status):
#        return self.text in status
#
# h = HasText("Success")
# assert HasText("Success")("Test passed: Success")
# assert HasText("Error")("All OK") == False

# Создай класс Book, который хранит:
# название книги (title)
# автора (author)
# Переопредели __str__ и __repr__, чтобы:
# print(book) выводил "Автор — Название"
# repr(book) показывал <Book 'Название' by Автор>

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return f'{self.author} - {self.title}'
#
#     def __repr__(self):
#         return f"<Book '{self.title}' by {self.author}>"
#
# book = Book("1984", "Джордж Оруэлл")
# print(book)         # Джордж Оруэлл — 1984
# print(repr(book))   # <Book '1984' by Джордж Оруэлл>


# 5. Создай класс TestUser, который содержит id, name, email.
# Переопредели __repr__, чтобы его было удобно видеть в логах автотеста:
# user = TestUser(12, "Daniil", "daniil@example.com")
# print(user)
# <TestUser id=12 name='Daniil' email='daniil@example.com'>

# class TestUser:
#     def __init__(self, test_id, name, email):
#         self.test_id = test_id
#         self.name = name
#         self.email = email
#     def __repr__(self):
#         return f"<TestUser id={self.test_id} name='{self.name}' email='{self.email}'"
#
# user = TestUser(12, "Daniil", "daniil@example.com")
# print(user)