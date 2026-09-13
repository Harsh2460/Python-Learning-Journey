# Revision 

# 1.Take two integers and print their sum.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("Sum:",a+b)

# 2.Take name and age as input and display them.

name = input("Enter name: ")
age = int(input("Enter age: "))

print(name)
print(age)

# 3.Find the data type of five different variables.

a = 10
b = 6.8
c = "Hello"
d = True
e = None

print(type(a),type(b),type(c),type(d),type(e))

# 4.Convert an integer into float.

a = int(input("Enter an integer: "))

b = float(a)
print(b)
print(type(b))

# 5.Convert a numeric string into an integer.

a = input("Enter a number: ")

b = int(a)
print(b)
print(type(b))

# 6.Take length and width as input and calculate the area of a rectangle.

l = float(input("Enter length: "))
w = float(input("Enter width: "))

print("Area of a rectangle: ", l * w)

# 7.Swap two variables using a third variable.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

temp = a
a = b
b = temp

print(a)
print(b)

# 8.Swap two variables without using a third variable.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

a,b = b,a
print(a)
print(b)

# 9.Take marks of three subjects and calculate the average.

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

average = (marks1 + marks2 + marks3) / 3
print("Average:",average)

# 10.Check the output data type after typecasting.

num = (input("Enter a number: "))
print(type(num))

num = int(num)
print(type(num))