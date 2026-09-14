# Hard Level Practice Questions

# 1. Complete String Analyzer
# Take a string as input and display:
# Original String
# Length of String
# First Character
# Last Character
# Reverse String
# Uppercase Version
# Lowercase Version
# Title Case Version

s = input("Enter string: ")

print("Original:",s)
print("Length:",len(s))
print("First Character:",s[0])
print("Last Character:",s[-1])
print("Reverse:",s[::-1])
print("Uppercase:",s.upper())
print("Lowercase:",s.lower())
print("Title Case:",s.title())

# 2. Name Formatter Project
# Take a full name as input and print:
# Name in Uppercase
# Name in Lowercase
# Name in Title Case
# Total Characters (excluding leading and trailing spaces)
# First 3 Characters
# Last 3 Characters

name = input("Enter Full Name: ")

clean_name = name.strip()

print("Uppercase:",clean_name.upper())
print("Lowercase:",clean_name.lower())
print("Title case:",clean_name.title())
print("Total Character:",len(clean_name))
print("First three character:",clean_name[:3])
print("Last three Character:",clean_name[-3:])

# 3. Sentence Manipulation Project
# Take a sentence as input and display:
# Number of spaces
# Number of occurrences of letter "a"
# Whether it starts with "Python"
# Whether it ends with "."
# Replace all spaces with "-"

s = input("Enter the sentence: ")

print("Spaces:",s.count(" "))
print("Count of a:",s.count("a"))
print("Starts:",s.startswith("Python"))
print("Ends:",s.endswith("."))
print("Replace:",s.replace(" ","-"))

# 4. Advanced String Slicing
# Create a string:
# text = "ProgrammingLanguage"
# Print:
# First 10 characters
# Last 8 characters
# Every second character
# Every third character
# Reverse string

text = "ProgrammingLanguage"

print("First ten character:",text[:10])
print("Last eight character:",text[-8:])
print("Every second character:",text[::2])
print("Every third character:",text[::3])
print("Reverse string:",text[::-1])

text = "ProgrammingLanguage"

print(text[:10])
print(text[-8:])
print(text[::2])
print(text[::3])
print(text[::-1])

# 5. Mini String Report Generator
# Take a sentence from the user and generate a report showing:
# Original Sentence
# Length
# Uppercase
# Lowercase
# Title Case
# Reverse Sentence
# Count of Spaces
# Count of Letter "e"
# First 5 Characters
# Last 5 Characters

s = input("Enter the sentence: ")

print("Original:",s)
print("Length:",len(s))
print("Uppercase:",s.upper())
print("Lowercase:",s.lower())
print("Title case:",s.title())
print("Reverse:",s[::-1])
print("Spaces:",s.count(" "))
print("Count of e:",s.count("e"))
print("First 5 Characters:",s[:5])
print("Last 5 Characters:",s[-5:])

# 6.Palindrome Checker (Without if)

word = input("Enter a word: ")

print(word)
print(word[::-1])
print(word == word[::-1])