""" Задание 1 """

# s = "Python для автоматизации"
# print(s.upper())
# print(s.lower())

""" Задание 2 """
# msg = "абракадабра"
# print(msg.count("ра"))
# print(msg.count("а", 3))

""" Задание 3 """
# msg = "абракадабра"
# print(msg.find("ка"))
# print(msg.find("а", -1))
# print(msg.find("xyz",))

""" Задание 4 """
# text = "Я изучаю Java"
# print(text.replace("Java", "Python"))
# print(text.replace(" ", ""))

""" Задание 5 """
# text1 = "Python"
# print(text1. isalpha())
# a = "12345"
# print(a.isdigit())
# text2 = "123abc"
# print(not text2.isdigit())

""" Задание 6 """
# code = "42"
# print(code.rjust(5, "0"))
# a = "text"
# print(a.ljust(10, "*"))

""" Задание 7 """
# s = "яблоко, груша, банан"
# apple, grusha, banan = s.split()
# print(apple)
# print(grusha)
# print(banan)
# s1= "Python;Java;C++" по ";" # НЕ ПОНИМАЮ ЗАДАНИЯ
# Python, Java, C++ to = s1.split()

""" Задание 8 """
# text3 = ["Привет", "мир", "!"]
# print(' '.join(text3))
# text4 =  ["apple", "banana", "cherry"]
# print(", ".join(text4))

""" Задание 9 """
# text4 = " Python"
# print(text4.lstrip())
# # text5 = "Python "
# # print(text5.rstrip())
# text6 = " Python "
# print(text6.strip())

""" Задание 10 """
# text = "программирование"
# print(text[:0] + "П" + text[1:])

""" Перевод строки задание 1 """
# text = "Hello\nPython"
# print(text) # потому \n перенес слово

""" Задание 2 """
# t = "Python\tAutomation"
# print(t) # добавил длинный пробел

""" Задание 3 """
# path = "C:\new\test.txt"
# print(path) # перенес слова на новую строку и добавил длинный пробел
# s = "Марка вина \"Ягодка\""
# print(s)

""" Задание 4 """
# path = r"C:\new\test.txt"
# print(path) # к простой добавляем 2 \\, а у сырой доб. r и один \

""" Задание 5 """

# s = "Hello\b World"
# print(s) # нет буквы о
# s = "Hello\fPython"
# print(s)

""" Форматирование задание 1 """
# name = "Мария"
# age = 37
# text = "Мое имя " + name +", мой возраст " + str(age) + " лет"
# text = "Мое имя " + name +", мой возраст " + str(age) + 10
# print(text) # ошибка

""" Задание 2 """
# name = "Мария"
# age = 37
# # text1 = "Привет, меня зовут {0}, мне {1} лет".format(name, age)
# # print(text1)
# text3 = "Привет, меня зовут {имя}, мне {возраст} лет".format(имя=name, возраст=age)
# print(text3)
# text4 = "Привет, меня зовут {имя}, мне {возраст} лет".format(имя=age, возраст=name)
# print(text4)

""" Задание 3 """
# city = "Москва"
# year = 2026
# # text = f"Сегодня {year} год, и я живу в {city}"
# # print(text)
# year1 = 5
# text2 = f"Через {year1} лет будет {year + 5} год"
# print(text2)

""" Задание 4 """
# age = 37
# text3 = f"Дважды мой возраст {age + age}"
# print(text3)
# print(name.upper())

""" Задание 5 """
# dollar = 1
# rub = 92.5
# currency = "Курс валют: {0} доллар = {1} рубля".format(dollar, rub)
# print(currency)

# square = 7
# text = f"Квадрат числа {7} равен {7 ** 2}."
# print(text)