# Medium Level Practice Questions

# 1.Take the user's first name and last name as input and print the full name in title case.

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

full_name = first_name + " " + last_name  # Concatenation(joining strings using +.)
print(full_name.title())

# 2.Take a string as input and print:
# Total number of characters
# Number of times the letter "a" appears

s = "banana"

print("Total Characters:",len(s))
print("Count of a:",s.count("a"))

# 3.Create a string and print it in reverse using slicing.

string = "Delhi"
print(string[::-1])

# 4.Take a username as input and check whether it starts with "@".

user_name = input("Enter the username: ")
print(user_name.startswith("@"))

# 5.Take an email as input and check whether it ends with ".com".

email = input("Enter Email: ")
print(email.endswith(".com"))

# 6.Take a sentence from the user and replace "Python" with "Java".

s = input("Enter the sentence: ")
print(s.replace("Python","Java"))

# 7.Take a sentence and find the position of a word entered by the user.

sentence = input("Enter the sentence: ")
word = input("Enter the word: ")

print(sentence.find(word)) # Important concept

# 8.Take a sentence with extra spaces and remove spaces from both ends using strip().

s = input("Enter the sentence: ")
print(s.strip())

# 9.Create a string "Programming" and print:
# First 5 characters
# Last 5 characters
# Every second character  # Meaning- Start from the first character and take one character, skip one character, take the next, skip the next, and so on.

string = "Programming"

print(string[:5])
print(string[-5:])
print(string[::2])

# 10.Take rondom name as input and print:
# Length of the name
# First character
# Last character
# Name in uppercase

name = input("Enter the name: ")

print("Length:",len(name))
print("First character:",name[0])
print("Last character:",name[-1])
print("Uppercase:",name.upper())

# 11.Take a string as input and count the occurrences of:
# a
# e
# i
# o
# u

string = input("Enter the string: ")

print("a:",string.count("a"))
print("e:",string.count("e"))
print("i:",string.count("i"))
print("o:",string.count("o"))
print("u:",string.count("u"))

# 12.Take a password as input and print its length. Check if the length is at least 8 characters.

password = input("Enter the password: ")

print("Length:",len(password))
print(len(password) >= 8)

# 13.Take a sentence as input and convert it to title case using title().

sentence = input("Enter the sentence: ")

print(sentence.title())

# 14.Write a program that prints:
# Random name on one line
# Random city on the next line
# Your favorite subject after a tab space
# Use escape sequence characters.

print("Rahul\nKanpur\n\tPython")

# 15. Mini String Project
# Take a sentence from the user and display:
# Original sentence
# Length of sentence
# Sentence in uppercase
# Sentence in lowercase
# Number of spaces in the sentence
# Whether it starts with a specific word entered by the user

sentence = input("Enter sentence: ")
word = input("Enter starting word: ")

print("Original:",sentence)
print("Length:",len(sentence))
print("Uppercase:",sentence.upper())
print("Lowercase:",sentence.lower())
print("Number of spaces:",sentence.count(" "))
print("Starts with a specific word:",sentence.startswith(word))