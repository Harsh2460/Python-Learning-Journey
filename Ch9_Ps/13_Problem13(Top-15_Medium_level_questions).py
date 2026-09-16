# Medium Level Practice Questions

# 1.Write a program to read a text file using read() and count the total number of words using split().

with open("poem.txt","r") as f:
    text = f.read()

words = text.split() # In Python, split() is a built-in string method used to break a string into a list of smaller strings (substrings) based on a specified delimiter.

print("Total Words:",len(words))

# 2.Read a file and display:
# Total lines
# Total words
# Total characters
# Use readlines() for counting lines.

with open("poems.txt") as f:
    lines = f.readlines()

with open("poems.txt") as f:
    text = f.read()

print("Total lines:",len(lines))
print("Total words:",len(text.split()))
print("Total Characters:",len(text))

# 3.Read the contents of source.txt and copy them into backup.txt using with open().

with open("source.txt","r") as f:
    content = f.read()

with open("backup.txt","w") as f:
    f.write(content)

print("File copy successfully")

# 4.Take 3 lines from the user and append all three lines to an existing file using a mode.

line1 = input("Enter the sentence 1: ")
line2 = input("Enter the sentence 2: ")
line3 = input("Enter the sentence 3: ")

with open("data.txt","a") as f:
    f.write(line1 + "\n")
    f.write(line2 + "\n")
    f.write(line3 + "\n")

print("Lines appened succesfully")

# 5.Use readline() repeatedly to read a file and display every line.

with open("blog.txt","r") as f:
    line = f.readline()

    while line:
        print(line,end="")
        line = f.readline()

# 6.Take a word from the user and check whether that word exists in a text file.
# Example:
# Enter word: Python
# Output: Word Found

with open("blog.txt") as f:
    data = f.read()

if "Python" in data:
    print("Word Found")
else:
    print("Word not Found")

# 7.Read a file, replace one word with another, and save the updated content back into the same file.
# Example:
# Old word: Java
# New word: Python

old = input("Enter old word: ")
new = input("Enter new word: ")

with open("blog.txt","r") as f:
    text = f.read()

new_text = text.replace(old,new)

with open("Blog.txt","w") as f:
    f.write(new_text)

print("Replace word successfully")

# 8.Take a word from the user and count how many times it occurs in a text file.

word = input("Enter the word: ")

with open("blog.txt","r") as f:
    data = f.read()

new_data = data.count(word)

print("Occurrence:",new_data)

# 9.Read a file using readlines() and display only the lines that are not empty.

with open("hello.txt","r") as f:
    lines = f.readlines()

for line in lines:
    if line.strip() != "":
        print(line,end="")

# 10.Take the following details from the user:
# Name
# Course
# Age
# Marks
# Store them in student.txt in a properly formatted manner.

name = input("Enter name: ")
course = input("Enter course: ")
age = input("Enter age: ")
marks = input("Enter marks: ")

with open("students.txt","w") as f:
    f.write("Name: " + name + "\n")
    f.write("Course: " + course + "\n")
    f.write("Age: " + age + "\n")
    f.write("Marks: " + marks + "\n")

print("Store student details successfully")

# 11.Read students.txt and display the complete student information stored in the file.

with open("students.txt") as f:
    info = f.read()

print("Student Records:")
print(info)

# 12.Take student name and marks as input and append the record to marks.txt.
# Example format:
# Rahul - 85
# Aman - 91
# Kanha - 88

name = input("Enter name: ")
marks = input("Enter marks: ")

with open("marks.txt","a") as f:
    f.write(name + " - " + marks + "\n")

print("Record append successfully")

# 13.Create a file containing numbers, read them from the file, and find the largest number.
# Example file:
# 10
# 45
# 23
# 78
# 32
# Output:
# Largest = 78

with open("numbers.txt") as f:
    data = f.readlines()

numbers = []
for line in data:
    numbers.append(int(line))

largest = max(numbers)
print("Largest =",largest)

# 14.Read numbers from a file and create two files:
# even.txt → contains even numbers
# odd.txt → contains odd numbers
# Example:
# Input file:
# 10
# 15
# 22
# 31
# 40

with open("nums.txt") as f:
    data = f.readlines()

with open("even.txt","w") as even_file:
    with open("odd.txt","w") as odd_file:

        for line in data:
            num = int(line)

            if num % 2 == 0:
                even_file.write(str(num) + "\n")
            else:
                odd_file.write(str(num) + "\n")

print("Creates file sucessfully")

# 15.Write a program that reads a text file and displays:
# Total Lines = ?
# Total Words = ?
# Total Characters = ?
# Also take a word from the user and display its number of occurrences in the file.

word = input("Enter the occurrence of word: ")

with open("h.txt","r") as f:
    lines = f.readlines()

with open("h.txt","r") as f:
    content = f.read()

print("Total Lines =",len(lines))
print("Total Words =",len(content.split()))
print("Total Characters =",len(content))
print("Occurrence of word =",content.count(word))