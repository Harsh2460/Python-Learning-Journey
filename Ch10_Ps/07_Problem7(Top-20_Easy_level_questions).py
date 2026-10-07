# Easy Level Practice Questions

# 1.Create a class Student and create an object of it.

class Student:
    pass

c = Student()

print("Class is created.")

# 2.Create a class Student with a method display() that prints "Hello Student".

class Student:
    def display(self):
        print("Hello Student")

s = Student()
s.display()

# 3.Create a Student class with an instance attribute name. Take the student's name as input and display it.

class Student:
    pass

name = input("Enter student name: ")

h = Student()
h.name = name

print("Name =", h.name)

# 4.Create a class Student with name and age as instance attributes. Display both attributes.

class Student:
    pass

name = input("Enter the name: ")
age = input("Enter the age: ")

s = Student()
s.name = name
s.age = age

print("Name =",s.name)
print("Age =",s.age)

# 5.Create a class Student with:
# name
# age
# course
# Display all student details.

class Student:
    pass

name = input("Enter the name: ")
age = input("Enter the age: ")
course = input("Enter the course: ")

s = Student()
s.name = name
s.age = age
s.course = course

print("Name =",s.name)
print("Age =",s.age)
print("Course =",s.course)

# 6.Create an Employee class with name and salary as instance attributes. Display the employee's details.

class Employee:
    pass

name = input("Enter the employee name: ")
salary = input("Enter the salary: ")

e = Employee()
e.name = name 
e.salary = salary

print("Employee Name =",e.name)
print("Employee Salary =",e.salary)

# 7.Create a class Person with a method introduce() that uses self.name to display:
# My name is Rahul

class Person:
    def introduce(self):
        print("My name is Rahul")

p = Person()
p.introduce()

# 8.Create a class Employee with a class attribute:
# company = "Google"
# Create two objects and display the company name using both objects.

class Employee:
    company = "Google"

e = Employee()
c = Employee()

print("Company Name =",e.company)
print("Company Name =",c.company)

# 9.Create an Employee class with:
# company = "Google"
# Change the class attribute to "Microsoft" and display it.

class Employee:
    company = "Google"

print("Before =",Employee.company)

Employee.company = "Microsoft"

print("After =",Employee.company)

# 10.Create a class Employee with a class attribute company = "Google".
# Create two employees with different names and salaries.
# Display their details.

class Employee:
    company = "Google"

e1 = Employee()
e2 = Employee()

e1.name = input("Enter Employee 1 Name: ")
e1.salary = input("Enter Employee 1 Salary: ")

e2.name = input("Enter Employee 2 Name: ")
e2.salary = input("Enter Employee 2 Salary: ")

print("Employee 1 Name =",e1.name)
print("Employee 1 Salary =",e1.salary)

print("Employee 2 Name =",e2.name)
print("Employee 2 Salary =",e2.salary)

# 11.Create a class:
# class Employee:
#     company = "Google"
# Create an object and give it its own company attribute:
# employee.company = "Microsoft"
# Display the company using both the object and the class.

class Employee:
    company = "Google"

e = Employee()
print("Before =", e.company)

e.company = "Microsoft"

print("After =", e.company)

print("Class company =", Employee.company)

# 12.Create a class Student with an __init__() constructor that automatically prints:
# Student object created
# when an object is created.

class Student:
    def __init__(self):
        print("Student object created")

s = Student()

# 13.Create a class Student whose constructor accepts name and stores it in:
# self.name
# Display the name.

class Student:
    def __init__(self,name):
        self.name = name

name = input("Enter name: ")

s = Student(name)

print("Name =",s.name)

# 14.Create a class Employee with an __init__() constructor that accepts:
# name
# age
# salary
# Display all three values.

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

name = input("Enter the name: ")
age = input("Enter the age: ")
salary = input("Enter the salary: ")

e = Employee(name,age,salary)

print("Name =",e.name)
print("Age =",e.age)
print("Salary =",e.salary)

# 15.Create an Employee class with a salary attribute and a method getSalary() that displays the salary.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print("Salary =",self.salary)

name = input("Enter name: ")
salary = input("Enter salary: ")

e = Employee(name,salary)

print("Name =",e.name)

e.getSalary() # call the getSalary method

# 16.Create a class Student with a method greet() that displays:
# Good Morning, Student!

class Student:
    def greet(self):
        print("Good Morning, Student!")

s = Student()
s.greet()

# 17.Create a class Calculator with a static method welcome() that displays:
# Welcome to Calculator
# Call the method without creating an object.

class Calculator:
    @staticmethod
    def welcome():
        print("Welcome to Calculator")

Calculator.welcome()

# 18.Create a class Calculator with a static method square(n) that returns the square of a number.
# Take the number as input and display the result.

class Calculator:
    @staticmethod
    def square(n):
        return n * n

n = int(input("Enter the number: "))

c = Calculator()
print("Square =",c.square(n))
# or 
print("Square =",Calculator.square(n))

# 19.Create a class Calculator with methods:
# add()
# subtract()
# multiply()
# divide()
# Take two numbers as input and display the results.

class Calaculator:
    def add(self,a,b):
        return a + b
    
    def subtract(self,a,b):
        return a - b
    
    def multiply(self,a,b):
        return a * b
    
    def divide(self,a,b):
        return a / b

a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))

c = Calaculator()

print("Add =",c.add(a,b))
print("Subtract =",c.subtract(a,b))
print("Multiply =",c.multiply(a,b))
print("Divide =",c.divide(a,b))

# 20.Create a Student class using a constructor with:
# name
# age
# course
# marks
# Create an object and display all student information using a method called display().

class Student:
    def __init__(self,name,age,course,marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("Name =",self.name)
        print("Age =",self.age)
        print("Course =",self.course)
        print("Marks =",self.marks)

name = input("Enter the name: ")
age = input("Enter the age: ")
course = input("Enter the course: ")
marks = input("Enter the marks: ")

s = Student(name,age,course,marks)

s.display()