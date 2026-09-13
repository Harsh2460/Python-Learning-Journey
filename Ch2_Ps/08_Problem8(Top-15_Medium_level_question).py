# Medium Level Practice Questions

# 1.Write a program to take three numbers as input from the user and print their sum.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# print("Sum is:",num1 + num2 + num3)

# 2.Write a program to take marks of 5 subjects as input and calculate the average marks.

# a = int(input("Marks 1: "))
# b = int(input("Marks 2: "))
# c = int(input("Marks 3: "))
# d = int(input("Marks 4: "))
# e = int(input("Marks 5: "))

# print("Average marks:",(a+b+c+d+e)/5)

# 3.Write a program to take the length and breadth of a rectangle as input and calculate its area.

# l = int(input("Enter the length of rectangle: "))
# b = int(input("Enter the breadth of rectangle: "))

# rectangle = l * b
# print("Area of rectangle:",rectangle)

# 4.Write a program to swap the values of two variables.

# a = int(input("Enter value a: "))
# b = int(input("Enter value b: "))

# a,b = b,a

# print("a:",a)
# print("b:",b)

# 5.Take a number as input from the user and:
# Convert it to float
# Convert it to string
# Display the data type after each conversion

# number = int(input("Enter the number: "))

# a = float(number)
# print("Float value:",a)
# print("Data type:",type(a))

# b = str(number)
# print("String value:",b)
# print("Data type:",type(b))

# 6.Take the following inputs from the user:
# Name
# Age
# Class
# Percentage
# Print all the details neatly.

# Name = input("Enter the name: ")
# Age = input("Enter the age: ")
# Class = input("Enter the class: ")
# Percentage = input("Enter the percentage: ")

# print("Name:",Name)
# print("Age:",Age)
# print("Class:",Class)
# print("Percentage:",Percentage)

# 7.Write a program to calculate Simple Interest using:
# Take Principal, Rate, and Time as input from the user.

# p = float(input("Principal: "))
# r = float(input("Rate: "))
# t = float(input("Time: "))

# si = p * r * t / 100
# print("Simple Interest:",si)

# 8.Write a program to convert temperature from Celsius to Fahrenheit.

# c = float(input("Enter the value of celsius: "))

# f = (c * 9/5) + 32
# print("Temperature from Celsius to Fahrenheit:",f)

# 9.Take marks of 4 subjects as input and calculate:
# Total Marks
# Percentage

# a = int(input("Subject 1: "))
# b = int(input("Subject 2: "))
# c = int(input("Subject 3: "))
# d = int(input("Subject 4: "))

# total = a + b + c + d
# percent = total / 4

# print("Total:",total)
# print("Percentage:",percent)

# 10.Create variables of the following types:
# Integer
# Float
# String
# Boolean
# None
# Print each variable along with its data type.

# a = 10
# print(a)
# print(type(a))

# b = 8.2
# print(b)
# print(type(b))

# c = "Rohit"
# print(c)
# print(type(c))

# d = True
# print(d)
# print(type(d))

# e = None 
# print(e)
# print(type(e))

# 11.Take age in years as input and calculate the approximate age in months.

# age = int(input("Age in years: "))

# print("Months:",age * 12)

# 12.Take two numbers as input and perform:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# print("Addition:",a + b)
# print("Subtraction:",a - b)
# print("Multiplication:",a * b)
# print("Division:",a / b)
# print("Modulus:",a % b)

# 13.Take a monthly salary as input and calculate the annual salary.

# ms = float(input("Monthly salary: "))

# print("Annual salary:",ms * 12)

# 14.Take random name as input and print:
# Random name
# Number of characters in random name

# name = input("Enter the name: ")

# print(name)
# print(len(name))

# 15.Mini Student Result Program
# Take:
# Student Name
# Roll Number
# Marks in English
# Marks in Maths
# Marks in Science
# Calculate:
# Total Marks
# Percentage
# Display all information in a formatted way.

student_name = input("Enter the student name: ")
roll_number = input("Enter the roll no: ")
e = int(input("Marks of English: "))
m = int(input("Marks of Maths: "))
s = int(input("Marks of Science: "))

total_marks = e + m + s
percent = total_marks / 3

print("Student name:",student_name)
print("Roll no:",roll_number)
print("Total Marks:",total_marks)
print("Percentage:",percent)