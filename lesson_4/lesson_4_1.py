""" Методы строк """
# s = "Mariia Alekseevna"
# s1 = s.upper()
# s2 = s.lower()
# print(s.upper()) # все большие буквы
# print(s.lower()) # все маленькие буквы
# print(s1)
# print(s2)
# Станачала пишется сама строка.метод()

# print(s.count("i")) # сколько букв "i" в имени
# print(s.count("i", 4)) # считает сколько с определенного индекса
# print(s.count("i", 0, 7)) # считает сколько от и до индекса
# print(s.find("a")) # с какого начинается индекс
# print(s.find("a", 4)) # указать с каого индекса начинать искать
# print(s.rfind("a")) # искать с другой стороны
# print(s.find("y")) # показывает что нет такой буквы
# print(s.index("y")) # можно использовать индекс, это тоже find только явно указывает ошибку
# print(s. replace("a", "o")) # замена символов подстроки
# print(s. replace("i", "e", 2)) # замена сомволов например только на 2 вхождения
# print(s. replace(" ", "")) # если хоти удалить лишнее

""" Проверка содержимого строки """
# print(s.isalpha()) # состоит из алфавита, но будет false, потому что есть пробел
# print(s.replace(" ", "").isalpha()) # убрали пробел
# print("MariiaAlekseevna".isalpha()) # тоже самое, убради пробел
# a = "34734"
# print(a.isdigit()) # строка состоит только из цифр
# a = "22"
# b = "374799"
# c = "345"
# print(a.rjust(8))# позволяет добавить символы справа до заданной длины
# print(b.rjust(8))
# print(c.rjust(8))
# print(a.rjust(8, "*")) # позволяет добавить символы слева до заданной длины
# print(b.rjust(8, "*"))
# print(c.rjust(8, "%"))
# print(a.ljust(8, "*")) # позволяет добавить символы справа до заданной длины
# print(b.ljust(8, "*"))
# print(c.ljust(8, "%"))

# s = "Коляко Мария Алексеевна" # разбить
# name, surname, second_name = s.split()
# s = "Коляко-Мария-Алексеевна"
# name, surname, second_name = s.split("-")
# print(name)
# print(surname)
# print(second_name)
# nums = "1, 2,3,  45,     8, 80"
# print(nums.replace(" ", '')) # убрать лишнии пробелы
# print(nums.replace(" ", '').split(",")) # сделать в ковычках
# words = ["str", "float", "bool"]
# print(', '.join(words)) # join объединяет

""" Удаление пробелов """
# a = '  Aaaaa aaa aaa'
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())