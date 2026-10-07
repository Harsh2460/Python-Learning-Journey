# Hard Level Practice Questions

# 1. Employee Salary Management
# Create an Employee class with:
# name
# salary
# department
# Use a constructor to initialize the values.
# Create methods:
# display() → display employee details
# calculate_bonus() → calculate 10% bonus
# final_salary() → display salary after adding the bonus
# Take all values from the user.

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name =",self.name)
        print("Salary =",self.salary)
        print("Department =",self.department)

    def calaculate_bonus(self):
        bonus = self.salary * 10 / 100
        print("Bonus Amount",bonus)

    def final_salary(self):
        bonus = self.salary * 10 / 100
        print("Final Salary =",self.salary + bonus)

name = input("Enter the name: ")
salary = int(input("Enter salary: "))
department = input("Enter department: ")

e = Employee(name,salary,department)

print("\nEmployee Details:")
e.display()

print("\nBonus:")
e.calaculate_bonus()

print("\nFinal Salary:")
e.final_salary()

# 2. Bank Account Management
# Create a BankAccount class with:
# account_holder
# account_number
# balance
# Create methods:
# deposit(amount)
# withdraw(amount)
# check_balance()
# Rules:
# Deposit amount should be added to balance.
# Withdrawal should happen only if sufficient balance is available.
# Otherwise display "Insufficient Balance".
# Take input from the user and perform both deposit and withdrawal.

class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit Amount =",amount)

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdraw Amount =",amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Account holder name:",self.account_holder)
        print("Account holder number:",self.account_number)
        print("Current Balance:",self.balance)

account_holder = input("Enter the account_holder name: ")
account_number = input("Enter the account_holder number: ")
balance = int(input("Enter initial balance in account: "))

account = BankAccount(account_holder,account_number,balance)

d_amount = int(input("Enter Deposit amount: "))
account.deposit(d_amount)

w_amount = int(input("Enter Withdraw amount: "))
account.withdraw(w_amount)

account.check_balance()

# 3. Student Grade Management
# Create a Student class with:
# name
# roll_no
# course
# marks
# Create methods:
# display_details()
# calculate_result()
# calculate_grade()
# Grade rules:
# Marks	Grade
# 90–100	A
# 75–89	B
# 60–74	C
# 40–59	D
# Below 40	F
# Also display Pass/Fail.

class Student:
    def __init__(self,name,roll_no,course,marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display_details(self):
        print("Name =",self.name)
        print("Rool_no =",self.roll_no)
        print("Course =",self.course)
        print("Marks =",self.marks)

    def calaculate_result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

    def calaculate_grade(self):
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
roll_no = input("Enter the roll_no: ")
course = input("Enter the course: ")
marks = int(input("Enter the marks: "))

s = Student(name,roll_no,course,marks)

print("\nStudent Details:")
s.display_details()

print("\nResult:")
s.calaculate_result()

print("\nGrade:")
s.calaculate_grade()

# 4. Shopping Cart Using Class
# Create a ShoppingCart class with:
# product_name
# price
# quantity
# Create methods:
# display_product()
# calculate_total()
# apply_discount()
# Rules:
# Total = price × quantity
# If total is ₹5000 or more → 10% discount
# Otherwise → no discount
# Display:
# Product name
# Price
# Quantity
# Total amount
# Discount
# Final amount

class ShoppingCart:
    def __init__(self,product_name,price,quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product name:",self.product_name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)

    def calaulate_total(self):
        total = self.price * self.quantity
        print("Toatal Amount:",total)

    def apply_discount(self):
        total = self.price * self.quantity
        if total >= 5000:
            discount = total * 10 / 100
            print("Discount Amount:",discount)
        else:
            discount = 0

        print("Final Amount:",total - discount)

product_name = input("Enter product name: ")
price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

s = ShoppingCart(product_name,price,quantity)

print("\nDetails:")
s.display_product()

print("\nTotal Amount:")
s.calaulate_total()

print("\nDiscount:")
s.apply_discount()

