""" Задание 1 """

x = int(input("Введите число: "))
if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

""" Задание 2 """

x = int(input("Введите целое число: "))
if x % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

""" Задание 3 """

x_1 = int(input("Введите целое число: "))
x = [1, 10]
if x_1 in x:
    print("Число в диапазоне")
else:
    print("Число вне диапазона")

""" Задание 4 """

a = int(input("Введите число: "))
b = int(input("Введите число: "))
if a < b:
    a, b = b, a
print(("Числа в порядке убывания:", a, b))

""" Задание 5 """

a = int(input("Введите число: "))
b = int(input("Введите число: "))
if a < b:
    print("Число меньше: a")
else:
    print("Число меньше: b")

""" Задание 6 """

marks = [3, 4, 5, 2, 5, 4]
mark = int(input("Введите оценку для проверки: "))
if mark == 2:
    print("Есть неудовлетворительная оценка")
else:
    print("Все оценки положительные")

""" Задание 7 """

x = int(input("Введите число: "))
if x % 3 == 0 and x % 5 == 0:
    print("Число делится на 3 и 5")
elif x % 3 == 0:
    print("Число делится только на 3")
elif x % 5 == 0:
    print("Число делится только на 5")
else:
    print("Число не делится на 3 и 5")

""" Задание 8 """

x = input("Введите пароль: ")
if x == "admin123":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

""" Задание 9 """

amount = int(input("Введите сумму покупки: "))
if amount >= 5000:
    print("Скидка 10%")
    discount = 0.10
elif amount >= 1000:
    print("Скидка 5%")
    discount = 0.05
else:
    print("Скидки нет")
    discount = 0
final_amount = amount * (1 - discount)
print("Итоговая сумма после скидки:", final_amount)

""" Задание 10 """

year = int(input("Укажи год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

""" Проверка оценки Задание 1 """

"""
grade - оценка 5
grade - оценка 4
grade - оценка 3
grade - оценка 2
grade - оценка 1
"""
grade = int(input("Напиши оценку (1-5): "))
if grade == 5:
    print("Отлично")
elif grade == 4:
    print("Хорошо")
elif grade == 3:
    print("Удовлетворительно")
elif grade == 1 or grade == 2:
    print("Неудовлетворительно")
else:
    print("Некорректная оценка")

""" Задание 2 """
"""
hour - c 6 до 11
hour- с 12 до 17
hour - с 18 до 21
hour - с 22 до 5
"""
hour = int(input("Напиши текущее время (0-23): "))
if 6 <= hour <= 11:
    print("Утро")
elif 12 <= hour <= 17:
    print("День")
elif 18 <= hour <= 21:
    print("Вечер")
elif 22 <= hour <= 5:
    print("Ночь")
else:
    print("Некорректное время")

""" Задание 3 """
"""
temp - -10
temp- от -10 до 0
temp - от 1 до 10
temp - выше 25
"""
temp = int(input("Напиши температуру: "))
if temp <= -10:
    print("Очень холодно")
elif -10 <= temp <= 0:
    print("Холодно")
elif 1 <= temp <= 10:
    print("Прохладно")
elif 11 <= temp <= 25:
    print("Тепло")
else:
    if temp > 25:
        print("Жарко")

""" Задание 4 """

year = int(input("Укажи год: "))
if (year % 4 == 0 and year % 100 != 00) or (year % 400 == 0):
        print("Год високосный")
else:
        print("Год не високосный")

""" Задание 5 """

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    print("Результат", a + b)
elif operation == "-":
    print("Результат", a - b)
elif operation == "*":
    print("Результат", a * b)
elif operation == "/":
    if b != 0:
        print("Результат", a / b)
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Некорректная операция")

""" Проверка четности числа """

number = int(input("Введите число: "))
res = "Число четное" if number % 2 == 0 else "Число нечетное"
print(res)

""" Определение наибольшего числа """
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

max_number = a if a > b else b
print("Максимальное число", max_number)

""" Проверка положительного или отрицательного числа """

a = int(input("Введите первое число: "))
result = "Положительное" if a > 0 else "Отрицательно" if a < 0 else 0
print(result)

""" Определение возраста для входа в клуб """

age = int(input("Введите свой возраст: "))
res = "Вход разрешен" if age >= 18 else "Вход запрещен"
print(res)

""" Определение скидки в магазине """
amount = int(input("Введите сумму покупки: "))
final_amount = amount * 0.9 if amount >= 5000 else amount
print("Итоговая сумма к оплате:", final_amount)


