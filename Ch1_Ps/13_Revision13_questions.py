# Revision

# 1.Print "Hello, Python!".

print("Hello, Python!")

# 2.Write a program using single-line comments.

# Printing the Hello World!
print("Hello Python!")

# 3.Write a program using multi-line comments.

"""Welcome Python
Rohit Sharme playing cricket
"""
print("Hello Python")

# 4.Import the math module and print the value of π.

import math

print(math.pi)

# 5.Import the random module and print a random number.

import random

print(random.randint(1,10))

## 6.Import the calendar module and display the calendar of a given year.

import calendar

y = int(input("Enter year: "))

print(calendar.calendar(y))

## 7.Import the datetime module and print today's date

import datetime

print(datetime.date.today())

## 8.Import the keyword module and print all Python keywords.

import keyword

print(keyword.kwlist)

# 9.Import both math and random modules and use functions from both.

import math
import random

print(math.sqrt(64))
print(random.randint(1,100))

## 10.Write a program using at least three built-in modules.

import random
import math
import keyword

print(random.randint(1,10))
print(math.sqrt(144))
print(keyword.kwlist[:5])