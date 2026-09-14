# Medium Level Practice Questions

# 1.Take three numbers as input and print the largest number using if-elif-else.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is num1:",num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is num2:",num2)
else:
    print("Largest number is num3:",num3)

# or

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

# 2.Take marks as input and display the grade using the following criteria:
# 90–100 → Grade A
# 75–89 → Grade B
# 60–74 → Grade C
# 33–59 → Grade D
# Below 33 → Fail

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 33:
    print("Grade D")
else:
    print("Fail") 

# 3.Take a year as input and check whether it is a leap year using the correct leap year rules:
# Divisible by 400, or
# Divisible by 4 but not by 100.

year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

# 4.Create a simple calculator.
# Take two numbers and an operator (+, -, *, /) as input and perform the selected operation.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
o = input("Enter operator(+,-,*,/): ")

if o == "+":
    print("Add:", a + b)
elif o == "-":
    print("Subtract:", a - b)
elif o == "*":
    print("Multiplication:", a * b)
elif o == "/":
    print("Division:", a / b)
else:
    print("Invalid Operator")

## 5.Take a character as input and check whether it is:
# Uppercase letter
# Lowercase letter
# Digit
# Special character

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

# 6.Take three numbers as input and print the smallest number.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 <= num2 and num1 <= num3:
    print("Smallest number is num1:",num1)
elif num2 <= num3:
    print("Smallest number is num2:",num2)
else:
    print("Smallest number is num3:",num3)

# 7.Calculate the electricity bill based on the following slabs:
# Up to 100 units → ₹5 per unit
# 101–200 units → ₹7 per unit
# Above 200 units → ₹10 per unit

units = int(input("Enter the units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Bill:",bill)

# 8.Calculate the employee bonus based on salary:
# Salary ≥ ₹50,000 → 20% bonus
# Salary ≥ ₹30,000 → 10% bonus
# Otherwise → 5% bonus
# Print the bonus amount.

salary = int(input("Enter salary: "))

if salary >= 50000:
    bonus = salary * 0.20
elif salary >= 30000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus amount:",bonus)

# or

salary = int(input("Enter salary: "))

if salary >= 50000:
    bonus = salary * 20 / 100
elif salary >= 30000:
    bonus = salary * 10 / 100
else:
    bonus = salary * 5 / 100

print("Bonus =", bonus)

# 9.Take three angles as input and check whether they can form a valid triangle.
# (Hint: Sum of angles should be 180°.)

a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a + b + c == 180:
    print("Valid triangle")
else:
    print("Not a valid triangle")

# 10.Take a number as input and check whether it is divisible by both 2 and 7. 

num = int(input("Enter number: "))

if num % 2 == 0 and num % 7 == 0:
    print("Divisible by both 2 and 7")
else:
    print("Not divisible")

# 11.Calculate the shopping discount based on purchase amount:
# ₹10,000 or more → 20% discount
# ₹5,000–₹9,999 → 10% discount
# Below ₹5,000 → No discount
# Print the final payable amount.

amount = int(input("Enter amount: "))

if amount >= 10000:
    discount = amount * 0.20
elif amount >= 5000:
    discount = amount * 0.10
else:
    discount = 0

print("Payable amount:",amount - discount)

# 12.Check loan eligibility based on the following conditions:
# Age ≥ 21
# Salary ≥ ₹25,000
# If both conditions are true, print "Loan Approved"; otherwise print "Loan Rejected".

age = int(input("Enter age: "))
salary = int(input("Enter salary: "))

if age >= 21 and salary >= 25000:
    print("Loan Approved")
else: 
    print("Loan Rejected")

# 13.Calculate income tax based on salary:
# Up to ₹2,50,000 → No Tax
# ₹2,50,001–₹5,00,000 → 5%
# ₹5,00,001–₹10,00,000 → 20%
# Above ₹10,00,000 → 30%
# Print the tax amount.

salary = int(input("Enter salary: "))

if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print("Tax amount:",tax)

# 14.Take three numbers as input and print the second largest number.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    print("Second Largest:",a)
elif (b >= a and b <= c) or (b >= c and b <= a):
    print("Second Largest:",b)
else:
    print("Second Largest:",c)

# 15.Create a login system.
# Take a username and password as input.
# If the username is "admin" and the password is "python123", print "Login Successful".
# Otherwise, print "Invalid Username or Password".

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")