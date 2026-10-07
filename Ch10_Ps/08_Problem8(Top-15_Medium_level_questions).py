# Medium Level Practice Questions

# 1.Create a Student class with a constructor that accepts name, age, and course. Create an object and display all details.

class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

name = input("Enter name: ")
age = input("Enter age: ")
course = input("Enter course: ")

s = Student(name,age,course)

print("Name =",s.name)
print("Age =",s.age)
print("Course =",s.course)

# 2.Create an Employee class with name and salary. Use a method getSalary() to display the employee's salary.

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

e.getSalary()

# 3.Create an Employee class with name and salary. Create a method increment() that increases the salary by 10%.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def increment(self):
        self.salary = self.salary + (self.salary * 10 / 100)
        print("Increment salary =",self.salary)
       
name = input("Enter name: ")
salary = int(input("Enter salary: "))

e = Employee(name,salary)

print("Name =",e.name)
print("Salary =",e.salary)

e.increment()

# 4.Create an Employee class with a constructor. Create three employee objects with different names and salaries and display their details.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name =",self.name)
        print("Salary =",self.salary)

name1 = input("Enter Employee 1 name: ")
salary1 = input("Enter Employee 1 salary: ")

name2 = input("Enter Employee 2 name: ")
salary2 = input("Enter Employee 2 salary: ")

name3 = input("Enter Employee 3 name: ")
salary3 = input("Enter Employee 3 salary: ")

e1 = Employee(name1,salary1)
e2 = Employee(name2,salary2)
e3 = Employee(name3,salary3)

print("\nEmployee 1:")
e1.display()

print("\nEmployee 2:")
e2.display()

print("\nEmployee 3:")
e3.display()

# 5.Create an Employee class with a class attribute company = "Google". Create three employees and display their names and company.

class Employee:
    company = "Google"

    def __init__(self,name):
        self.name = name

    def display(self):
        print("Name =",self.name)
        print("Company =",self.company)

name1 = input("Enter Empolyee 1 Name: ")

name2 = input("Enter Empolyee 2 Name: ")

name3 = input("Enter Empolyee 3 Name: ")

e1 = Employee(name1)
e2 = Employee(name2)
e3 = Employee(name3)

print("\nEmployee 1:")
e1.display()

print("\nEmployee 2:")
e2.display()

print("\nEmployee 3:")
e3.display()

# 6.Create an Employee class with company = "Google". Change the company to "Microsoft" using the class name and display the company for all objects.

class Employee:
    company = "Google"

    def __init__(self,name):
        self.name = name

name1 = input("Enter Empolyee 1 Name: ")

name2 = input("Enter Empolyee 2 Name: ")

e1 = Employee(name1)
e2 = Employee(name2)

print("\nBefore changing:")
print(e1.name, " - ", e1.company)
print(e2.name, " - ", e2.company)

Employee.company = "Microsoft"

print("\nAfter changing:")
print(e1.name, " - ", e1.company)
print(e2.name, " - ", e2.company)

# 7.Create a class with a class attribute company = "Google". Create an object and give it its own company instance attribute. Display both values and explain which one takes preference.

class Emplyoee:
    company = "Google"

e = Emplyoee()

print("Class attriburte =",Emplyoee.company)
print("Before instance atttribute =",e.company)

e.company = "Microsoft" # instance attribute takes prefernce over class attribute
print("After instance atttribute =",e.company)
print("Class attriburte =",Emplyoee.company)

# 8.Create a Student class with name and marks. Create a method displayResult() that displays the student's name and marks.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def displayResult(self):
        print("Name =",self.name)
        print("Marks =",self.marks)

name = input("Enter the name: ")
marks = input("Enter the marks: ")

s = Student(name,marks)
s.displayResult()

# 9.Create a Student class with a constructor accepting name and marks. Create a method that displays "Pass" if marks are 40 or above, otherwise "Fail".

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

name = input("Enter the name: ")
marks = int(input("Enter the marks: "))

s = Student(name,marks)

print("Name =",s.name)
print("Marks =",s.marks)
s.display()

# 10.Create a Calculator class with methods:
# add()
# subtract()
# multiply()
# divide()
# Take two numbers from the user and perform all operations.

class Calculator:
    def add(self,a,b):
        print("Addition =",a + b)

    def subtract(self,a,b):
        print("Subtraction =",a - b)

    def multiply(self,a,b):
        print("Multiplication =",a * b)

    def divide(self,a,b):
        print("Division =",a / b)

a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))

c = Calculator()

c.add(a,b)
c.subtract(a,b)
c.multiply(a,b)
c.divide(a,b)

# 11.Create a Student class with a static method greet() that displays a welcome message. Call the method without creating an object.

class Student:
    @staticmethod
    def greet():
        print("Welcome to Goa")

Student.greet()

# 12.Create a Calculator class with two static methods
# square(n)
# cube(n)
# Take a number from the user and display its square and cube.

class Calculator:
    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def cube(n):
        return n * n * n

n = int(input("Enter the value: "))

print("Square =",Calculator.square(n))
print("Cube =",Calculator.cube(n))

# 13.Create an Employee class with name and salary. Create a method calculateBonus() that calculates a 5% bonus and displays the final salary.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculateBonus(self):
        self.salary = self.salary + (self.salary * 5 / 100)
        print("Final Salary =",self.salary)

name = input("Enter the name: ")
salary = int(input("Enter the salary: "))

e = Employee(name,salary)

print("Name =",e.name)
print("Salary =",e.salary)
e.calculateBonus()

# 14.Create a BankAccount class with:
# account_holder
# balance
# Create methods:
# deposit()
# withdraw()
# display_balance()
# Take the required values from the user and perform the operations.

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit amount =",amount)

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdraw amount =",amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder name =",self.account_holder)
        print("Balance =",self.balance)

account_holder = input("Enter the account_holder name: ")
balance = int(input("Enter initial balance in account: "))

b = BankAccount(account_holder,balance)

d_amount = int(input("Enter deposite amount: "))
b.deposit(d_amount)

w_amount = int(input("Enter withdraw amount: "))
b.withdraw(w_amount)

b.display_balance()

# 15.Create a Student class with:
# name
# age
# course
# marks
# Use a constructor to initialize the values and methods to:
# Display student details
# Calculate whether the student passed or failed
# Display the grade based on marks

class Student:
    def __init__(self,name,age,course,marks):
        self.name = name
        self.age = age
        self.course = course 
        self.marks = marks

    def studentDetails(self):
        print("Name =",self.name)
        print("Age =",self.age)
        print("Course =",self.course)
        print("Marks =",self.marks)

    def studentResult(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

    def studentGrade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks >= 60:
            print("Grade C")
        elif self.marks >= 40:
            print("Grade D")
        else:
            print("Grade F")

name = input("Enter the name: ")
age = input("Enter the age: ")
course = input("Enter the course: ")
marks = int(input("Enter the marks: "))

s = Student(name,age,course,marks)

print("\nStudent Details:")
s.studentDetails()

print("\nResult:")
s.studentResult()

print("\nGrade:")
s.studentGrade()