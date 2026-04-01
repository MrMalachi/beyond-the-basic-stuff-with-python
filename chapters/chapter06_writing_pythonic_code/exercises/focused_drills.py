# Part 1: List Comprehension Drills

# Create a list of numbers from 1-10 & then convert into a list comprehension.
numbers = list(range(1, 11))
print(numbers)

# List comprehension
numbers = [number for number in range(1, 11)]
print(numbers)

# Create a list of only odd numbers from 1-15.
odd_numbers = []
for number in range(1, 16):
    if number % 2:
        odd_numbers.append(number)
print(odd_numbers)

# List comprehension
odd_numbers = [number for number in range(1, 16) if number % 2]
print(odd_numbers)

# Create a list of only even numbers, squared.
# Given:
nums = [1, 2, 3, 4, 5, 6]
even_nums = [number ** 2 for number in nums if number % 2 == 0]
print(even_nums)

# Create a list of words longer than 3 characters, converted to uppercase.
# Given:
words = ["apple", "hi", "banana", "cat", "grape"]
uppercase_three_character = [word.upper() for word in words if len(word) > 3]
print(uppercase_three_character)

# Create a list of only temperatures above 75, subtract 5 from each.
# Given:
temps = [72, 85, 90, 60, 77]
new_temps = [temp - 5 for temp in temps if temp > 75]
print(new_temps)

# Create: ["Alice", "Bob", "Charlie"]
# Given:
names = ["alice", "bob", "charlie"]
title_case_names = [name.title() for name in names]
print(title_case_names)

# Part 2: Rewrite to Pythonic

# Exercise 8 - Rewrite this:
result = []
for n in range(1, 11):
    if n % 2 == 0:
        result.append(n)
print(result)

result = [n for n in range(1, 11) if n % 2 == 0]
print(result)

# Exercise 9 - Rewrite this:
output = []
for word in words:
    output.append(word.lower())
print(output)

output = [word.lower() for word in words]
print(output)

# Exercise 10 - Rewrite this:
filtered = []
for word in words:
    if len(word) < 5:
        filtered.append(word.title())
print(filtered)

filtered = [word.title() for word in words if len(word) < 5]
print(filtered)

# Part 3: enumerate() Practice

# Exercise 11 - Print:
# 0 apple
# 1 banana
# 2 cherry
# Using:
items = ["apple", "banana", "cherry"]

for index, item in enumerate(items):
    print(index, item)

# Exercise 12 - Print:
# 1. red
# 2. blue
# 3. green
# Using:
colors = ["red", "blue", "green"]

for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")

# Exercise 13 - Thinking Exercise
# When should you NOT use enumerate()?

# the enumerate() function should not be used when you do not need to iterate
# over both index and values.


