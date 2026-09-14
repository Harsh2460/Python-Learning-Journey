# Easy Level Practice Questions

# 1.Take a number as input and check whether it is positive or negative.

num = int(input("Enter number: "))

if(num >= 0):
    print("This is a postive number")

else:
    print("This is a negative number")

# 2.Take a number as input and check whether it is even or odd.

num = int(input("Enter number: "))

if(num%2==0):
    print("Even")
else:
    print("Odd")

# 3.Take two numbers as input and print the greater number.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if(num1>num2):
    print("Greater is num 1:",num1)
else:
    print("Greater is num 2:",num2)

# 4.Take two numbers as input and check whether they are equal or not.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 == num2:
    print("It is Equal")
else:
    print("It is not equal")

# 5.Take three numbers as input and print the largest number.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1>=num2 and num1>=num3:
    print("Largest number num 1:",num1)
elif num2>=num3:
    print("Largest number num 2:",num2)
else:
    print("Largest number num 3:",num3)

# # or

if num1>=num2 and num1>=num3:
    print("Largest number num 1:",num1)
elif num2>=num1 and num2>=num3:
    print("Largest number num 2:",num2)
else:
    print("Largest number num 3:",num3)

# 6.Take the age of a person as input and check whether the person is eligible to vote.

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 7.Take the marks of a student as input and check whether the student has passed or failed. (Passing marks = 33)

marks = int(input("Enter marks: "))

if marks >= 33:
    print("Passed")
else:
    print("Failed")

# 8.Take a number as input and check whether it is divisible by 5.

num = int(input("Enter number: "))

if num % 5 == 0:
    print("It is divisible by 5")
else:
    print("It is not divisible by 5")

# 9.Take a number as input and check whether it is divisible by both 3 and 5.

num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("It is divisible by both 3 and 5")
else:
    print("It is not divisible by both 3 and 5")

# 10.Take a character as input and check whether it is a vowel or a consonant.

ch = input("Enter charcter: ")

if ch in "aeiouAEIOU":
    print("It is Vowel")
else:
    print("It is Consonant")

# 11.Take a year as input and check whether it is a leap year. 

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not Leap year")

# 12.Take the temperature (in °C) as input. Print:
# Hot if the temperature is above 35°C
# Normal otherwise

temp = int(input("Enter temperature: "))

if temp > 35:
    print("Hot")
else:
    print("Normal")

# 13.Take a number as input and check whether it is a multiple of 10.

num = int(input("Enter number: "))

if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not multiple of 10")

# 14.Take two strings as input and check whether they are equal.

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

if s1 == s2:
    print("Equal")
else:
    print("Not equal")

# 15.Take a number as input and check whether it is greater than 100.

num = int(input("Enter number: "))

if num > 100:
    print("Greater than 100")
else:
    print("Not greater than 100")

# 16.Take a person's age as input and check whether the person is a senior citizen. (Age ≥ 60)

age = int(input("Enter age: "))

if age >= 60:
    print("Senior citizen")
else:
    print("Not a senior citizen")

# 17.Create a predefined password. Take a password as input from the user and check whether it matches.

pre = "abc123"

password = input("Enter password: ")

if pre == password:
    print("Matches")
else:
    print("Not Matches")

# or

password = input("Enter password: ")

if password == "python123":
    print("Login Successful")
else:
    print("Incorrect Password")

# 18.Take a number as input and print:
# Positive
# Negative
# Zero

num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 19.Take the age of a person as input and check whether the person is eligible for a driving license. (Age ≥ 18)

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for a driving license")
else:
    print("Not eligible for a driving license")

# 20.Take a salary as input and check whether it is greater than ₹50,000.

salary = int(input("Enter salary: "))

if salary > 50000:
    print("Greater than 50000")
else:
    print("Not greater than 50000")