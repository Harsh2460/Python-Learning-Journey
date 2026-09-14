# Hard Level Practice Questions

# 1. Student Result Management System
# Write a program to:
# Take marks of five subjects as input.
# Calculate the total marks.
# Calculate the percentage.
# Display the grade using the following criteria:
# Percentage ≥ 90 → Grade A
# Percentage ≥ 75 → Grade B
# Percentage ≥ 60 → Grade C
# Percentage ≥ 33 → Grade D
# Below 33 → Fail
# Display Pass if the percentage is 33 or above; otherwise display Fail.

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total_marks = m1 + m2 + m3 + m4 + m5
percentage = total_marks / 5

print("Toatal Marks:",total_marks)
print("Percentage:",percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 33:
    print("Grade D")
else:
    print("Fail")

if percentage >= 33:
    print("Pass")
else:
    print("Fail")

# 2. ATM Mini Project
# Write a program to simulate an ATM.
# Set a predefined PIN (e.g., 1234).
# Take the PIN from the user.
# If the PIN is correct:
# Ask the user to choose an option:
# Balance Inquiry
# Deposit
# Withdraw
# Perform the selected operation.
# Otherwise, display "Invalid PIN".

pre_pin = 1234
balance = 10000

pin = int(input("Enter pin: "))

if pin == pre_pin:
    print("1.Balance Inquiry")
    print("2.Deposit")
    print("3.Withdraw")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:",balance) 
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Updated balance:",balance) 
    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Updated balance:",balance)
        else:
            print("Insufficient Balance")

    else:
        print("Invalid Choice")

else:
    print("Invalid Pin")

# 3. Electricity Bill Calculator
# Write a program to calculate the electricity bill based on the following slabs:
# First 100 units → ₹5 per unit
# Next 100 units (101–200) → ₹7 per unit
# Above 200 units → ₹10 per unit
# Additional Rules:
# If the total bill is greater than ₹2000, add a 5% surcharge.
# Display:
# Units Consumed
# Bill Amount
# Surcharge (if applicable)
# Final Bill

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) +  ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10) 

if bill > 2000:
    surcharge = bill * 0.05
else:
    surcharge = 0

final_bill = bill + surcharge

print("Units Consumed:",units)
print("Bill amount:",bill)
print("Surcharge:",surcharge)
print("Final Bill:",final_bill)

# 4. Employee Salary Management System
# Write a program to:
# Take the employee's basic salary as input.
# Calculate:
# HRA = 20% of basic salary
# DA = 10% of basic salary
# Calculate Bonus:
# Basic Salary ≥ ₹50,000 → 20%
# Basic Salary ≥ ₹30,000 → 10%
# Otherwise → 5%
# Calculate the Gross Salary.
# Display:
# Basic Salary
# HRA
# DA
# Bonus
# Gross Salary
# Salary Category:
# High Salary (Gross Salary ≥ ₹80,000)
# Medium Salary (Gross Salary ≥ ₹50,000)
# Low Salary (Otherwise)

salary = int(input("Enter basic salary: "))

hra = salary * 0.20
da = salary * 0.10

if salary >= 50000:
    bonus = salary * 0.20
elif salary >= 30000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

gross_salary = salary + hra + da + bonus

print("Basic Salary:",salary)
print("HRA:",hra)
print("DA:",da)
print("Bonus:",bonus)
print("Gross Salary:",gross_salary)

if gross_salary >= 80000:
    print("Salary Category: High Salary")
elif gross_salary >= 50000:
    print("Salary Category: Medium Salary")
else:
    print("Salary Category: Low Salary")

# 5. Online Shopping Billing System
# Write a program to:
# Take the total purchase amount as input.
# Apply the following discount:
# ₹20,000 or more → 20%
# ₹10,000–₹19,999 → 15%
# ₹5,000–₹9,999 → 10%
# Below ₹5,000 → No discount
# Calculate the discount amount.
# Calculate GST (18%) on the discounted amount.
# Display:
# Original Amount
# Discount
# Amount After Discount
# GST
# Final Payable Amount

amount = int(input("Enter purchase amount: "))

if amount >= 20000:
    discount = amount * 0.20
elif amount >= 10000:
    discount = amount * 0.15
elif amount >= 5000:
    discount = amount * 0.10
else:
    discount = 0

after_discount = amount - discount
gst = after_discount * 0.18
final_amount = after_discount + gst

print("Original Amount:",amount)
print("Discount:",discount)
print("Amount After Discount:",after_discount)
print("GST:",gst)
print("Final Payable Amount:",final_amount)