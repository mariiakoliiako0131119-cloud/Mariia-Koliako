# class Dog:
#     """Класс для описания собаки"""
#     species = "canis"
#     legs = 4
#
# dog1 = Dog()
# dog2 = Dog()
#
# dog1.species = "canis"
# dog2.legs = 2
#
# print("Species:", dog1.species)
# print("Legs:", dog2.legs)
# print(Dog.__dict__)
#
# print(Dog.__dict__)
#
# dog1.name = "Bobik"
# dog2.age = 2
# print("Name:", dog1.name)
# print("Age:", dog2.age)
#
# del dog1.name
# print("Name:", getattr(dog1, 'name', "атрибута нет"))


# class User:
#     role = "guest"
#     active = True
#
# setattr(User, 'role', "admin")
# print(User.role)
#
# print(hasattr(User, "active"))
#
# setattr(User, "email", 'mariay@mail.ru')
# print(User.email)
#
# print(getattr(User, "role"))
# print(getattr(User, "email"))
#
# del User.role
# print(hasattr(User, "role"))
#
# print(User.__dict__)










