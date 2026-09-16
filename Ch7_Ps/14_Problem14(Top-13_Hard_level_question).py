# Hard Level Practice Questions

# 1. Fibonacci Series
# Write a program to:
# Take a number N as input.
# Print the first N terms of the Fibonacci series.
# Example:
# Input:
# 10
# Output:
# 0 1 1 2 3 5 8 13 21 34

n = int(input("Enter the number: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(1,11):
    print(a,end=" ")
    c = a + b
    a = b
    b = c

# 2. Number Pattern Generator
# Write a program to print the following number pattern.
# Example (N = 5):
# 1
# 12
# 123
# 1234
# 12345
# Also print the reverse pattern:
# 12345
# 1234
# 123
# 12
# 1

n = int(input("Enter the number: "))

print("Incresing Pattern:")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("Decreasing Pattern:")

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 3. Prime Numbers and Their Sum
# Write a program to:
# Take a number N as input.
# Print all prime numbers from 1 to N.
# Count the total prime numbers.
# Calculate and print the sum of all prime numbers.
# Example:
# Input:
# 20
# Output:
# Prime Numbers:
# 2 3 5 7 11 13 17 19
# Total Prime Numbers = 8
# Sum = 77

n = int(input("Enter the number: "))

total = 0
prime_sum = 0

print("Prime Numbers:")

for i in range(2,n+1):
    count = 0

    for j in range(1,i+1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(i,end=" ")
        total += 1
        prime_sum += i

print()

print("Total Prime Numbers = ",total)
print("Sum = ",prime_sum)

# 4. Student Marks Analysis
# Write a program to:
# Take marks of 10 students as input.
# Calculate:
# Total marks
# Average marks
# Highest marks
# Lowest marks
# Count how many students passed (marks ≥ 33).
# Count how many students failed.
# Display all the results.

total = 0
h = 0
l = 100
p_count = 0
f_count = 0

for i in range(1,11):
    n = int(input("Enter the marks: "))
    total += n

    if n > h:
        h = n

    if n < l:
        l = n

    if n >= 33:
        p_count += 1
    else:
        f_count += 1

avg = total / 10

print("Total Marks:",total)
print("Average Marks:",avg)
print("Highest Marks:",h)
print("Lowest Marks:",l)
print("Count of Students Passed:",p_count)
print("Count of Students Failed:",f_count)

# 5. Number Analysis Mini Project
# Write a program to:
# Take a number N as input.
# Calculate and display:
# Reverse of the number
# Sum of digits
# Number of digits
# Whether it is a palindrome or not
# Whether it is an Armstrong number or not
# Display all the results together.

n = int(input("Enter the number: "))

original = n
reverse = 0
s_digits = 0
n_digits = 0
a_sum = 0

power = len(str(n))

while(n > 0):
    digit = n % 10 
    reverse = reverse * 10 + digit
    s_digits += digit
    n_digits += 1
    a_sum += digit ** power
    n //= 10

print("Reverse of the number:",reverse)
print("Sum of digits:",s_digits)
print("Number of digits:",n_digits)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")

if original == a_sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

# 6.Strong Number
# Write a program to:
# Take a number N as input.
# Calculate the factorial of each digit.
# Find the sum of these factorials.
# Check whether the number is a Strong Number.
# Example:
# 145 → Strong Number
# 40585 → Strong Number

n = int(input("Enter the number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10

    fact = 1
    
    for i in range(1,digit+1):
        fact = fact * i
    sum += fact 
    n //= 10

if original == sum:
    print("Strong Number")
else:
    print("Not a Strong Number")

# 7. Perfect Number
# Write a program to:
# Take a number N as input.
# Find the sum of all its proper factors (excluding the number itself).
# Check whether the number is a Perfect Number.
# Example:
# 6 → Perfect Number
# 28 → Perfect Number

n = int(input("Enter the number: "))

original = n
sum = 0

for i in range(1,n):
    if n % i == 0:
        sum += i

if original == sum:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# 8.Decimal to Binary Conversion
# Write a program to:
# Take a decimal number as input.
# Convert it into binary using a while loop.
# Do not use Python's built-in bin() function.
# Example:
# Input:
# 13
# Output:
# 1101

n = int(input("Enter the decimal number: "))

binary = ""

while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n //= 2

print("Binary:",binary)

# 9.Diamond Star Pattern
# Write a program to print the following pattern.
# For N = 5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print()

for i in range(n-1,0,-1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print()

# 10.Frequency of Digits
# Write a program to:
# Take a number as input.
# Count how many times each digit appears.
# Display the frequency of every digit.
# Example:
# Input:
# 12233441
# Output:
# Digit 1 = 2 times
# Digit 2 = 2 times
# Digit 3 = 2 times
# Digit 4 = 2 times

n = input("Enter the number: ")

checked = ""

for i in n:
    if i not in checked:
        count = 0

        for j in n:
            if j == i:
                count += 1

        print("Digit", i, "=", count, "times")
        checked += i

# 11.Neon Number
# Write a program to:
# Take a number N as input.
# Find the square of the number.
# Calculate the sum of the digits of the square.
# Check whether the number is a Neon Number.
# Example:
# 9 → Neon Number (9² = 81, 8 + 1 = 9)

n = int(input("Enter the number: "))

sq = n ** 2

sum = 0

while sq > 0:
    dig = sq % 10
    sum += dig
    sq //= 10

if n == sum:
    print("Neon Number")
else:
    print("Not neon Number")

# 12.Spy Number
# Write a program to:
# Take a number N as input.
# Calculate the sum of its digits.
# Calculate the product of its digits.
# Check whether the sum and product are equal.
# Example:
# 123 → Spy Number (1 + 2 + 3 = 6 and 1 × 2 × 3 = 6)

n = int(input("Enter the number: "))

temp = n
total_sum = 0
product = 1

while temp > 0:
    digit = temp % 10
    total_sum += digit
    product *= digit
    temp //= 10

if total_sum == product:
    print("Spy Number")
else:
    print("Not a Spy Number")

# 13.Floyd's Triangle
# Write a program to print Floyd's Triangle.
# Example (Rows = 5):
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = int(input("Enter the number: "))

num = 1

for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()

