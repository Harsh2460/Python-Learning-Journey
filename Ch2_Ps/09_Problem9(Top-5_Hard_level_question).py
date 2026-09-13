# Hard Level Practice Questions

# 1. Advanced Student Report Card System
# Write a program that:
# Takes student name, roll number, and marks of 5 subjects
# Calculates total marks
# Calculates percentage
# Displays result in a proper format
# Also prints data types of all variables

name = input("Enter the name: ")
roll_no = input("Enter the roll_no: ")
a = int(input("Subject 1: "))
b = int(input("Subject 2: "))
c = int(input("Subject 3: "))
d = int(input("Subject 4: "))
e = int(input("Subject 5: "))

total_marks = a + b + c + d + e
percent = total_marks / 5

print("Name:",name)
print("Roll no:",roll_no)
print("Total Marks:",total_marks)
print("Percentage:",percent)

print(type(name),type(roll_no),type(total_marks),type(percent))

# 2. Smart Calculator (All Operators)
# Write a program that:
# Takes two numbers as input
# Performs:
# Addition
# Subtraction
# Multiplication
# Division
# Floor division
# Modulus
# Power

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:",a + b)
print("Subtraction:",a - b)
print("Multiplication:",a * b)
print("Division:",a / b)
print("Floor division:",a // b)
print("Modulus:",a % b)
print("Power:",a ** b)

# 3. Typecasting Challenge
# Write a program that:
# Takes input as string
# Converts it into:
# int
# float
# Then performs:
# Square of the number
# Cube of the number
# Print results with data types

a = input("Enter the number: ")

b = int(a)
c = float(a)

square = b ** 2
cube = b ** 3

print("Original:",a,type(a))
print("Integer:",b,type(b))
print("Float:",c,type(c))
print("Square:",square,type(square))
print("Cube:",cube,type(cube))

# 4. Real-Life Billing System
# Write a program that:
# Takes item name, price, and quantity as input
# Calculates total bill
# Applies 5% discount
# Prints final amount
# Also prints data types of all variables

name = input("Enter item name: ")
price = int(input("Enter item price: "))
quantity = int(input("Enter item quantity: "))

total_bill = price * quantity
discount = total_bill * 0.05
final_amount = total_bill - discount

print("Item Name:",name)
print("Item Price:",price)
print("Item quantity:",quantity)
print("Total Bill:",total_bill)
print("Discount:",discount)
print("Final Amount:",final_amount)

print(type(name),type(price),type(quantity),type(total_bill),type(discount),type(final_amount))

# 5. Mixed Data Type Analyzer
# Write a program that:
# Creates variables of all types:
# int
# float
# string
# boolean
# None
# Prints:
# Value of each variable
# Its data type using type()
# Then converts:
# int → float
# float → string
# string → int (if possible)

a = 10
b = 12.6
c = "16" # string → int (if possible)-> when string like "16" then it is possible otherwise not.
d = True
e = None

print(a,b,c,d,e)
print(type(a),type(b),type(c),type(d),type(e))

print(float(a))
print(str(b))
print(int(c))
