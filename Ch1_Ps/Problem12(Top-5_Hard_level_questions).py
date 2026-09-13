# Hard-Level Practice Questions

# 1. Lucky Number Generator
# Write a program that:
# Imports the random module.
# Generates 5 random numbers between 1 and 100.
# Prints each number on a new line.
# Add comments explaining the code.

# Importing random module
import random

# Generate and printing 5 Random number between 1 and 100
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

# 2. Math Toolkit
# Write a program that:
# Imports the math module.
# Finds the square root of 625.
# Finds the value of π (pi).
# Finds the value of e.
# Prints all results with proper labels.
# Use comments for each step.

# Importing the math module
import math

#  Finding the square root 
print("Square root of 625:",math.sqrt(625))
# Printing the value of pi
print("Value of pi:",math.pi)
# Printing the value of e
print("Value of e:",math.e)

# 3. Random Password Suggestion
# Write a program that:
# Imports the random module.
# Generates a 4-digit random password.
# Prints the password.
# Add comments describing the program.

# Importing random module
import random

# Generate the 4-digit random password
password = random.randint(1000,9999)
# Printing the password
print("Suggested Password:",password)

# 4. Built-in vs External Modules Table
# Create a Python program that prints the following table:
# Module       Type
# ---------------------
# os           Built-in
# math         Built-in
# random       Built-in
# flask        External
# tensorflow   External
# pandas       External
# Use comments to explain the program.


# Printing modules type
print("Module          Type")
print("------------------------")
print("os              Built-in")
print("math            Built-in")
print("random          Built-in")
print("flask           External")
print("tensorflow      External")
print("pandas          External")

# 5. Combined Challenge Program
# Write a program that:
# Imports both math and random.
# Generates a random number between 1 and 20.
# Finds the square root of that random number.
# Prints both the random number and its square root.
# Add meaningful comments throughout the code.

# Importing module
import math
import random
# Generate the random number
Rn = random.randint(1,20)
# Find the square root
Sr = math.sqrt(Rn)
# Display the output
print("Random Number:",Rn)
print("Square Root:",Sr)