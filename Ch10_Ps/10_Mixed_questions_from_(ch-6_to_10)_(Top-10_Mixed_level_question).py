# Mixed Practice Questions

# 1.Write a function check_number(n) that:
# Takes a number as input.
# Checks whether it is even or odd.
# Returns the result.

def check_number(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
n = int(input("Enter the number: "))

result = check_number(n)

print("Number is =",result)

# 2.Take a number n from the user and print all prime numbers from 1 to n.
# Example:
# Input: 20
# Output: 2 3 5 7 11 13 17 19

n = int(input("Enter the number: "))

print("Prime Numbers:")

for i in range(2,n+1):
    count = 0

    for j in range(1,i+1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(i,end=" ")

# 3.Create a function that accepts marks of 5 subjects and calculates:
# Total marks
# Percentage
# Grade
# Use:
# 90+ → A
# 75–89 → B
# 60–74 → C
# 40–59 → D
# Below 40 → F

def student_marks(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else: 
        grade = "F"

    return total,percentage,grade

marks = []

for i in range(5):
    mark = int(input(f"Enter the marks of subject {i + 1}: "))
    marks.append(mark)

total,percentage,grade = student_marks(marks)

print("Total:",total)
print("Perctange:",percentage)
print("Grade:",grade)

# 4.Take numbers from the user and create a new list containing only unique values.
# Example:
# Input: 10 20 10 30 20 40
# Output: [10, 20, 30, 40]

numbers = list(map(int, input("Enter numbers separte by spaces : ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Unique list:", unique)

# 5.Take a sentence from the user and create a dictionary containing the number of times each word occurs.
# Example:
# Input: python is easy python is powerful
# Output:
# {'python': 2, 'is': 2, 'easy': 1, 'powerful': 1}

s = input("Enter the sentence: ")

words = s.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print("Word Count:",count)

# 6.Create a recursive function factorial(n) that calculates the factorial of a number.
# Example:
# Input: 5
# Output: 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number: "))

result = factorial(n)
print("Factorial:",result)

# 7.Create a program that:
# Takes student name and marks from the user.
# Writes the information into students.txt.
# Reads the file.
# Displays the stored information.

name = input("Enter the name: ")
marks = input("Enter the marks: ")

with open("students.txt","w") as f:
    f.write("Name: "+ name + "\n")
    f.write("Marks: "+ marks + "\n")

with open("students.txt") as f:
    data = f.read()

print("\nStudent Record:")
print(data)

# 8.Create a program that reads a text file and counts:
# Number of lines
# Number of words
# Number of characters

with open("students.txt","r") as f:
    lines = f.readlines()

with open("students.txt","r") as f:
    content = f.read()

print("Number of lines:",len(lines))
print("Number of words:",len(content.split()))
print("Number of characters:",len(content))

# 9.Create a Student class with:
# name
# marks
# Add methods:
# display() → displays student details
# percentage() → calculates percentage
# Take marks of 5 subjects using a list.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)

    def percentage(self):
        total = sum(self.marks)
        return total / len(self.marks)

name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = int(input(f"Enter the marks of subject {i + 1}: "))
    marks.append(mark)


s = Student(name,marks)

s.display()
print("Percentage:",s.percentage())

# 10.Create an Employee class with:
# name
# salary
# department
# Add methods:
# display()
# is_high_salary() → returns "Yes" if salary ≥ 50,000, otherwise "No"
# Create multiple employee objects and display their information.

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def dispaly(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)

    def is_high_salary(self):
        if self.salary >= 50000:
            return "Yes"
        else:
            return "No"

name = input("Enter the name: ")
salary = int(input("Enter the salary: "))
department = input("Enter the department: ")

e = Employee(name,salary,department)

e.dispaly()
print("High Salary:",e.is_high_salary())