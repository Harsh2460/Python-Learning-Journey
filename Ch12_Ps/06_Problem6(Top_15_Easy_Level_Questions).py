# Easy Level Practice Questions      

# 1.Take a list of numbers and use the walrus operator := to store its length inside an if condition. Print the length if it is greater than 5.

l = [10,20,30,40,50,60]

if (length := len(l)) > 5:
    print("List is large")
    print("Length:",length)
else:
    print("List is small")

# 2.Create a function add() that takes two integers and returns their sum. Use type hints for parameters and return type.

def add(a: int,b: int) -> int:
    return a + b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Sum=",add(a,b))

# 3.Create a list of integers using List[int] and write a function that returns the sum of all numbers.

from typing import List

def calaculate_sum(numbers: List[int]) -> int:
    return sum(numbers)

numbers = list(map(int,input("Enter numbers: ").split()))

print("Sum:",calaculate_sum(numbers))

# 4.Create a dictionary containing student names and marks using Dict[str, int]. Print the name and marks of each student.

from typing import Dict

students: Dict[str,int] = {
    "Rahul": 90,
    "Deepak": 88,
    "Rohan":92
}

for name,marks in students.items():
    print(name, ":", marks)

# 5.Create a tuple containing a person's name and age using:
# Tuple[str, int]

from typing import Tuple

def get_person() -> Tuple[str,int]:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    return name,age

person = get_person()

print("Name:",person[0])
print("Age:",person[1])

# 6.Take a number from 1 to 7 and use match-case to print the corresponding day.
# Example:
# 1 → Monday
# 2 → Tuesday

day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")

# 7.Take two numbers and an operator (+, -, *, /) from the user. Use match-case to perform the calculation.

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
opertor = input("Enter operator(+,-,*,/): ")

match opertor:
    case "+":
        print("Result=",n1 + n2)
    case "-":
        print("Result=",n1 - n2)
    case "*":
        print("Result=",n1 * n2)
    case "/":
        print("Result=",n1 / n2)
    case _:
        print("Invalid Opertor")

# 8.Create two dictionaries and merge them using the | operator.
# Example:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1 | dict2
print("Merged Dictionary:",merged)

# 9.Create a dictionary and update it using the |= operator.
# Example:
# student = {"name": "Rahul", "marks": 80}
# Update the marks and add a new key.

student = {
    "name": "Rahul",
    "marks": 80
}

new_data = {
    "marks": 92,
    "course": "BA"
}

student |= new_data

print("Updated Dictionary:",student)

# 10.Create two text files using a single with statement and write different messages into both files.

message1 = input("Enter the message for file 1: ")
message2 = input("Enter the message for file 2: ")

with (
    open("file1.txt","w") as f1,
    open("file2.txt","w") as f2
):
    f1.write(message1)
    f2.write(message2)

print("Data written successfully")

# 11.Take two numbers from the user and divide them. Handle the ZeroDivisionError using try-except.

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b
    print("Result=",result)

except ZeroDivisionError:
    print("Cannot divide by zero")

# 12.Take two values from the user and perform division. Handle:
# ValueError
# ZeroDivisionError
# using separate except blocks.

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b
    print("Result:",result)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

# 13.Take a number from the user and convert it into an integer.
# Use:
# try → conversion
# except → handle invalid input
# else → print successful conversion
# finally → print "Program completed"

try:
    n = int(input("Enter the number: "))

except ValueError:
    print("Invalid input")

else:
    print("Conversion Successful:",n)

finally:
    print("Program Completed")

# 14.Create a list of 5 student names and use enumerate() to print each student's index and name.
# Expected format:
# 0 Sumit
# 1 Rahul
# 2 Aman
# ...

l = ["Sumit","Rahul","Aman","Tushar","Kunal"]

for index,name in enumerate(l):
    print(index, name)

# 15.Given a list:
# numbers = [1, 7, 12, 11, 22, 5, 30]
# Use list comprehension to create a new list containing only numbers greater than 10.
# Expected output:
# [12, 11, 22, 30]

numbers = [1, 7, 12, 11, 22, 5, 30]

new_numbers = [i for i in numbers if i > 10]
print("Number greater than 10:",new_numbers)