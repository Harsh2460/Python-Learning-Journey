# Medium Level Practice Questions

# 1.Create an Employee class with:
# name
# salary
# Create a Programmer class that inherits from Employee and adds:
# language
# Use a constructor and display all details.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Programmer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language = language

name = input("Enter the name: ")
salary = float("Enter the salary: ")
language = input("Enter the language: ")

p = Programmer(name,salary,language)

print("Name =",p.name)
print("Salary =",p.salary)
print("Language =",p.language)

# 2.Create a parent class Employee with a display() method.
# Create a child class Manager that:
# Overrides display()
# Uses super().display()
# Displays an additional department attribute.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name =",self.name)
        print("Salary =",self.salary)

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department =",self.department)

name = input("Enter the name: ")
salary = float(input("Enter the salary: "))
department = input("Enter the department: ")

m = Manager(name,salary,department)
m.display()

# 3.Create:
# Student class → course
# Employee class → salary
# Create a WorkingStudent class that inherits from both classes.
# Use a constructor to initialize all values and display the complete details.

class Student:
    def __init__(self,course):
        self.course = course

class Employee:
    def __init__(self,salary):
        self.salary = salary

class WorkingStudent(Student,Employee):
    def __init__(self, course,salary,name):
        Student.__init__(self,course)
        Employee.__init__(self,salary)
        self.name = name

    def display(self):
        print("Name =",self.name)
        print("Course =",self.course)
        print("Salary =",self.salary)

name = input("Enter the name: ")
course = input("Enter the course: ")
salary = float(input("Enter the salary: "))

w = WorkingStudent(course,salary,name)
w.display()

# 4.Create the following inheritance chain:
# Employee
#    ↓
# Programmer
#    ↓
# SeniorProgrammer
# Employee → name
# Programmer → programming language
# SeniorProgrammer → experience
# Use super() to initialize the parent attributes.

class Employee:
    def __init__(self,name):
        self.name = name

class Programmer(Employee):
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language

class SenoirProgrammer(Programmer):
    def __init__(self,name,language,experience):
        super().__init__(name,language)
        self.experience = experience

    def display(self):
        print("Name =",self.name)
        print("Language =",self.language)
        print("Experience =",self.experience,"years")

name = input("Enter the name: ")
language = input("Enter the language: ")
experience = int(input("Enter the experience: "))

s = SenoirProgrammer(name,language,experience)
s.display()

# 5.Create an Employee class with:
# company = "Google"
# Create a class method change_company() that changes the company name.
# Create two employee objects and show that changing the class attribute affects both objects.

class Employee:
    company = "Google"

    def __init__(self,name):
        self.name = name

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

    def display(self):
        print("Name =",self.name)
        print("Company =",self.company)

name1 = input("Enter the Name 1: ")
name2 = input("Enter the Name 2: ")

e1 = Employee(name1)
e2 = Employee(name2)

print("\nBefore changing Comapny:")
e1.display()
e2.display()

new_company = input("\nEnter new company: ")
Employee.change_company(new_company)

print("\nAfter changing Company:")
e1.display()
e2.display()

# 6.Create an Employee class with a private-style attribute:
# _ename
# Create:
# @property name → getter
# @name.setter → setter
# Take the employee name from the user, display it, change it using the setter, and display the new name.

class Employee:
    def __init__(self,name):
        self._ename = name

    @property
    def name(self):
        return self._ename

    @name.setter
    def name(self,new_name):
        self._ename = new_name

name = input("Enter the name: ")
new_name = input("Enter new name: ")

e1 = Employee(name)

print("Name =",e1.name)

e1.name = new_name
print("New Name =",e1.name)

# 7.Create a Student class with a marks property.
# Use a getter and setter.
# The setter should allow marks only between 0 and 100.
# If the user enters an invalid value, display:
# Invalid marks

class Student:
    def __init__(self,marks):
        self._marks = 0
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")

marks = int(input("Enter the marks: "))

s = Student(marks)
print("Marks =",s.marks)

# 8.Create a Number class with a value attribute.
# Overload:
# + using __add__()
# - using __sub__()
# Create two objects and perform both operations.

class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

n1 = Number(a)
n2 = Number(b)

print("Addition =",n1 + n2)
print("Subtraction =",n1 - n2)

# 9.Create an Employee class with a salary attribute.
# Overload the + operator so that:
# e1 + e2
# returns the combined salary of both employees.

class Employee:
    def __init__(self,salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

Employee1 = int(input("Enter the salary of Employee 1: "))
Employee2 = int(input("Enter the salary of Employee 2: "))

e1 = Employee(Employee1)
e2 = Employee(Employee2)

print("Combined Salary =",e1 + e2)

# 10.Create a Student class with:
# name
# course
# subjects
# Implement:
# __str__() → displays student name and course.
# __len__() → returns the number of subjects.
# Then use:
# print(student)
# print(len(student))

class Student:
    def __init__(self,name,course,subjects):
        self.name = name
        self.course = course
        self.subjects = subjects

    def __str__(self):
        return "Name: " + self.name + ", Course: " + self.course 

    def __len__(self):
        return len(self.subjects)

name = input("Enter the name: ")
course = input("Enter the course: ")
subjects = input("Enter the subjects separated by comma: ")

subjects_list = subjects.split(",")

student = Student(name,course,subjects_list)

print(student)
print("Number of subjects =",len(student))