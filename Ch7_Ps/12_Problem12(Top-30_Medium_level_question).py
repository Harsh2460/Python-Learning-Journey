# Medium Level Practice Questions

# 1.Take a number N as input and calculate its factorial using a for loop.

n = int(input("Enter the number: "))

fact = 1

for i in range(1,n+1):
    fact = fact * i

print("Factorial of",n, "is", fact)

## 2.Take a number N as input and count the total number of digits using a while loop.

n = int(input("Enter the number: "))

count = 0

while(n > 0):
    count += 1
    n //= 10

print("Total Digits:",count)

## 3.Take a number N as input and calculate the sum of its digits.

n = int(input("Enter the number: "))

sum = 0

while(n > 0):
    digit = n % 10 # 1234 % 10 evaluates to 4
    sum += digit
    n //= 10       # 1234 // 10 becomes 123

print(sum)

# 4.Take a number N as input and print its reverse.

n = int(input("Enter the number: "))

reverse = 0

while(n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)

# 5.Take a number N as input and check whether it is a palindrome number.

n = int(input("Enter the number: "))

orginal = n
reverse = 0

while(n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if orginal == reverse:
    print("Palindrome number")
else:
    print("Not a Palindrome number")

# 6.Take a number N as input and check whether it is an Armstrong number.

n = int(input("Enter the number: "))

original = n
sum = 0

power = len(str(n)) # The len() function works only with objects that have a length, such as: str,list,tuple,dict,set.But an integer (int) has no length.

while(n > 0):
    digit = n % 10
    sum += digit ** power
    n //= 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# 7.Take a number N as input and print all factors of that number.

n = int(input("Enter the number: "))

print("Factors are:")

for i in range(1,n+1):
    if n % i == 0:
        print(i)

# 8.Take a number N as input and check whether it is a prime number.

n = int(input("Enter the number: "))

count = 0

for i in range(1,n+1):
    if (n % i) == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# or 

n = int(input("Enter the number: "))

for i in range(2,n):
    if(n % i) == 0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")

# 9.Print all prime numbers from 1 to N.

n = int(input("Enter the number: "))

print("Prime Numbers:")

for num in range(2,n+1):
    count = 0

    for i in range(1,num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)

# 10.Print the following pattern:
# *
# **
# ***
# ****
# *****

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print("*" * i)

# or 

for i in range(1,n+1):
    print("*" * i,end="")
    print()

# 11.Print the following pattern:
# *****
# ****
# ***
# **
# *

n = int(input("Enter the number: "))

for i in range(n,0,-1):
    print("*" * i)

# or 

for i in range(n,0,-1):
    print("*" * i,end="")
    print()

# 12.Print the following multiplication tables from 1 to 10.
# Example:
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 10 x 10 = 100    

for num in range(1,11):
    for i in range(1,11):
        print(num, "x", i, "=", num * i)

# # or 

for i in range(1, 11):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print() 

# 13.Take 10 numbers as input and calculate:
# Sum
# Average

sum = 0

for i in range(1,11):
    n = int(input("Enter the number: "))
    sum += n
    
avg = sum / 10

print("Sum:",sum)
print("Average:",avg)

# 14.Use the continue statement to print numbers from 1 to 20, skipping all multiples of 3.

for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)

# 15.Use the break statement to stop printing numbers when the first number divisible by 13 is found between 1 and 100.

for i in range(1,101):
    if i % 13 == 0:
        print("First number divisible by 13:",i)
        break

# 16.Take a number N as input and print the square of numbers from 1 to N.

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print("Square of",i, ":", i * i) # or i ** 2

# 17.Take a number N as input and print the cube of numbers from 1 to N.

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print(f"Cube of {i}: {i ** 3}")

# 18.Take a number N as input and count how many even and odd numbers are present from 1 to N.

n = int(input("Enter the number: "))

even = 0
odd = 0

for i in range(1,n+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Count Even Number:",even)
print("Count Odd Number:",odd)

# 19.Take a number N as input and print all numbers divisible by 5 between 1 and N.

n = int(input("Enter the number: "))

print("Numbers Divisible by 5:")

for i in range(1,n+1):
    if i % 5 == 0:
        print(i)

# 20.Take a number N as input and print all numbers divisible by 3 and 7 between 1 and N.

n = int(input("Enter the number: "))

print("Numbers divisible by 3 and 7:")

for i in range(1,n+1):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

# 21.Take a string as input and count the total number of vowels.

s = input("Enter the string: ")

vowel = 0

for i in s:
    if i in "aeiouAEIOU":
        vowel += 1

print("Total vowels:",vowel)

# 22.Take a string as input and count the total number of uppercase and lowercase letters.

s = input("Enter the string: ")

upper = 0
lower = 0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("Uppercase:",upper)
print("Lowercase:",lower)

# 23.Take a string as input and count the number of digits, alphabets, and special characters.

s = input("Enter the string: ")

digit = 0
alphabet = 0
special = 0

for i in s:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alphabet += 1
    else:
        special += 1

print("Total Digits:",digit)
print("Total Alphabets:",alphabet)
print("Total Special Characters:",special)

# 24.Take a string as input and print each character along with its position.
# Example:
# Input: Python
# Output:
# 1 : P
# 2 : y
# 3 : t
# 4 : h
# 5 : o
# 6 : n

s = input("Enter the string: ")

count = 1

for i in s:
    print(count, ":", i)
    count += 1

# 25.Take N numbers as input and find the largest number.

n = int(input("How many numbers?: "))

largest = int(input("Enter number: "))

for i in range(2,n+1):
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

print("Largest Number:",largest)

# 26.Take N numbers as input and find the smallest number.

n = int(input("How many numbers?: "))

smallest = int(input("Enter number: "))

for i in range(2,n+1):
    num = int(input("Enter number: "))

    if num < smallest:
        smallest = num

print("Smallest Number:",smallest)

# 27.Take N numbers as input and count how many numbers are positive, negative, and zero.

n = int(input("How many numbers?: "))

pos = 0
neg = 0
zero = 0

for i in range(1,n+1):
    num = int(input("Enter number: "))

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print("Total Postive Numbers:",pos)
print("Total Negative Numbers:",neg)
print("Total Zero Numbers:",zero)

# 28.Print the following pattern:
# 1
# 12
# 123
# 1234
# 12345

n = int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
      print(j,end="")
    print()

# 29.Print the following pattern:
# 12345
# 1234
# 123
# 12
# 1

n = int(input("Enter the number: "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 30.Print the following pattern:
# A
# AB
# ABC
# ABCD
# ABCDE

n = int(input("Enter the number: "))

for i in range(1,n+1):
    ch = 65
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch += 1

    print()