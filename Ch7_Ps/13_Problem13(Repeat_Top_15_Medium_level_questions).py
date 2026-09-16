# Repeat Same Medium Level Practice Questions

# 1.Take a number N as input and calculate its factorial using a for loop.

# Input from user
n = int(input("Enter the number: "))

# store the total element of fact
fact = 1

# Loop started from 1 to n 
for i in range(1,n+1):
    # It is calculate the factorial of n number
    fact = fact * i

# Print the output
print("Factorial:",fact)

# 2.Take a number N as input and count the total number of digits using a while loop.

n = int(input("Enter the number: "))

# store the value of count
count = 0

# loop started from n and stop when n will be 0
while(n > 0):
    # every time loop flow then count will be increases one time
    count += 1
    # It can remove the last element of n everytime
    n //= 10

print("Total digit:",count)

# 3.Take a number N as input and calculate the sum of its digits.

n = int(input("Enter the number: "))

sum = 0

while(n > 0):
    # it will give the last element of n everytime
    digit = n % 10
    # store the elemnt of digit everytime
    sum += digit
    n //= 10

print("Sum of Digits:",sum)

# 4.Take a number N as input and print its reverse.

n = int(input("Enter the number: "))

reverse = 0

while(n > 0):
    digit = n % 10
    # It is calaulate the reverse number entered by the user
    reverse = reverse * 10 + digit
    n //= 10

print("Reverse:",reverse)

# 5.Take a number N as input and check whether it is a palindrome number.

n = int(input("Enter the number: "))

original = n
reverse = 0

while(n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

# check the condition will be true or not
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# 6.Take a number N as input and check whether it is an Armstrong number.

n = int(input("Enter the number: "))

original = n
sum = 0

# it will give the length of n number
power = len(str(n))

while(n > 0):
    digit = n % 10
    sum += digit ** power
    n //= 10

if original == sum:
    print("Armstrong number")
else:
    print("Not a Armstrong number")

# 7.Take a number N as input and print all factors of that number.

n = int(input("Enter the number: "))

print("Factors are:")

for i in range(1,n+1):
    # it will give the factors of n numbers
    if n % i == 0:
        print(i)

# 8.Take a number N as input and check whether it is a prime number.

n = int(input("Enter the number: "))

count = 0

for i in range(1,n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# or 

n = int(input("Enter the number: "))

for i in range(2,n):
    if n % i == 0:
        print("Not a Prime number")
        break

else:
    print("Prime Number")

# 9.Print all prime numbers from 1 to N.

n = int(input("Enter the number: "))

print("Prime Numbers: ")

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

# 11.Print the following pattern:
# *****
# ****
# ***
# **
# *

n = int(input("Enter the number: "))

for i in range(n,0,-1):
    print("*" * i)

# 12.Print the following multiplication tables from 1 to 10.

for i in range(1,11):
    print("Table is",i)
    
    for j in range(1,11):
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