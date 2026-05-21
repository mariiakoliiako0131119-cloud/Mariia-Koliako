# 1. Создай класс SecureData, который:
#
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"

# class SecureData:
#     def __init__(self, secret):
#         self.__secret = secret
#
#     def __getattribute__(self, name):
#         if name == "_SecureData__secret":
#             raise ValueError("Доступ запрещен")
#         return object.__getattribute__(self, name)
#
#     def get_secret(self):
#         return object.__getattribute__(self, "_SecureData__secret")
#
#
# data = SecureData("пароль123")
# try:
#     print(data._SecureData__secret)
# except ValueError:
#     print("Доступ запрещен")
# print(data.get_secret())

# 2. Добавь в класс SecureData метод __setattr__,
# который запрещает создание любого атрибута с именем token.
#
# Проверь:
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает

# class SecureData:
#     def __init__(self, secret):
#         self.__secret = secret
#
#     def __getattribute__(self, name):
#         if name == "_SecureData__secret":
#             raise ValueError("Доступ запрещен")
#         return object.__getattribute__(self, name)
#
#     def get_secret(self):
#         return object.__getattribute__(self, "_SecureData__secret")
#
#     def __setattr__(self, key, value):
#         if key == 'token':
#             raise ValueError("Создание атрибута запрещено")
#         return object.__setattr__(self, key, value)
#
# data = SecureData("пароль123")
# data.token = "abc123"
# data.other = "ok"
# print(data.__dict__)


# Создай класс SafeDict, в котором:
#
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key

# class SafeDict:
#
#     def __getattr__(self, name):
#         return "N/A"
#
#     def __delattr__(self, key):
#         print(f"Удалён атрибут: {key}")
#         return object.__delattr__(self, key)
#
# d = SafeDict()
# print(d.unknown)
# d.key = 10
# del d.key

# Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
#
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if value <= 0:
#             raise ValueError("Зарплата не является положительной")
#         self.__salary = value
#
# e = Employee("Daniil", 5000)
# print(e.salary)
# e.salary = 8000
# print(e.salary)
# e.salary = -100


# Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
# и поле реально исчезало.
# Проверь:

# del e.salary
# print(e.__dict__)  # salary нет

# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     @property # @property → “посмотреть значение” это как getter. делает метод похожим на переменную
#     def salary(self):
#         return self.__salary
#
#     @salary.setter # @setter → “изменить значение” добавляет проверку при изменении
#     def salary(self, value):
#         if value <= 0:
#             raise ValueError("Зарплата не является положительной")
#         self.__salary = value
#
#     @salary.deleter # @deleter → “удалить значение” управляет удалением
#     def salary(self):
#         print("Зарплата удалена")
#         del self.__salary
#
# e = Employee("Daniil", 5000)
# print(e.salary)
# e.salary = 8000
# print(e.salary)
#
# # e.salary = -100
#
# del e.salary
# print(e.__dict__)


# Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
#
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"

# class LoginForm:
#     def __init__(self):
#         self._username = None
#
#     @property
#     def username(self):
#         return self._username
#
#     @username.setter
#     def username(self, value):
#         print("username изменён")
#         self._username = value
#
# form = LoginForm()
# form.username = "admin2"
# print(form.username)

# Создай класс Card, где:
# поле __number хранит номер карты (строка);
# в @property возвращай номер с маской **** **** **** 1234;
# в @setter проверяй, что номер состоит из 16 цифр;
# в @deleter логируй удаление номера с текущим временем.
# Напиши тесты (через assert)
# проверку установки корректного номера;
# проверку исключения при вводе короткого номера;
# проверку вывода замаскированного номера.

# from datetime import datetime
#
# class Card:
#     def __init__(self, number: str):
#         self.number = number
#
#     @property
#     def number(self):
#         return "**** **** **** " + self.__number[-4:]
#
#     @number.setter
#     def number(self, value):
#         if len(value) != 16 or not value.isdigit(): # isdigit - состоит ли строка только из цифр
#             raise ValueError ("Номер карты должен состоять из 16 цифр")
#         self.__number = value
#
#     @number.deleter
#     def number(self):
#         print(f"LOG"
#               f"{datetime.now().strftime('%Y.%m.%d.%H.%M.%S.%m')} Номер удален")
#         del self.__number
#
# c = Card("1234567812345678")
# #
# # проверка установки корректного номера
# # assert c.number == "**** **** **** 5678", "Номер верный"
# #
# # проверка исключения при вводе короткого номера
# c.number = "1234567"
# assert c.number == "1234567"

# проверка вывода замаскированного номера
# c.number = "1111222233334444"
# assert c.number == "**** **** **** 4444"

# 8. Создай класс UserData для API регистрации пользователя:
# email — строка, содержит @;
# age — целое число ≥ 18;
# is_active — bool;
# свойство .json возвращает словарь для запроса.
# Напиши тест (через assert)
# проверь, что при age = 15 выбрасывается ValueError;
# проверь, что email без @ вызывает ошибку;
# проверь, что json возвращает корректную структуру.

# class UserData:
#     def __init__(self,
#                  email: str,
#                  age: int,
#                  is_active: bool
#     ):
#         self.email = email # — запускает логику
#         self.age = age
#         self.is_active = is_active
#
#     @property
#     def email(self):
#         return self.__email
#
#     @email.setter
#     def email(self, value):
#         if "@" not in value:
#             raise ValueError("Некорректный email")
#         self.__email = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if not value >= 18:
#             raise ValueError("Возраст не подходит")
#         self.__age = value
#
#     @property
#     def is_active(self):
#         return self.__is_active
#
#     @is_active.setter
#     def is_active(self, value):
#         if not isinstance(value, bool):
#             raise ValueError("is_active должен быть bool")
#         self.__is_active = value # это инкапсуляция — хранит данные
#
#     @property
#     def json(self):
#         return {
#             "email": self.email,
#             "age": self.age,
#             "is_active": self.is_active
#         }
#
# user = UserData("test@mail.com", 19, True)
#
# assert user.email == "test@mail.com"
#
# assert user.age == 19
# assert user.json == {
#     "email": "test@mail.com",
#     "age": 19,
#     "is_active": True
# }
#
# # ❌ возраст < 18
# # try:
# #     UserData("test@mail.com", 15, True)
# #     assert False
# # except ValueError:
# #     pass
# #
# # ❌ email без @
# try:
#     UserData("test.mail.com", 20, True)
#     assert False
# except ValueError:
#     pass




