# Easy Level Practice Questions

# 1.Write a program to open data.txt in read mode and print its complete contents using read().

f = open("data.txt","w")
f.write("Hello World!")
f.close()

f = open("data.txt")
content = f.read()
print(content)
f.close

# 2.Write a program to create hello.txt in write mode and write:
# Hello Python
# Welcome to File Handling

f = open("hello.txt","w")
f.write("Hello Python\n")
f.write("Welcome to File Handling")
f.close()

print("Data written successfully")

# 3.Write a program to read only the first line of hello.txt using readline().

f = open("hello.txt")
content = f.readline()
print(content)
f.close()

# 4.Write a program to read all lines from hello.txt using readlines() and print them.

f = open("hello.txt")
lines = f.readlines()
print(lines)
f.close()

# 5.Write a program to open hello.txt in append mode and add:
# This is Chapter 9
# without deleting the previous content.

f = open("hello.txt","a")
f.write("\nThis is Chapter 9")
f.close()

print("Data appended Successfully")

# 6.Write a program to create a new file student.txt using exclusive creation mode (x).
# Write your name into the file.

name = input("Enter the name: ")

f = open("student.txt","x")
f.write(name)
f.close()

print("File created successfully")

# 7.Write a program using the with open() statement to read and print the contents of data.txt.

with open("data.txt") as f:
    content = f.read()

print(content)

# 8.Write a program using with open() to create notes.txt and write three lines into it.

with open("notes.txt","w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3")

print("File written successfully")

# 9.Read the contents of story.txt and print the total number of characters using len().

with open("story.txt","r") as f:
    content = f.read()

print("Number of Characters: ",len(content))

# 10.Read a file using readlines() and print the total number of lines present.

with open("hello.txt","r") as f:
    lines = f.readlines()

print("Total number of lines are:",len(lines))

# or 

t_lines = 0
for line in lines:
    t_lines += 1

print("Total number of lines are:",t_lines)

# 11.Open poems.txt and print each line one by one using a loop.

with open("poems.txt","r") as f:
    lines = f.readlines()

for line in lines:
    print(line,end="")  # Since line already contains a \n character from the file, using standard print(line) would result in double-spacing (a blank line after each sentence) that why we use end="".

# 12.Read the contents of source.txt and write the same contents into destination.txt.

with open("source.txt","r") as f:
    content = f.read()

with open ("destination.txt","w") as f:
    f.write(content)

print("File copied successfully")

# 13.Take a student's name as input and save it into student.txt using write mode.

name = input("Enter the name: ")

with open("student.txt","w") as f:
    f.write(name)

print("Student name save successfully")

# 14.Take three sentences as input from the user and save them into paragraph.txt.

s1 = input("Enter sentence 1: ")
s2 = input("Enter sentence 2: ")
s3 = input("Enter sentence 3: ")

with open("paragraph.txt","w") as f:
    f.write(s1 + "\n")
    f.write(s2 + "\n")
    f.write(s3)

print("Sentence saved successfully")

# 15.Take a message as input and append it to message.txt.

message = input("Enter message: ")

with open("message.txt","a") as f:
    f.write(message + "\n")

print("Message append successfully")

# 16.Create a file containing:
# Python
# Java
# C++
# Read and display the entire content using read().

with open("text.txt") as f:
    content = f.read()

print(content)

# 17.Write a program that first prints one line using readline() and then prints the remaining lines using readlines().

with open("poems.txt") as f:
    line1 = f.readline()
    r_lines = f.readlines()

print("First line:",line1,end="")
print("Remaining Lines:")
print(r_lines)

# 18.Create daily_notes.txt and write today's study topic into it using w mode.

topic = input("Enter topic name: ")

with open("daily_notes.txt","w") as f:
    f.write(topic)

print("Study topic Written successfully")

# 19.Create marks.txt with initial marks, then append one more student's marks without deleting existing data.

name = input("Enter the name: ")
marks = input("Enter marks: ")

with open("marks.txt","a") as f:
    f.write(name + " - " + marks + "\n")

print("Marks append successfully")

# 20.Create a text file with five lines and use with open() together with readlines() to display all lines.

with open("blog.txt") as f:
    lines = f.readlines()

for line in lines:
    print(line,end="")