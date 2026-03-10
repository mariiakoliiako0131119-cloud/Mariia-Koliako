# Задание 1
numbers = [1, 2, 3, 4, 5]
it_numbers = iter(numbers)
print(next(it_numbers))
print(next(it_numbers))
print(next(it_numbers))
print(next(it_numbers))
print(next(it_numbers))

# Задание 2
text = "Python"
it_text = iter(text)
print(next(it_text))
print(next(it_text))
print(next(it_text))
print(next(it_text))
print(next(it_text))
print(next(it_text))

# Задание 1
n = 10
result = [num ** 2 for num in range(1, n + 1)]
print(result)

# Задание 2
numbers = [x for x in range(-10, 11) if x % 2 == 0]
print(numbers)

# Задание 3
words = ["python", "code", "program", "AI"]
lengths = [len(word) for word in words]
print(lengths)

# Задание 4
result = ["Четное" if x % 2 == 0 else "Нечетное" for x in range(1, 21)]
print(result)

# Задание 5
list = [10, "python", [1,2,3]]
result = [True if type(x) in (str, list, tuple, dict, set) else False for x in list]
print(result)