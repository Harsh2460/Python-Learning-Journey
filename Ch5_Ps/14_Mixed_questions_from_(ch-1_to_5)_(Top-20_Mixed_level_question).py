# These questions combine concepts from all five (1 to 5) chapters.

# 1.Print introduction using variables.

name = input("Enter the name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print("Name:",name)
print("Age:",age)
print("City:",city)

# 2.Take a name as input and print it in uppercase.

name = input("Enter name: ")

print("Uppercase:",name.upper())

# 3.Store five marks in a list and find the highest mark.

l = []

l.append(int(input("Enter marks: ")))
l.append(int(input("Enter marks: ")))
l.append(int(input("Enter marks: ")))
l.append(int(input("Enter marks: ")))
l.append(int(input("Enter marks: ")))

print("Marks:",l)
print("Highest Mark:",max(l))

# 4.Store student details in a dictionary.

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

student = {
    "Name": name,
    "Age": age,
    "City": city
}

print(student)

# 5.Create a set from a list containing duplicate values.

l = [1,2,4,2,5,2,6,2]

s = set(l)

print("List:",l)
print("Set:",s)

# 6.Reverse a string using slicing.

text = input("Enter text: ")

print("Reverse:",text[::-1])

# 7.Find the length of a tuple.

t = (1,2,3,4,5,6)

print("Tuple:",t)
print("Length:",len(t))

# 8.Update a dictionary using update().

d = {
    "name": "Rohan",
    "age": 16
}

d.update({"city": "Kanpur"})
print("Updated:",d)

# 9.Check whether a number exists in a set.

s = {1,2,3,4,5}

c = int(input("Enter number: "))

print("Membership:",c in s)

# 10.Concatenate two lists.

l1 = [1,2,3,4]
l2 = [5,6,7,8]

print("Concatenate:",l1 + l2)

# 11.Replace a word in a string.

sentence = input("Enter sentence: ")
o = input("Enter old word: ")
n = input("Enter new word: ")

print("Updated sentence:",sentence.replace(o,n))

# 12.Count the occurrence of a character in a string.

s = input("Enter String: ")
ch = input("Enter character: ")

print("Count:",s.count(ch))

# 13.Find the index of an element in a tuple.

t = (1,2,3,4,5)

e = int(input("Enter number: "))

print("Indexing:",t.index(e))

# 14.Remove the last item from a dictionary using popitem().

d = {
    "name": "Rohan",
    "age": 16,
    "city": "Kanpur"
}

d.popitem()

print("Remove Last:",d)

# 15.Copy a dictionary and print both.

d = {
    "name": "Rohan",
    "age": 16,
    "city": "Kanpur"
}

new_d = d.copy()

print("Original:",d)
print("Copy:",new_d)

# 16.Perform union and intersection of two sets.

s1 = {1,2,3}
s2 = {4,2,6}

print("Union:",s1.union(s2))
print("Intersection:",s1.intersection(s2))

# 17.Import the math module and calculate the square root of a number.

import math

num = int(input("Enter square root: "))

print("Square Root:",math.sqrt(num))

# 18.Take two numbers as input and perform all arithmetic operations.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("Addition:",a + b)
print("Subtraction:",a - b)
print("Multiplication:",a * b)
print("Division:",a / b)
print("Remainder:",a % b)
print("Power:",a ** b)
print("Floor Division:",a // b)

# 19.Create a list, sort it, and reverse it.

num = []

num.append(int(input("Enter number: ")))
num.append(int(input("Enter number: ")))
num.append(int(input("Enter number: ")))
num.append(int(input("Enter number: ")))
num.append(int(input("Enter number: ")))

print("Original:",num)

num.sort()
print("Sorted:",num)

num.reverse()
print("Reverse:",num)

# 20.Build a mini student record using variables, strings, lists, dictionaries, and sets together.

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

marks = []

marks.append(int(input("Enter marks 1: ")))
marks.append(int(input("Enter marks 2: ")))
marks.append(int(input("Enter marks 3 ")))

student = {
    "Name": name,
    "Age": age,
    "City": city
}

s = {"Histroy","Math","Science"}

print("Student Dictionary:",student)
print("Marks:",marks)
print("Subject:",s)
print("Name in Uppercase:",name.upper())
print("Total marks:",sum(marks))
print("Average marks:",sum(marks) / len(marks))