# 1. Employee Management System
# Create a class Employee with:
# name
# salary
# display() method
# Create a Manager class that inherits from Employee and adds:
# department
# Override display() using super()
# Create a SeniorManager class that inherits from Manager and adds:
# experience

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

class SeniorManager(Manager):
    def __init__(self, name, salary, department,experience):
        super().__init__(name, salary, department)
        self.experience = experience

    def display(self):
        super().display()
        print("Experience =",self.experience, "years")

name = input("Enter the name: ")
salary = float(input("Enter the salary: "))
department = input("Enter the department: ")
experience = int(input("Enter the experience: "))

s = SeniorManager(name,salary,department,experience)
s.display()

# 2. Bank Account with Getter and Setter
# Create a class BankAccount with:
# account_holder
# _balance
# Use @property for balance.
# Setter should:
# Allow balance only if it is 0 or greater
# Otherwise print "Invalid balance"
# Add a method deposit() to increase the balance.

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value >= 0:
            self._balance = value
        else:
            print("Invalid balance")

    def deposit(self,amount):
        self._balance += amount

account_holder = input("Enter account holder: ")
balance = int(input("Enter initial balance: "))

b = BankAccount(account_holder,balance)

print("Account Holder Name =",b.account_holder)
print("Balance =",b.balance)

amount = int(input("Enter the deposit amount: "))
b.deposit(amount)

print("New Balance =",b.balance)

# 3. Company System with Class Method
# Create an Employee class with:
# name
# salary
# Class variable company = "Google"
# Create a Programmer class inheriting from Employee with:
# language
# Create a class method change_company() that changes the company for all employees.
# Create two programmer objects and display their information before and after changing the company.

class Employee:
    company = "Google"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

    def display(self):
        print("Name =",self.name)
        print("Salary =",self.salary)
        print("Comapany =",self.company)

class Programmer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language =",self.language)

name1 = input("Enter first programmer name: ")
salary1 = int(input("Enter first salary: "))
language1 = input("Enter first language: ")

name2 = input("Enter second programmer name: ")
salary2 = int(input("Enter second salary: "))
language2 = input("Enter second language: ")

p1 = Programmer(name1,salary1,language1)
p2 = Programmer(name2,salary2,language2)

print("\nBefore changing company:")
p1.display()
print()
p2.display()

new_company = input("\nEnter new company: ")
Employee.change_company(new_company)

print("\nAfter changing company:")
p1.display()
print()
p2.display()

# 4. Multiple Inheritance + Operator Overloading
# Create:
# Student class → name, marks
# Employee class → salary
# WorkingStudent(Student, Employee) → inherits both
# Overload the + operator so that:
# student1 + student2
# returns the total marks of both students.
# Also implement __str__() to display the student's name and marks.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}"

class Employee:
    def __init__(self,salary):
        self.salary = salary

class WorkingStudent(Student,Employee):
    def __init__(self, name, marks,salary):
        Student.__init__(self,name, marks)
        Employee.__init__(self,salary)

name1 = input("Enter first name: ")
marks1 = int(input("Enter first marks: "))
salary1 = int(input("Enter first salary: "))

name2 = input("Enter second name: ")
marks2 = int(input("Enter second marks: "))
salary2 = int(input("Enter second salary: "))

w1 = WorkingStudent(name1,marks1,salary1)
w2 = WorkingStudent(name2,marks2,salary2)

print("\nStudent 1:")
print(w1)

print("Salary =",w1.salary)

print("\nStudent 2:")
print(w1)

print("Salary =",w2.salary)

print("\nTotal Marks =",w1 + w2)

# 5. Complete Student Result System 
# Create a Student class with:
# name
# _marks
# subjects
# Requirements:
# Use @property and setter for marks.
# Marks must be between 0 and 100.
# Use __len__() to return the number of subjects.
# Use __str__() to display student information.
# Overload + to add the marks of two students.
# Create a class method change_school() to change the school name for all students.

class Student:
    school = "ABC School"
    def __init__(self,name,marks,subjects):
        self.name = name
        self._marks = marks
        self.subjects = subjects

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid Marks")

    def __len__(self):
        return len(self.subjects)

    def __str__(self):
        return f"Name : {self.name}, Marks: {self.marks}"

    def __add__(self, other):
        return self.marks + other.marks

    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school

name1 = input("Enter first student name: ")
marks1 = int(input("Enter first student marks: "))
subjects1 = input("Enter first student subjects: ").split(",")

name2 = input("Enter second student name: ")
marks2 = int(input("Enter second student marks: "))
subjects2 = input("Enter second student subjects: ").split(",")

s1 = Student(name1,marks1,subjects1)
s2 = Student(name2,marks2,subjects2)

print("\nStudent 1:")
print(s1)
print("Subjects:",len(s1))
print("School:",s1.school)

print("\nStudent 2:")
print(s2)
print("Subjects:",len(s2))
print("School:",s2.school)

print("\nTotal Marks:",s1 + s2)

new_school = input("Enter new school: ")
Student.change_school(new_school)

print("\nAfter Changing School:")
print("Student 1 school:",s1.school)
print("Student 2 school:",s2.school)