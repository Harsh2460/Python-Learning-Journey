# Medium Level Practice Questions

# 1. Student Information Dictionary
# Take the following details from the user:
# Name
# Age
# Course
# City
# Store them in a dictionary and display:
# Complete dictionary
# All keys
# All values
# Total number of key-value pairs

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
city = input("Enter city: ")

student = {
    "Name": name,
    "Age": age,
    "Course": course,
    "City": city
}

print("Dictionary:",student)
print("Keys:",student.keys())
print("Values:",student.values())
print("Length:",len(student))

# 2. Employee Record
# Create a dictionary of an employee. Then:
# Update the salary
# Add the department
# Display the updated dictionary

emp = {
    "name": "Sohan",
    "age": 28,
    "salary": 70000
}

emp.update({"salary": 100000})
emp.update({"department": "HR"})

print("Final dictionary:",emp)

# 3. Dictionary Methods Practice
# Create a dictionary of five students and their marks. Display:
# Keys
# Values
# Items
# Marks of one student using get()

marks = {
    "Rohan": 90,
    "Sumit": 92,
    "Amit": 88,
    "Mohan": 84,
    "Sohan": 91
}

print("Keys:",marks.keys())
print("Values:",marks.values())
print("Items:",marks.items())
print("Marks:",marks.get("Sumit"))

# 4. Dictionary Copy and Clear
# Create a dictionary, make its copy using copy(), then clear the original dictionary and print both dictionaries.

emp = {
    "name": "Sohan",
    "age": 28,
    "salary": 70000
}

new_emp = emp.copy()

emp.clear()

print("Original:",emp)
print("Copy:",new_emp)

# 5. setdefault() Practice
# Create a dictionary of student details. Use setdefault() to:
# Add a new key if it doesn't exist
# Display the updated dictionary

student = {
    "name": "Kuldeep",
    "class": 8,
    "rollno": 10
}

student.setdefault("hobby","Cricket")
print("Updated:",student)

# 6. Fruit Price Dictionary
# Take the names and prices of three fruits as input from the user. Store them in a dictionary and display:
# Dictionary
# Fruit names
# Prices
# Total number of fruits

# Method 1

fruits = {}

name = input("Enter name: ")
price = int(input("Enter price: "))
fruits.update({name: price})

name = input("Enter name: ")
price = int(input("Enter price: "))
fruits.update({name: price})

name = input("Enter name: ")
price = int(input("Enter price: "))
fruits.update({name: price})

print("Dictionary:",fruits)
print("Fruits:",fruits.keys())
print("Prices:",fruits.values())
print("Length:",len(fruits))

# Method 2

fruit1 = input("Enter fruit 1: ")
price1 = int(input("Enter price: "))

fruit2 = input("Enter fruit 2: ")
price2 = int(input("Enter price: "))

fruit3 = input("Enter fruit 3: ")
price3 = int(input("Enter price: "))

fruits = {
    fruit1: price1,
    fruit2: price2,
    fruit3: price3
}

print(fruits)
print(fruits.keys())
print(fruits.values())
print(len(fruits))

# 7. Set Creation
# Take five numbers as input from the user and store them in a set. Display:
# Original set
# Length of the set
# Maximum value
# Minimum value

s = set()

s.add(int(input("Enter number: ")))
s.add(int(input("Enter number: ")))
s.add(int(input("Enter number: ")))
s.add(int(input("Enter number: ")))
s.add(int(input("Enter number: ")))

print("Original:",s)
print("Length:",len(s))
print("Maximum:",max(s))
print("Minimum:",min(s))

# 8. Set Operations
# Create two sets and perform:
# Union
# Intersection
# Difference
# Copy of the first set

s1 = {1,2,3,4}
s2 = {5,2,6,4}

print("Union:",s1.union(s2))
print("Intersection:",s1.intersection(s2))
print("Difference:",s1.difference(s2))

print("Copy:",s1.copy())
# or
new_s1 = s1.copy()
print("Copy:",new_s1)

# 9. Set Methods Practice
# Create a set of numbers. Then:
# Add a new element
# Update with another set
# Remove an element
# Discard another element
# Display the final set

s = {1,2,3,4,5,6,7,8}

s.add(10)
s.update({9,12})
s.remove(4)
s.discard(100)

print("Final:",s)

# 10. Remove Duplicate Values
# Take a list containing duplicate values and convert it into a set. Print both the list and the set.

l = [1,2,2,4,5,3,2,3]

s = set(l)

print("List:",l)
print("Set:",s)

# 11. Check Membership
# Take a number as input from the user and check whether it exists in a set.

numbers = {10,20,30,40,50}

num = int(input("Enter the num: "))

print("Membership:",num in numbers)

# 12. Subset and Superset
# Create two sets and check:
# Whether the first set is a subset of the second
# Whether the second set is a superset of the first

s1 = {1,2}
s2 = {3,4,1,2}

print("Subset:",s1.issubset(s2))
print("Superset:",s2.issuperset(s1))

# 13. Disjoint Sets
# Create two sets and check whether they are disjoint using isdisjoint().

s1 = {1,2}
s2 = {3,4}

print("Disjoint:",s1.isdisjoint(s2))

# 14. Mini Dictionary Project
# Create a dictionary of five books and their authors. Display:
# Dictionary
# Keys
# Values
# Items
# Length of the dictionary
# Remove one book using pop()

books = {
    "Python":"Guido",
    "Java":"James",
    "C":"Dennis",
    "HTML":"Tim",
    "SQL":"Donald"
}

print("Dictionary:",books)
print("Keys:",books.keys())
print("Values:",books.values())
print("Items:",books.items())
print("Length:",len(books))

books.pop("C")
print("Pop:",books)

# 15. Mini Dictionary and Set Project
# Create:
# A dictionary containing student details
# A set containing the student's favorite subjects
# Display:
# Dictionary
# Set
# Dictionary keys
# Dictionary values
# Length of dictionary
# Length of set
# Add a new subject to the set
# Update the dictionary with one new key-value pair

students = {
    "name": "Rohan",
    "class": 8,
}

s = {"Hindi","Math","English","Politics"}

print("Dictionary:",students)
print("Set:",s)

print("Keys:",students.keys())
print("Values:",students.values())

print("Length dictionary:",len(students))
print("Length set:",len(s))

s.add("Geography")
print("Add:",s)

students.update({"sec": "A"})
print("Update:",students)