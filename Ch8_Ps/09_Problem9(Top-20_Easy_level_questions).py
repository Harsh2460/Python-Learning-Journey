# Easy Level Practice Questions

# 1. Write a function greet() that prints "Good Day".

def greet():
    print("Good Day")

greet()

# 2. Write a function welcome() that prints "Welcome to Python".

def welcome():
    print("Welcome to Python")

welcome()

# 3. Write a function hello() and call it three times.

def hello():
    print("Hello")

hello()
hello()
hello()

# 4. Create a function show_name() that prints name.

def show_name():
    print("Rohan")

show_name()

# 5. Create a function show_details() that prints name, age, and course.

def show_details():
    print("Name: Sohan")
    print("Age: 26")
    print("Course: P.hd")

show_details()

# 6. Write a function greet(name) that takes a name as an argument and prints a greeting.

def greet(name):
    print("Hello,",name)

name = input("Enter the name: ")
greet(name)

# 7. Write a function add(a, b) that takes two numbers and prints their sum.

def add(a,b):
    print("Sum:",a + b)

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

add(a,b)

# 8. Write a function subtract(a, b) that takes two numbers and prints their difference

def subtract(a,b):
    print("Difference:",a - b)

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

subtract(a,b)

# 9. Write a function multiply(a, b) that takes two numbers and prints their product.

def multiply(a,b):
    print("Product:",a*b)

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

multiply(a,b)

# 10. Write a function square(n) that takes a number and prints its square.

def square(n):
    print("Square:",n ** 2)

n = int(input("Enter the number: "))
square(n)

# 11. Write a function add(a, b) that returns the sum of two numbers.

def add(a,b):
    return a + b

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

c = add(a,b)
print("Sum:",c)

# 12. Write a function cube(n) that returns the cube of a number.

def cube(n):
    return n ** 3

n = int(input("Enter the number: "))

a = cube(n)
print("Cube:",a)

# 13. Write a function average(a, b, c) that returns the average of three numbers.

def average(a,b,c):
    return (a + b + c)/3

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

d = average(a,b,c)
print("Average:",round(d,2))

# 14. Write a function area(length, width) that returns the area of a rectangle.

def area(length,width):
    return length * width

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

a = area(length,width)
print("Area of a rectangle:",a)

# 15. Write a function convert_celsius(celsius) that converts Celsius to Fahrenheit and returns the result.

def convert_celsius(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in celsius: "))

fahrenheit = convert_celsius(celsius)
print("Temperature in Fahrenheit:",fahrenheit,"°F")

# 16. Write a function greet(name="stranger") that prints a greeting. Call it:
# Without an argument
# With a name

def greet(name="stranger"):
    print("Hello,",name)

greet()

name = input("Enter the name: ")
greet(name)

# 17. Write a function power(number, exponent=2) that returns the result of raising a number to the given power.

def power(number,exponent=2):
    return number ** exponent

number = int(input("Enter the number: "))

result = power(number)
print("Power:",result)

# 18. Take a string as input and use a function to find its length.

text = input("Enter the text: ")

length = len(text)
print("Length:",length)

# 19. Take five numbers in a list and use built-in functions to find the maximum, minimum, and sum.

num = [10,20,30,40,50]

print("Maximum:",max(num))
print("Minimum:",min(num))
print("Sum:",sum(num))

# 20. Write a recursive function countdown(n) that prints numbers from n to 1.
# Example:
# Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1

def countdown(n):
    if n == 0:
       return
    print(n)
    countdown(n-1)

n = int(input("Enter the number: "))
countdown(n)