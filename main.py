# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# AVERAGE HEIGHT
#
# student_height = input("Input a list of student heights: ").split()
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])
# print(student_height)
#
# total_sum = 0
# for height in student_height:
#     total_sum += height
#
# average_height = round(total_sum / int(len(student_height)))
# print(f"AVERAGE HEIGHT: {average_height}m")

# HIGHEST CLASS SCORE
#
# student_scores = input("INPUT A LIST OF STUDENT SCORES: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# highest_score = student_scores[0]
# for score in range(0, len(student_scores)):
#     if highest_score <= student_scores[score]:
#         highest_score = student_scores[score]
#
# print(f"THE HIGHEST SCORE IN THE CLASS IS: {highest_score}")

# ADDING EVEN NUMBERS 1-100
#
# adding_even_numbers = 0
# for n in range(0, 101, 2):
#     print(n)
#     adding_even_numbers += n
#
# print(f"TOTAL SUM OF EVEN NUMBERS: {adding_even_numbers}")

# FIZZBUZZ APP
# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

# PASSWORD GENERATOR PROJECT
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_letters = []
for n in range(1, nr_letters + 1):
    random_letters.append(letters[random.randint(0, int(len(letters)) - 1)])

# print(random_letters)

random_numbers = []
for n in range(1, nr_numbers + 1):
    random_numbers.append(numbers[random.randint(0, int(len(numbers)) - 1)])

# print(random_numbers)

random_symbols = []
for n in range(1, nr_symbols + 1):
    random_symbols.append(symbols[random.randint(0, int(len(symbols)) - 1)])

# print(random_symbols)

password = random_letters + random_numbers + random_symbols
print("THE EASY PASSWORD IS: " + "".join(password))
random.shuffle(password)
print("THE HARD PASSWORD IS: " + "".join(password))
