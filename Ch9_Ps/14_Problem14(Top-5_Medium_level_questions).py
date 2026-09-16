# Hard Level Practice Questions

# 1. Complete File Statistics
# Write a program that reads a text file and displays:
# Total lines
# Total words
# Total characters
# Total vowels
# Total occurrences of a word entered by the user
# Example:
# File:
# Python is easy to learn.
# Python is powerful.
# Input:
# Enter word: Python
# Output:
# Total Lines = 2
# Total Words = 7
# Total Characters = 41
# Total Vowels = 13
# Word Occurrence = 2

word = input("Enter the word: ")

with open("stat.txt") as f:
    data = f.readlines()

with open("stat.txt") as f:
    info = f.read()

vowels = 0

for ch in info.lower():
    if ch in "aeiou":
        vowels += 1

print("Total Lines =",len(data))
print("Total Words =",len(info.split()))
print("Total Charcters =",len(info))
print("Total Vowels =",vowels)
print("Word Occurrence =",info.count(word))

# 2. Find the Most Frequent Word
# Write a program to read a text file and find the word that occurs most frequently.
# Use a dictionary to store the frequency of each word.
# Example:
# File:
# python is easy
# python is powerful
# python is popular
# Output:
# Most Frequent Word = python
# Frequency = 3

with open("freq.txt", "r") as f:
    text = f.read().lower()

words = text.split()

frequency = {}

for word in words:
    word = word.strip(".,!?")

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

most_word = max(frequency, key=frequency.get)

print("Most Frequent Word =", most_word)
print("Frequency =", frequency[most_word])

# 3. Separate Numbers into Multiple Files
# Create a file containing several numbers. Read the numbers and create three separate files
# even.txt → even numbers
# odd.txt → odd numbers
# prime.txt → prime numbers
# Use functions to check whether a number is prime.
# Example:
# numbers.txt:
# 2
# 7
# 10
# 13
# 15
# 20
# Output:
# even.txt:
# 2
# 10
# 20
# odd.txt:
# 7
# 13
# 15
# prime.txt:
# 2
# 7
# 13

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2,number):
        if number % i == 0:
            return False

    return True

with open("m_numbers.txt","r") as f:
    nums = f.readlines()

with open("even.txt","w") as even_file:
    with open("odd.txt","w") as odd_file:
        with open("prime.txt","w") as prime_file:

            for line in nums:
                n = int(line)

                if n % 2 == 0:
                    even_file.write(str(n) + "\n")
                else:
                    odd_file.write(str(n) + "\n")

                if is_prime(n):
                    prime_file.write(str(n) + "\n")

print("Numbers separated successfully")                
     
# 4. Student Marks File Analyzer
# Create a file containing student names and marks in this format:
# Rahul,85
# Aman,92
# Kanha,78
# Rohit,91
# Write a program using functions to:
# Read the file
# Find the student with the highest marks
# Find the student with the lowest marks
# Calculate the average marks
# Count students who scored 80 or above
# Expected Output:
# Highest Marks = Aman - 92
# Lowest Marks = Kanha - 78
# Average Marks = 86.5
# Students Above 80 = 3

def read_students():
    students = []

    with open("stu.txt","r") as f:
        lines = f.readlines()

    for line in lines:
        name,marks = line.strip().split(",")  # line.strip() removes whitespace and newline characters (\n). and .split(",") splits each line into two parts around the comma: the name string and the marks string.
        students.append(name,int(marks))

    return students

def highest_student(students):
    return max(students,key=lambda x: x[1])

def lowest_student(students):
    return min(students,key=lambda x: x[1])

students = read_students()
highest = highest_student()
lowest = lowest_student()

total = 0
above_80 = 0

for name,marks in students:
    total += marks

    if marks >= 80:
        above_80 += 1

average = total / len(students)

print("Highest Marks =",highest[0], " - ", highest[1])
print("Lowest Marks =",lowest[0], " - ", lowest[1])
print("Average Marks =",average)
print("Students Above 80 =",above_80)

# 5. File Word Analysis Program
# Write a program that reads a text file and creates a complete word analysis.
# Display:
# Total number of words
# Number of unique words
# Most frequent word
# Least frequent word
# All unique words
# Frequency of each word
# Use a dictionary to store word frequencies and a set to store unique words.
# Example:
# File:
# python is easy
# python is useful
# python is powerful
# Output:
# Total Words = 9
# Unique Words = 5
# Most Frequent Word = python
# Frequency = 3

with open("pro.txt", "r") as f:
    text = f.read().lower()

words = text.split()

frequency = {}

for word in words:
    word = word.strip(".,!?")

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

unique_words = set(frequency.keys())

most_word = max(frequency, key=frequency.get)
least_word = min(frequency, key=frequency.get)

print("Total Words =", len(words))
print("Unique Words =", len(unique_words))
print("Most Frequent Word =", most_word)
print("Frequency =", frequency[most_word])
print("Least Frequent Word =", least_word)
print("Frequency =", frequency[least_word])

print("\nUnique Words:")
print(unique_words)

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, "=", count)