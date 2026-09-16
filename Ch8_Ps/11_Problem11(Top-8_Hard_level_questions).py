# Hard Level Practice Questions

# 1.Write a function prime_numbers(n) that prints all prime numbers from 1 to N and returns the total number of prime numbers.
# Example:
# Input: 20
# Output:
# 2 3 5 7 11 13 17 19
# Total Prime Numbers = 8

def prime_numbers(n):
    total = 0

    for i in range(2,n+1):
        count = 0

        for j in range(1,i+1):
            if i % j == 0:
                count += 1

        if count == 2:
            print(i,end=" ")
            total += 1

    return total

n = int(input("Enter the number: "))
t = prime_numbers(n)

print()
print("Total Prime Numbers:",t)

# 2.Write a function armstrong_numbers(n) that prints all Armstrong numbers from 1 to N.
# Example:
# Input: 500
# Output:
# 1 2 3 4 5 6 7 8 9 153 370 371 407

def is_armstrong(n):
    original = n
    total = 0
    power = len(str(n))

    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10

    return total == original

def armstrong_number(n):
    for num in range(1,n+1):
        if is_armstrong(num):
            print(num,end=" ")

n = int(input("Enter the number: "))
armstrong_number(n)

# 3.Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
# Example:
# Input: 7
# Output:
# Fibonacci Number = 13

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number: "))
result = fibonacci(n)
print("Fibonacci Number =",result)

# 4.Write a recursive function power(base, exponent) that calculates:
# base^exponent
# Do not use Python's ** operator.
# Example:
# Input:
# 2
# 5
# Output:
# Power = 32

def power(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base,exponent-1)

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))

result = power(base,exponent)
print("Power =",result)

# 5. Number Analysis Using Multiple Functions
# Create separate functions to:
# Find the reverse of a number
# Find the sum of digits
# Count the digits
# Check whether the number is a palindrome
# Check whether the number is an Armstrong number
# Then call all the functions from the main program and display the results.
# Example:
# Input:
# 153
# Output:
# Reverse = 351
# Sum of Digits = 9
# Number of Digits = 3
# Palindrome = False
# Armstrong = True

def reverse_n(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return reverse

def sum_n(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total

def count_n(n):
    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count

def palindrome_n(n):
    return n == reverse_n(n)

def armstong_n(n):
    orignal = n
    power = len(str(n))
    total_n = 0

    while n > 0:
        digit = n % 10
        total_n += digit ** power
        n //= 10

    return total_n == orignal

n = int(input("Enter the number: "))

print("Reverse =",reverse_n(n))
print("Sum of Digits =",sum_n(n))
print("Number of Digits =",count_n(n))
print("Palindrome =",palindrome_n(n))
print("Armstrong =",armstong_n(n))

# 6.Write a recursive function sum_digits(n) that returns the sum of all digits of a number.
# Example:
# Input: 9875
# Output: Sum of Digits = 29

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

n = int(input("Enter the number: "))
result = sum_digits(n)
print("Sum of Digits =",result)

# 7.Write a recursive function to reverse a number without using a loop.
# Example:
# Input: 12345
# Output: Reverse = 54321 

def reverse_n(n,reverse = 0):
    if n == 0:
        return reverse
    else:
        digit = n % 10
        reverse = reverse * 10 + digit
        return reverse_n(n // 10,reverse)

n = int(input("Enter the number: "))
print("Reverse =",reverse_n(n))

# 8.Write a recursive function gcd(a, b) to find the Greatest Common Divisor (GCD) of two numbers.
# Example:
# Input:
# 48
# 18
# Output:
# GCD = 6

# GCD stands for Greatest Common Divisor (also commonly known as the HCF or Highest Common Factor).
# Example: Finding the GCD of 48 and 18
#1. Find the factors of each number:
# Factors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48
# Factors of 18: 1, 2, 3, 6, 9, 18
#2. Identify the common factors:
# Common factors = 1, 2, 3, 6
#3. Select the largest one:
# GCD(48, 18) = 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("GCD =",gcd(a,b))