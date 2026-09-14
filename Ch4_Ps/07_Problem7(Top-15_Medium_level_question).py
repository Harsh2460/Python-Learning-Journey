# Medium Level Practice Questions

# 1. Student Marks List
# Take five marks as input from the user, store them in a list, and print:
# The complete list
# Highest mark
# Lowest mark
# Total marks
# Average marks

list = []

m1 = int(input("Enter the Marks: "))
list.append(m1)
m2 = int(input("Enter the Marks: "))
list.append(m2)
m3 = int(input("Enter the Marks: "))
list.append(m3)
m4 = int(input("Enter the Marks: "))
list.append(m4)
m5 = int(input("Enter the Marks: "))
list.append(m5)

print("Complete list:",list)
print("Highest Mark:",max(list))
print("Lowest Mark:",min(list))

total = sum(list)
print("Total Marks:",total)

average = total / 5
print("Average Marks",average)

# Second method

marks = []

marks.append(int(input("Enter mark 1: ")))
marks.append(int(input("Enter mark 2: ")))
marks.append(int(input("Enter mark 3: ")))
marks.append(int(input("Enter mark 4: ")))
marks.append(int(input("Enter mark 5: ")))

print("Marks:",marks)
print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Total:",sum(marks))
print("Average:",sum(marks)/len(marks))

# 2. Favorite Fruits
# Take four fruit names as input from the user and store them in a list. Then:
# Print the list
# Sort the list alphabetically
# Reverse the sorted list

fruits = []

fruits.append(input("Enter fruit 1: "))
fruits.append(input("Enter fruit 2: "))
fruits.append(input("Enter fruit 3: "))
fruits.append(input("Enter fruit 4: "))

print("Original List:",fruits)

fruits.sort()
print("Sorted List:",fruits)

fruits.reverse()
print("Reverse List:",fruits)

# 3. Even Numbers List
# Create a list containing the first ten even numbers and print:
# First three elements
# Last three elements
# Every second element

numbers = [2,4,6,8,10,12,14,16,18,20]

print("First 3 elements:",numbers[:3])
print("Last 3 elements:",numbers[-3:])
print("Every second elements:",numbers[::2])

# 4. List Operations
# Create two lists of five numbers each and perform:
# Concatenation
# Repetition of the first list twice
# Check whether a number entered by the user exists in the first list

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

user = int(input("Enter the number: "))

print("Concatenation:",l1 + l2)
print("Repetition:",l1 * 2)
print("Membership:",user in l1)

# 5. Shopping List
# Create a shopping list with five items. Then:
# Add one new item using append()
# Insert one item at index 2
# Remove one item using remove()
# Print the final list

shopping = ["Rin","Goodday","Kit-Kate","Namkeen","Surf-excel"]

shopping.append("Ketchup")
shopping.insert(2,"Taka-Tak")
shopping.remove("Goodday")

print("Final list:",shopping)

# 6. Employee Salary List
# Create a list of five employee salaries and print:
# Maximum salary
# Minimum salary
# Total salary
# Number of employees

emp_sar = [50000,65000,80000,75000,90000]

print("Maximum:",max(emp_sar))
print("Minimum:",min(emp_sar))
print("Total:",sum(emp_sar))
print("Length:",len(emp_sar))

# 7. Find Element Position
# Create a list of colors. Take a color name as input and print its index using the index() method.

colors = ["Red","Green","White","Yellow","Pink"]

a = colors.index(input("Enter color name: "))
print(a)

# # Second method

colors = ["Red","Green","White","Yellow","Pink"]

a = input("Enter color name: ")
print(colors.index(a))

# 8. Count an Element
# Create a list containing duplicate values. Take a number as input and print how many times it appears in the list using count().

values = [1,2,3,4,2,6,7,2,8,9,2]

num = int(input("Enter number: "))
print("Counts:",values.count(num))

# 9. Tuple Operations
# Create a tuple of six numbers and print:
# First element
# Last element
# Middle three elements
# Length of the tuple
# Maximum value
# Minimum value
# Sum of all elements

numbers = (10,20,30,40,50,60)

print("First element:",numbers[0])
print("Last element:",numbers[-1])
print("Middle elements:",numbers[2:5])
print("Length:",len(numbers))
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))
print("Sum:",sum(numbers))

# 10. Tuple Membership
# Create a tuple of five cities. Take a city name as input and check whether it exists in the tuple using the membership operator (in).

cities = ("Kanpur","Lucknow","Delhi","Mumbai","Bihar")

c_name = input("Enter city: ")
print("Membership:",c_name in cities)

# 11. Tuple Concatenation and Repetition
# Create two tuples and:
# Concatenate them
# Repeat the first tuple three times

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)

print("Concatenate:",t1 + t2)
print("Repetition:",t1 * 3)

# 12. List Slicing Practice
# Create a list of numbers from 1 to 15 and print:
# First five elements
# Last five elements
# Elements from index 3 to 10
# Every second element

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("First five:",num[:5])
print("Last five:",num[-5:])
print("Indexing:",num[3:11])
print("Every second:",num[::2])

# 13. Class Students List
# Take the names of four students as input from the user and:
# Store them in a list
# Sort the list
# Print the sorted list
# Print the number of students

students = []

students.append(input("Enter Student 1: "))
students.append(input("Enter Student 2: "))
students.append(input("Enter Student 3: "))
students.append(input("Enter Student 4: "))

students.sort()
print("Sorted:",students)

print("Length:",len(students))

# 14. Mini List Project
# Take five numbers as input from the user and perform:
# Sort the list
# Reverse the list
# Find the largest number
# Find the smallest number
# Calculate the sum of all numbers

numbers = []

numbers.append(int(input("Enter the number 1: ")))
numbers.append(int(input("Enter the number 2: ")))
numbers.append(int(input("Enter the number 3: ")))
numbers.append(int(input("Enter the number 4: ")))
numbers.append(int(input("Enter the number 5: ")))

numbers.sort()
print("Sorted:",numbers)

numbers.reverse()
print("Reversed:",numbers)

print("Largest:",max(numbers))
print("Smallest:",min(numbers))
print("Sum:",sum(numbers))

# 15. List and Tuple Comparison
# Create:
# A list of five numbers
# A tuple of the same five numbers
# Print:
# The list
# The tuple
# Length of both
# Maximum value in both
# Minimum value in both
# Sum of elements in both

l = [10,20,30,40,50]
t = (10,20,30,40,50)

print("List:",l)
print("Tuple:",t)

print("Length of list:",len(l))
print("Length of tuple:",len(t))

print("Maximum of list:",max(l))
print("Maximum of tuple:",max(t))

print("Minimum of list:",min(l))
print("Minimum of tuple:",min(t))

print("Sum of list:",sum(l))
print("Sum of tuple:",sum(t))
