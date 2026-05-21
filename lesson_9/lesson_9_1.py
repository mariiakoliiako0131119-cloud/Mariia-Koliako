dict_ex = ["Даниил", "Николаев", "35", ["Москва", "Северодвинск", "Челябинск"]]

# Первый способ создать словари через фигурные скобки
# dict_ex = {"name": "Даниил", "last_name": "Николаев", "age": 35, "age": 37, "cities": ["Москва", "Северодвинск", "Челябинск"], "smoke": False}
# print(dict_ex['age'])

# Второй способ
# dict_ex = dict(name="Даниил", last_name="Николаев")
# print(dict_ex)

# Третий способ списки в списках
# dict_ex = [["name", "Даниил"], ["last_name", "Николаев"]]
# print(dict(dict_ex))

# dict_ex = dict() # создать пустой словарь

# Ключами могут быть
# str
# int
# bool
# tuple
# del dict_ex['name']# удалить ключ
# print(len(dict_ex)) # посмотреть длину словаря (считается кол-во ключей)

# print('name' in dict_ex) # есть ли ключ

# dict_ex = dict.fromkeys(("Даниил","Николаев", "35"))# создать словарь с помощью списка и создаться словарь со значениями пустыми
# dict_ex.clear() # очистить полностью словарь
# print(dict_ex)
# dict_ex_2 = dict_ex.copy() # скопировать словарь
# dict_ex_2 = dict(dict_ex) # другой способ скопировать словарь
# dict_ex_2['name'] = "Даня" # изменить значение
# dict_ex_2['jhk'] = 'jdflkjk' # добавить новый элемент
# print(dict_ex)
# print(id(dict_ex))
# print(id(dict_ex_2))
# print(dict_ex_2)

# получить значение по ключу
# name = dict_ex.get("name")
# if name:
#      print(name)

# name = dict_ex.get("wqfqwfw", "Дмитрий")
# if name:
#     print(name)

# другой метод получить значение по ключу
# dict_ex.setdefault('name', "Дмитрий")
# dict_ex.setdefault('олриыв', "Дмитрий") # если нужно добавть ключ
# print(dict_ex)

# удаляет ключ и возвращает значение

# print(dict_ex)
# str1 = dict_ex.pop('name')
# str2 = dict_ex.pop('рвапьи', "ключа нет") # если нет ключа, чтобы не было ошибки
# print(dict_ex)
# print(str1)
# print(str2)

# print(dict_ex)
# item = dict_ex.popitem() # удаляет последний элемент
# print(item)
# item = dict_ex.popitem()

# print(list(dict_ex.keys())) # получить все ключи
# print(list(dict_ex.values())) # получить все значения
# print(list(dict_ex.items())) # ключ - значение

# for key, value in dict_ex.items():
#     print(key, value)

# Объединить 2 словаря

# dict_ex1 = {"name": "Даниил"}
# dict_ex2 = {"last_name": "Николаев"}
# #
# dict_ex1.update(dict_ex2)
#
# print(dict_ex1)
# print(dict_ex2)
#
# # Если 2 словаря
# dict_res = {**dict_ex1, **dict_ex2}
# print(dict_res)