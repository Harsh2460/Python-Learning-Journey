# Hard Level Practice Questions

# 1. Student Marks Analyzer
# Take five marks as input from the user and store them in a list. Display:
# Original list
# Sorted list
# Reversed list
# Highest mark
# Lowest mark
# Total marks
# Average marks

marks = []

marks.append(int(input("Enter marks 1: ")))
marks.append(int(input("Enter marks 2: ")))
marks.append(int(input("Enter marks 3: ")))
marks.append(int(input("Enter marks 4: ")))
marks.append(int(input("Enter marks 5: ")))

print("Original:",marks)

marks.sort()
print("Sorted:",marks)

marks.reverse()
print("Reverse:",marks)

print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Total:",sum(marks))
print("Average:",sum(marks)/len(marks))

# 2. List Operations Project
# Create two lists of five numbers each. Perform the following operations:
# Concatenate both lists
# Repeat the first list three times
# Find the length of the concatenated list
# Find the maximum, minimum, and sum of the concatenated list
# Check whether a number entered by the user is present in the concatenated list

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

a = int(input("Enter number: "))

con = l1 + l2

print("Concatenate:",con)
print("Repetition:",l1 * 3)
print("Length:",len(con))
print("Maximum:",max(con))
print("Minimum:",min(con))
print("Sum:",sum(con))

print("Membership:",a in con)

# 3. Advanced List Manipulation
# Take five numbers as input from the user and perform the following operations:
# Insert 100 at index 2
# Append 200
# Remove the first occurrence of 100
# Remove the last element using pop()
# Sort the list
# Reverse the list
# Print the final list

numbers = []

numbers.append(int(input("Enter Number 1: ")))
numbers.append(int(input("Enter Number 2: ")))
numbers.append(int(input("Enter Number 3: ")))
numbers.append(int(input("Enter Number 4: ")))
numbers.append(int(input("Enter Number 5: ")))

numbers.insert(2,100)
numbers.append(200)
numbers.remove(100)
numbers.pop()

numbers.sort()
numbers.reverse()

print("Final:",numbers)

# 4. Tuple Operations Project
# Create a tuple of eight numbers and display:
# First four elements
# Last four elements
# Every second element
# Reverse the tuple
# Maximum value
# Minimum value
# Sum of all elements
# Count the occurrences of a number entered by the user
# Find the index of a number entered by the user

t = (1,2,3,4,2,6,7,8)

num = int(input("Enter number: "))

print("First four:",t[:4])
print("Last four:",t[-4:])
print("Every second:",t[::2])

print("Reverse:",t[::-1])
print("Maximum:",max(t))
print("Minimum:",min(t))
print("Sum:",sum(t))
print("Count:",t.count(num))
print("Index:",t.index(num))

# 5. Mini List and Tuple Report
# Create:
# A list of five numbers
# A tuple containing the same elements
# Display the following:
# List
# Tuple
# First element
# Last element
# First three elements
# Last three elements
# Length of both
# Maximum value
# Minimum value
# Sum of elements
# Concatenate the list with another list
# Concatenate the tuple with another tuple
# Repeat both the list and tuple two times
# Check whether a number entered by the user exists in both the list and tuple

l = [1,2,3,4,5]
t = (1,2,3,4,5)

user = int(input("Enter number: "))

print("List:",l)
print("Tuple:",t)

print("First:",l[0])
print("Last:",l[-1])

print("First three:",l[:3])
print("Last three:",l[-3:])

print("Length list:",len(l))
print("Length tuple:",len(t))

print("Maximum:",max(l))
print("Minimum:",min(l))
print("Sum:",sum(l))

print("Concatenate list:",l + [6,7])
print("Concatenate tuple:",t + (6,7))

print("Repetition list:",l * 2)
print("Repetition tuple:",t * 2)

print("Membership list:",user in l)
print("Membership tuple:",user in t)