# Задание 1

set_1 = {1, 2, 4, 5, True, "str", (9, 5)}
set_1.add(10)
print(set_1)
set_1.add(10)
print(set_1)

# Задание 2

cities = set(["Москва", "Париж", "Лондон", "Москва", "Берлин", "Париж"])
print(cities)
print(len(cities))

# Задание 3

nums = set(range(1, 11))
nums.remove(5)
nums.discard(15)
print(nums)

# Задание 4

str = set("abrakadabra")
print(str)

# Задание 5

s = set()
s.add(10)
s.add("hello")
s.add((1, 2, 3))
s.add([4, 5, 6])  # вызовет ошибку, потому что это список
print(s)

# Задание 6

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)
print(A | B)
print(A - B)
print(B - A)
print(A ^ B)

# Задание 7

even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers & odd_numbers)
print(even_numbers | odd_numbers)

# Задание 8

python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
print(python_students & java_students)
print(python_students ^ java_students)
print(python_students | java_students)

# Задание 9

text1 = set("программирование")
text2 = set("автоматизация")
print(text1 & text2)
print(text1 - text2)
print(text1 ^ text2)

# Задание 1

s = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print(s)
print(sorted(s))

# Задание 2

words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
s = set(w.upper() for w in words)
print(s)

# Задание 3

grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
result = {name: "Отлично" if grade >= 80 else "Удовлетворительно" for name, grade in grades.items()}
print(result)

# Задание 4

text = {"Python", "automation", "programming", "testing"}
result = {word: len(word) for word in text}
print(result)

# Задание 5

n = 10
result = {i: {j**2 for j in range(1, i + 1)} for i in range(1, n + 1)}
print(result)