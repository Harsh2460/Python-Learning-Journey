# Medium Level Practice Questions

# 1.Take numbers from the user and use the walrus operator to store the length of the list. Then use list comprehension to create a list containing only even numbers.

numbers = list(map(int,input("Enter the numbers: ").split()))

if (length := len(numbers)) > 0:
    print("Length:",length)

    new_list = [i for i in numbers if i % 2 == 0]
    print("Even numbers list:",new_list)

else:
    print("List is empty")

# 2.Create a function:
# def find_even(numbers: List[int]) -> List[int]:
# The function should return all even numbers from the given list.

from typing import List

def find_even(numbers: List[int]) -> List[int]:
    return [i for i in numbers if i % 2 == 0]

numbers = list(map(int,input("Enter the numbers: ").split()))

result = find_even(numbers)

print("Even numbers:",result)

# 3.Create a calculator function that accepts two numbers and an operator.
# Use match-case for:
# +
# -
# *
# /
# %
# Handle division/modulus by zero using exception handling.

def calculator(a: float,b: float,op: str) -> float:
    match op:
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
        case _:
            raise ValueError("Invalid Operator")

try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    op = input("Enter operator (+,-,*,/,%): ")

    result = calculator(a,b,op)
    print("Result:",result)

except ValueError as v:
    print("Error:",v)

except ZeroDivisionError:
    print("Cannot divide by zero")

# 4.Create two dictionaries containing student names and marks.
# Merge them using |.
# Then use list comprehension to create a list containing students whose marks are greater than or equal to 90.

student1 = {
    "Umar": 88,
    "Suresh": 90,
    "Tina": 86
}

student2 = {
    "Kunal": 82,
    "Sohan": 94,
    "Rakesh": 85
}

new_students = student1 | student2

l = [name for name,marks in new_students.items() if marks >= 90]

print("Merged:",new_students)
print("Marks greater than or equal to 90:",l)

# 5.Create a program that takes two numbers and divides them.
# Use:
# try → division
# except → handle ValueError and ZeroDivisionError
# else → print the result if successful
# finally → print "Calculation completed"

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:",result) 

finally:
    print("Calculation completed")

# 6.Take 5 student names from the user.
# Use enumerate() to display each student's number and name, but create the output list using list comprehension.
# Example:
# 1. Kunal
# 2. Rahul
# 3. Aman

students = []
for i in range(5):
    n = input(f"Enter the student {i + 1} name: ")
    students.append(n)

l = [f"{i + 1}. {name}" for i,name in enumerate(students)]

print("\nStudents:")

for student in l:
    print(student)

# 7.Open two files using a single with statement.
# Take messages from the user and write them into the two files. Handle any file-related exception using try-except.

try:
    message1 = input("Enter the meassage 1: ")
    message2 = input("Enter the meassage 2: ")

    with (
        open("text1.txt","w") as f1,
        open("text2.txt","w") as f2
    ):
        f1.write(message1)
        f2.write(message2)

        print("Data written successfully")

except OSError:
    print("File error occurred")

# 8.Create a global variable:
# count = 0
# Create a function increase_count() that uses the global keyword to increase the value by 1.
# Call the function 5 times and display the final value.

count = 0

def increase_count():
    global count
    count += 1

for i in range(5):
    increase_count()

print("Final count:",count)

# 9.Create a program with:
# def square(n):
#     return n * n
# Use:
# if __name__ == "__main__":
# to take input from the user and call the function.

def square(n):
    return n * n

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print("Square:",square(n))

# 10.Create a program that:
# Takes student names and marks.
# Stores them in a dictionary.
# Uses type hints such as Dict[str, int].
# Uses dictionary merge | to combine two student dictionaries.
# Uses list comprehension to find students with marks ≥ 85.
# Uses enumerate() to display the selected students with numbers.
# Uses try-except to handle invalid marks.

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

    l = [name for name,marks in students.items() if marks >= 85]

    print("\nAll Students:")
    print(students)

    print("\nStudents with marks >= 85:")

    for number,name in enumerate(l,start=1):
        print(number, name)

except ValueError as v:
    print("Error:",v)