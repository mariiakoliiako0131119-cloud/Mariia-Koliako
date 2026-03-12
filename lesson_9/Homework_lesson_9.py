# Задание 1

fruits = {"Яблоко": 60, "Банан": 110, "Киви": 150, "Груша": 220}
fruits.setdefault('Мандарин', 80)
print(fruits)

Задание 2

grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
for name, grade in grades.items():
    if grade >= 4:
        print(name)

# Задание 3

countries = {"Россия": "Москва", "Италия": "Милан", "Греция": "Афины", "Франция": "Париж"}
country = input("Введите страну: ")
found = False
for c in countries:
    if c  == country:
        print("Столица:", countries[c])
        found = True
if not found:
    print("Страна не найдена")

# Задание 4

students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]
courses = {}
for name, course in students:
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
print(courses)

# Задание 5

grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
print(grades)
item = grades.popitem()
print(item)
print(grades)

# Задание 6

students = ["Анна", "Борис", "Виктор", "Галина"]
students_dict = dict.fromkeys(("Анна", "Борис", "Виктор", "Галина"))
print(students_dict)
students_dict["Анна"] = 20
students_dict["Борис"] = 22
students_dict["Виктор"] = 24
students_dict["Галина"] = 19
print(students_dict)

# Задание 7

exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
currency = input("Введите валюту: ")
found = False
for c in exchange_rates:
    if c == currency:
        print("Курс:", exchange_rates[c])
        found = True
if not found:
    print("Неизвестная валюта")
    exchange_rates[currency] = None
print(exchange_rates)

# Задание 8

dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)

# Задание 1

t = (10, "Привет", 3.5, True, "Python")
print(t[2])
print(t[-1])

# Задание 2

nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
print(nums.count(4))
print(nums.index(7))

# Задание 3

lst = ["Python", "Java", "C++", "JavaScript"]
t = tuple(lst)
print(t)
print("C++" in t)

# Задание 4

t = (1,2,3,4,5,6,7,8,9,10)
print(t[:3])
print(t[-3:])
print(t[::2])


# Задание 5
t = (1, [2,3,4], {"a": 10})
t[1][2] = 9
print(t)
t[1].append(12)
print(t)

