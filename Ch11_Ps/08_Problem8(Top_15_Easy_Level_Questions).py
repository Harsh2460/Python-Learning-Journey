# Easy Level Practice Questions 

# 1.Create a Person class with a method display() that prints "I am a person". Create a Student class that inherits from Person and call the inherited method.

class Person:
    def display(self):
        print("I am a person")

class Student(Person):
    pass

s = Student()
s.display()

# 2.Create an Employee class with a method show_name(). Create a Programmer class that inherits from Employee and add a method show_language().

class Employee:
    def show_name(self):
        print("Name of Employee: Rahul")

class Programmer(Employee):
    def show_language(self):
        print("Langauge is: Python")

p = Programmer()
p.show_name()
p.show_language()

# 3.Create a parent class Employee with a class attribute company = "Google". Create a child class Programmer and access the company attribute using a Programmer object.

class Employee:
    company = "Google"

class Programmer(Employee):
    pass

p = Programmer()
print("Company =",p.company)

# 4.Create a parent class Animal with a method sound(). Create a child class Dog that overrides the sound() method.

class Animal:
    def sound(self):
        print("Animal makes a generic sound")

class Dog(Animal):
    # Overrides the sound() method of Animal
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

# 5.Create an Employee class with a constructor that accepts name. Create a Programmer class that uses super().__init__() to call the parent constructor.

class Employee:
    def __init__(self,name):
        self.name = name

class Programmer(Employee):
    def __init__(self, name,language):
        super().__init__(name)
        self.language = language

name = input("Enter the name: ")
language = input("Enter the language: ")

p = Programmer(name,language)
print("Name =",p.name)
print("Language =",p.language)

# 6.Create a parent class Person with a display() method. Override display() in the child class and use super().display() to call the parent method.

class Person:
    def display(self):
        print("This is a parent class.")

class Student(Person):
    def display(self):
        super().display()
        print("This is a child class")

s = Student()
s.display()

# 7.Create two classes:
# Father with a method father_info()
# Mother with a method mother_info()
# Create a Child class that inherits from both classes and call both methods.

class Father:
    def father_info(self):
        print("Father: Engineer")

class Mother:
    def mother_info(self):
        print("Mother: Teacher")

class Child(Father,Mother):
    pass

c = Child()
c.father_info()
c.mother_info()

# 8.Create three classes:
# Grandparent → Parent → Child
# Give each class one method and access all three methods using a Child object.

class Grandparent:
    def show(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def display(self):
        print("I am Parent")

class Child(Parent):
    def result(self):
        print("I am Child")

c = Child()
c.show()
c.display()
c.result()

# 9.Create an Employee class with a class attribute company. Create a class method change_company() that changes the company name.

class Employee:
    company = "Google"

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

print("Before =",Employee.company)

new_company = input("Enter new company: ")
Employee.change_company(new_company)
print("After =",Employee.company)

# 10.Create a Student class with a class attribute school = "ABC School". Create a class method to change the school name.

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school

print("Old School =",Student.school)

new_school = input("Enter new school: ")
Student.change_school(new_school)
print("New School =",Student.school)

# 11.Create an Employee class with an attribute ename. Use the @property decorator to create a getter called name. Display the name using:
# e.name

class Employee:
    def __init__(self,name):
        self.ename = name

    @property
    def name(self):
        return self.ename

name = input("Enter the name: ")

e = Employee(name)
print("Name =",e.name)

# 12.Create an Employee class with ename. Use:
# @property for the getter
# @name.setter for the setter
# Allow the user to change the employee's name using:
# e.name = "Rahul"

class Employee:
    def __init__(self,name):
        self.ename = name

    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self,value):
        self.ename = value

name = input("Enter the name: ")
new_name = input("Enter the new name: ")

e = Employee(name)
print("Old Name =",e.name)

e.name = new_name
print("New Name =",e.name)

# 13.Create a Number class with an attribute value. Overload the + operator using __add__() so that two Number objects can be added.

class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

n1 = Number(a)
n2 = Number(b)

result = n1 + n2
print("Sum =",result)

# 14.Create a Student class with name and course. Define __str__() so that printing the object displays the student's details.

class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def __str__(self):
        return "Name: " + self.name + ", Course: " + self.course

name = input("Enter the name: ")
course = input("Enter the course: ")

s = Student(name,course)
print(s)

# 15.Create a Student class containing a list of subjects. Define __len__() so that:
# len(student)
# returns the number of subjects.

class Student:
    def __init__(self,subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)

subjects = input("Enter subjects separted by comma: ")

subjects_list = subjects.split(",")

s = Student(subjects_list)
print("Number of subjects =",len(s))
