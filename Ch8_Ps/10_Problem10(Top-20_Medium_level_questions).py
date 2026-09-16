# Medium Level Practice Questions 

# 1.Write a function check_even_odd(n) that takes a number and prints whether it is Even or Odd.

def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

n = int(input("Enter the number: "))
check_even_odd(n)

# 2.Write a function largest(a, b, c) that takes three numbers and returns the largest number.

def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
result = largest(a,b,c)
print("Largest:",result)

# 3.Write a function check_number(n) that checks whether a number is positive, negative, or zero.

def check_number(n):
    if n > 0:
        return Postive 
    elif n < 0:
        return Negative
    else:
        return Zero

n = int(input("Enter the number: "))
print(check_number(n))

# 4.Write a function factorial(n) that takes a number and returns its factorial.
# Example:
# Input: 5
# Output: 120

def factorial(n):
    product = 1

    for i in range(1,n+1):
        product *= i
    return product

n = int(input("Enter the number: "))
print(factorial(n))

# 5.Write a function table(n) that prints the multiplication table of a given number from 1 to 10.

def table(n):
    for i in range(1,11):
            print(f"{n} X {i} = {n * i}")

n = int(input("Enter the number: "))
table(n)

# 6.Write a function count_vowels(text) that counts the total number of vowels in a string.
# Example:
# Input: programming
# Output: 3

def count_vowels(text):
    count = 0

    for i in text:
        if i in "aeiouAEIOU":
            count += 1
    return count

text = input("Enter the text: ")
v = count_vowels(text)
print("Total Vowels:",v)

# 7.Write a function reverse_string(text) that returns the reverse of a string.
# Example:
# Input: Python
# Output: nohtyP

def reverse_string(text):
    return text[::-1]

text = input("Enter the text: ")
print("Reverse:",reverse_string(text))

# 8.Write a function is_palindrome(text) that checks whether a string is a palindrome.
# Example:
# Input: madam
# Output: Palindrome

def is_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = input("Enter the text: ")
print(is_palindrome(text))

# 9.Write a function sum_digits(n) that calculates and returns the sum of all digits of a number.
# Example:
# Input: 12345
# Output: 15

def sum_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

n = int(input("Enter the number: "))
result = sum_digits(n)
print("Sum:",result)

# 10.Write a function is_prime(n) that checks whether a number is prime.
# Example:
# Input: 17
# Output: Prime Number

def is_prime(n):
    count = 0

    for i in range(1,n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

n = int(input("Enter the number: "))
is_prime(n)

# 11.Write a function fibonacci(n) that prints the first N terms of the Fibonacci series.
# Example:
# Input: 7
# Output: 0 1 1 2 3 5 8

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a,end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter the number: "))
fibonacci(n)

# 12.Write a function is_armstrong(n) that checks whether a number is an Armstrong number.
# Example:
# Input: 153
# Output: Armstrong Number


def is_armstrong(n):
    num = n
    total = 0

    power = len(str(n))

    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10

    if num == total:
        return Armstrong Number
    else:
        return Not a Armstrong Number

n = int(input("Enter the number: "))
print(is_armstrong(n))

# 13.Create a function:
# def student(name, course="BCA"):
# The function should display the student's name and course. Call it once with only the name and once with both arguments.

def student(name,course="BCA"):
    print("Student Name:",name)
    print("Student Course:",course)

name = input("Enter the name: ")
course = input("Enter the course: ")

student(name)
student(name,course)

# 14.Write a recursive function sum_n(n) that returns the sum of the first N natural numbers.
# Example:
# Input: 5
# Output: 15

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

n = int(input("Enter the number: "))
print("Sum:",sum_n(n))

# 15.Write a recursive function factorial(n) to calculate the factorial of a number.
# Example:
# Input: 6
# Output: 720

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number: "))
print("Factorial:",factorial(n))

# 16.Write a function is_perfect(n) that checks whether a number is a Perfect Number.
# A perfect number is a number whose proper divisors add up to the number itself.
# Example:
# Input: 28
# Output:
# Perfect Number

def is_perfect(n):
    total = 0

    for i in range(1,n):
        if n % i == 0:
            total += i

    if total == n:
        return True   # When a function begins with is_, has_, can_, or should_, it acts as a yes/no predicate
    else:
        return False

n = int(input("Enter the number: "))

if is_perfect(n):
    print("Perfect Number")
else:
    print("Not Perfect Number")

# 17.Write a function largest_digit(n) that returns the largest digit present in a number.
# Example:
# Input: 58392
# Output: Largest Digit = 9

def largest_digit(n):
    largest = 0

    while n > 0:
        digit = n % 10

        if digit > largest:
            largest = digit

        n //= 10

    return largest

n = int(input("Enter the number: "))
print("Largest Digit =",largest_digit(n))

# 18.Write a function count_digits(n) that takes a number and returns the total number of digits.
# Example:
# Input: 45892
# Output: Number of Digits = 5

def count_digits(n):
    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count

n = int(input("Enter the number: "))
print("Number of Digits =",count_digits(n))

# 19.Write two functions:
# factorial(n) → returns the factorial.
# sum_n(n) → returns the sum of numbers from 1 to N.
# Take N as input and display both results.
# Example:
# Input: 5
# Output:
# Factorial = 120
# Sum = 15

def factorial(n):
    product = 1

    for i in range(1,n+1):
        product *= i

    return product

def sum_n(n):
    total = 0

    for i in range(1,n+1):
        total += i

    return total

n = int(input("Enter the number: "))
print("Factorial =",factorial(n))
print("Sum =",sum_n(n))

# 20.Write a function count_even_odd(n) that counts how many digits of a number are even and how many are odd.
# Example:
# Input: 123456
# Output:
# Even Digits = 3
# Odd Digits = 3

def count_even_odd(n):
    even = 0
    odd = 0

    while n > 0:
        digit = n % 10
        
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1

        n //= 10

    return even,odd

n = int(input("Enter the number: "))
even,odd = count_even_odd(n)

print("Even Digits =",even)
print("Odd Digits =",odd)