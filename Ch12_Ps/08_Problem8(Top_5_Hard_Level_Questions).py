# Hard Level Practice Questions

# 1. Student Performance Analyzer
# Create a program that:
# Takes student names and marks from the user.
# Uses Dict[str, int] type hints.
# Validates marks using try-except.
# Uses the walrus operator := to check the number of students.
# Uses list comprehension to find students with marks ≥ 85.
# Uses enumerate() to display selected students with ranking numbers.
# Uses | to merge two student dictionaries.

from typing import Dict

student1: Dict[str,int] = {}
student2: Dict[str,int] = {}

try:
    n1 = int(input("Enter the number of students in group 1: "))

    for i in range(n1):
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))

        if 0 <= marks <= 100:
            student1[name] = marks
        else:
            raise ValueError("Marks must be between 0 and 100")

    n2 = int(input("\nEnter the number of students in group 2: "))

    for i in range(n2):
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))

        if 0 <= marks <= 100:
            student2[name] = marks
        else:
            raise ValueError("Marks must be between 0 and 100")

    students = student1 | student2

    if (length := len(students)) > 0:
        print("\nNumber of students:",length)

    selected = [name for name,marks in students.items() if marks >= 85]

    print("\nStudents with marks >= 85:")

    for number,name in enumerate(selected,start=1):
        print(number, name, "-", students[name])

except ValueError as v:
    print("Error:",v)

# 2. Advanced Calculator
# Create a calculator using a function:
# def calculator(a: float, b: float, operator: str) -> float:
# Requirements:
# Use match-case for +, -, *, /, %, and //.
# Handle invalid operators using raise.
# Handle ValueError.
# Handle ZeroDivisionError.
# Use else to display the result when there is no error.
# Use finally to print "Calculation completed".

def calaculator(a: float,b: float,operator: str) -> float:
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "%":
            return a % b
        case "//":
            return a // b
        case _:
            raise ValueError("Invalid opertor")

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    operator = input("Enter operator (+,-,*,/,%,//): ")

    result = calaculator(a,b,operator)

except ValueError as e:
    print("Error:",e)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:",result)

finally:
    print("Calaculation completed")

# 3.File Data Processor
# Create a program that:
# Takes student names and marks from the user.
# Writes the data into two separate files.
# Uses multiple context managers in one with statement.
# Reads both files.
# Combines the data.
# Uses list comprehension to find students who scored ≥ 85.
# Uses enumerate() to display the selected students.
# Handles file errors using try-except.

try:
    name1 = input("Enter name of student 1: ")
    marks1 = input("Enter marks of student 1: ")

    name2 = input("Enter name of student 2: ")
    marks2 = input("Enter marks of student 2: ")

    with (
        open("stu1.txt","w") as f1,
        open("stu2.txt","w") as f2
    ):
        f1.write(name1 + "," + marks1)
        f2.write(name2 + "," + marks2)

    with (
        open("stu1.txt","r") as f1,
        open("stu2.txt","r") as f2
    ):
        data1 = f1.read()
        data2 = f2.read()

    students = [data1, data2]

    l = [student for student in students if int(student.split(",")[1]) >= 85]

    print("\nStudents with marks >= 85:")

    for number,student in enumerate(l,start=1):
        name,marks = student.split(",")
        print(number, name, "-", marks)

except (OSError,ValueError) as e:
    print("Error:",e)

# 4. Global Counter + __name__
# Create a program containing:
# count = 0
# Create a function process_numbers() that:
# Uses global count.
# Takes a list of numbers.
# Uses list comprehension to create a list of squares.
# Increases count for every processed number.
# Uses the walrus operator to store the length of the list.
# Uses if __name__ == "__main__": to execute the main program.
# Display:
# Original numbers
# Squared numbers
# Number of elements
# Final counter value

count = 0

def process_numbers(numbers):
    global count

    square = [i*i for i in numbers]

    for number in numbers:
        count += 1

    if (length := len(numbers)) > 0:
        print("\nNumber of elements:",length)

        print("Original numbers:",numbers)
        print("Squared numbers:",square)

if __name__ == "__main__":
    numbers = list(map(int,input("Enter the numbers: ").split()))

    process_numbers(numbers)

    print("Final count:",count)

# 5. Complete Student Management System
# Create a mini Student Management System.
# Requirements:
# Store student data using:
# Dict[str, int]
# Take data for two groups of students.
# Merge both dictionaries using |.
# If the same student exists in both dictionaries, the second group's marks should replace the first.
# Validate marks from 0–100 using try-except.
# Use list comprehension to find:
# Students who passed (>= 40)
# Students who scored distinction (>= 75)
# Use enumerate() to display students with numbering.
# Use the walrus operator to store the total number of students.
# Use match-case to create a menu:
# 1. Show all students
# 2. Show passed students
# 3. Show distinction students
# 4. Exit
# Use finally to display:
# Program completed
# Use:
# if __name__ == "__main__":
# to start the program.

from typing import Dict

def add_students() -> Dict[str,int]:
    students: Dict[str,int] = {}

    try:
        n = int(input("Enter number of students: "))

        for i in range(n):
            name = input("Enter the name: ")
            marks = int(input("Enter the marks: "))

            if 0 <= marks <= 100:
                students[name] = marks
            else:
                raise ValueError("Marks must be between 0 and 100")

    except ValueError as e:
        print("Error:",e)

    return students

def show_student(students):
    print("\nAll Students:")

    for number, (name,marks) in enumerate(students.items(),start=1):
        print(number, name, "-", marks)

def show_passed(students):
    passed = [(name,marks) for name,marks in students.items() if marks >= 40]

    print("\nPassed Students:")

    for number, (name,marks) in enumerate(passed,start=1):
        print(number, name, "-", marks)

def show_distinction(students):
    distinction = [(name,marks) for name,marks in students.items() if marks >= 75]

    print("\nDistinction Students:")

    for number, (name,marks) in enumerate(distinction,start=1):
        print(number, name, "-", marks)

def main():
    print("GROUP 1")
    student1 = add_students()

    print("\nGROUP 2")
    student2 = add_students()

    students = student1 | student2

    if (length := len(students)) > 0:
        print("\nTotal Students:",length)

    while True:           # while True creates an infinite loop that keeps the menu active until the user explicitly chooses to exit.
        print("\n--- Menu ---")
        print("1.Show all students")
        print("2.Show passed students")
        print("3.Show distinction students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                show_student(students)
            case "2":
                show_passed(students)
            case "3":
                show_distinction(students)
            case "4":
                print("Exiting program....")
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print("Unexpected error:",e)

    finally:
        print("Program Completed")