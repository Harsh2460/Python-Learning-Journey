# Hard Level Practice Questions

# 1. Student Record Management System
# Take the following details from the user:
# Name
# Age
# Course
# City
# Marks
# Store them in a dictionary and perform the following operations:
# Display the dictionary
# Display all keys
# Display all values
# Display all items
# Display the total number of key-value pairs
# Add a new key "College" using update()
# Add a new key "State" using setdefault()
# Remove "Marks" using pop()
# Create a copy of the dictionary

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
city = input("Enter city: ")
marks = int(input("Enter marks: "))

d = {
    "Name": name,
    "Age": age,
    "Course": course,
    "City": city,
    "Marks": marks
}

print("Dictionary:",d)
print("Keys:",d.keys())
print("Values:",d.values())
print("Items:",d.items())
print("Length:",len(d))

d.update({"College": "IIT Indore"})
print("Updated:",d)

d.setdefault("State","MP")
print("Setdefault:",d)

d.pop("Marks")
print("Pop:",d)

new_c = d.copy()
print("Copy:",new_c)

# 2. Dictionary and Set Project
# Take five favorite subjects from the user.
# Store:
# Subject names as dictionary keys with values "Available"
# Subject names in a set
# Display:
# Dictionary
# Set
# Dictionary keys
# Dictionary values
# Dictionary items
# Length of dictionary
# Length of set
# Add one new subject to the set
# Update the dictionary with one new subject
# Create copies of both dictionary and set

sub1 = input("Enter subject 1: ")
sub2 = input("Enter subject 2: ")
sub3 = input("Enter subject 3: ")
sub4 = input("Enter subject 4: ")
sub5 = input("Enter subject 5: ")

d = {
    sub1: "Available",
    sub2: "Available",
    sub3: "Available",
    sub4: "Available",
    sub5: "Available"
}

sub_set = {sub1,sub2,sub3,sub4,sub5}

print("Dictionary:",d)
print("Set:",sub_set)
print("Keys:",d.keys())
print("Values:",d.values())
print("Items:",d.items())

print("Length dictionary:",len(d))
print("Length set:",len(sub_set))

sub_set.add("Geography")
print("Add:",sub_set)

d.update({"PS": "Available"})
print("Update:",d)

new_d = d.copy()
print("Copy Dictionary:",new_d)

new_s = sub_set.copy()
print("Copy Set:",new_s)

# 3. Advanced Set Operations
# Create two sets of numbers and perform the following:
# Union
# Intersection
# Difference (set1 - set2)
# Difference (set2 - set1)
# Copy of the first set
# Add one element
# Update with another set
# Remove one element
# Discard one element
# Check whether the first set is a subset of the second
# Check whether the first set is a superset of the second
# Check whether the two sets are disjoint

s1 = {1,3,2,2,5,1}
s2 = {2,3,4,1,6,4}

print("Union:",s1.union(s2))
print("Intersection:",s1.intersection(s2))
print("Difference 1:",s1.difference(s2))
print("Difference 2:",s2.difference(s1))

new_s1 = s1.copy()
print("Copy:",new_s1)

s1.add(8)
print("Add:",s1)

s1.update({9,10})
print("Update:",s1)

s1.remove(3)
print("Remove:",s1)

s1.discard(100)
print("Discard:",s1)

print("Subset:",s1.issubset(s2))
print("Superset:",s1.issuperset(s2))
print("Disjoint:",s1.isdisjoint(s2))

# 4. Employee Database Project
# Create a dictionary containing:
# Employee ID
# Name
# Department
# Salary
# City
# Then perform the following:
# Display all keys
# Display all values
# Display all items
# Update the salary
# Add "Experience" using setdefault()
# Remove "City" using pop()
# Remove the last inserted item using popitem()
# Display the final dictionary
# Create a copy of the dictionary

di = {
    "Employee ID": 101,
    "Name": "Rohit",
    "Department": "IT",
    "Salary": 80000,
    "City": "Delhi"
}

print("Keys:",di.keys())
print("Values:",di.values())
print("Items:",di.items())

di.update({"Salary": 85000})
di.setdefault("Experience","2 Years")
di.pop("City")
di.popitem()

print("Final dictionary:",di)

new_di = di.copy()
print("Copy:",new_di)
# or
print("C:",di.copy())

# 5. Mini Dictionary and Set Report
# Create:
# A dictionary of five books and their prices
# Two sets of book categories
# Perform the following:
# Dictionary
# Display dictionary
# Display keys
# Display values
# Display items
# Length of dictionary
# Update one book price
# Add one new book
# Remove one book
# Create a copy
# Sets
# Display both sets
# Union
# Intersection
# Difference
# Add one category
# Update with another set
# Remove one category
# Discard one category
# Check subset
# Check superset
# Check disjoint
# Create a copy of the first set

books = {
    "Python": 500,
    "Java": 450,
    "C": 300,
    "HTML": 250,
    "SQL": 350
}

set1 = {"Programming", "Database", "Web"}
set2 = {"Database", "Networking", "Cloud"}

print("Dictionary:",books)
print("Keys:",books.keys())
print("Values:",books.values())
print("Items:",books.items())
print("Length:",len(books))

books.update({"HTML": 275})
print("Update:",books)
books.update({"Software": 600})
print("Update 1:",books)
books.pop("C")
print("Pop:",books)

print("Copy:",books.copy())

print("Set 1:",set1)
print("Set 2:",set2)

print("Union:",set1.union(set2))
print("Intersection:",set1.intersection(set2))
print("Difference:",set1.difference(set2))

set1.add("Biographies")
print("Add:",set1)

set1.update({"Fiction", "History"})
print("Update:",set1)

set1.remove("Web")
print("Remove:",set1)

set1.discard("Sci-Fi")
print("Discard:",set1)

print("Subset:",set1.issubset(set2))
print("Superset:",set1.issuperset(set2))
print("Disjoint:",set1.isdisjoint(set2))
print("Copy:",set1.copy())