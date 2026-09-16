# Easy Level Practice Questions

# 1.Print numbers from 1 to 10 using a while loop.

i = 1

while(i<11):
    print(i)
    i += 1

# 2.Print numbers from 10 to 1 using a while loop.

i = 10

while(i>0):
    print(i)
    i -= 1

# 3.Print numbers from 1 to 20 using a for loop.

for i in range(1,21):
    print(i)

# 4.Print all even numbers from 1 to 20 using a for loop.

for i in range(1,21):
    if i%2 == 0:
        print(i)

# or

for i in range(2,21,2):
    print(i)

# 5.Print all odd numbers from 1 to 20 using a while loop.

i = 1

while(i<21):
    if i%2 != 0:
        print(i)
    i += 1

# or 

i = 1

while(i<21):
    print(i)
    i += 2

# 6.Take a number N as input and print numbers from 1 to N.

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print(i)

# 7.Take a number N as input and print numbers from N to 1.

n = int(input("Enter the number: "))

while(n>=1):
    print(n)
    n -= 1

# 8.Print the multiplication table of a given number from 1 to 10.

n = int(input("Enter the number: "))

for i in range(1,11):
    print(n, "X", i, "=", n * i)
    
    # or

    print(f"{n} X {i} = {n * i}")

# 9.Calculate the sum of numbers from 1 to N using a while loop.

# n = int(input("Enter the number: "))

i = 1
sum = 0

while(i<=n):
    sum += i # or sum = sum + i
    i += 1   # or i = i + 1

print("Sum:",sum)

# 10.Calculate the sum of even numbers from 1 to 50.

sum = 0

for i in range(2,51,2):
    sum += i

print("Sum:",sum)

# 11.Print each character of a string using a for loop.

s = input("Enter the string: ")

for i in s:
    print(i)

# 12.Print all elements of a list using a for loop.

l = [1,2,3,4]

for i in l:
    print(i)

# 13.Print all elements of a tuple using a for loop.

t = (1,2,3,4)

for i in t:
    print(i)

## 14.Print all keys and values of a dictionary using a for loop.

d = {
    "Name": "Rohan",
    "City": "Kanpur"
}

for key,value in d.items():
    print(key,":",value)

# 15.Print all elements of a set using a for loop.

s = {1,2,3,4}

for i in s:
    print(i)

# 16.Use the range() function to print numbers from 5 to 15.

for i in range(5,16):
    print(i)

# 17.Use range(start, stop, step) to print:
# 0
# 5
# 10
# 15
# 20

for i in range(0,21,5):
    print(i)

# 18.Use a for...else loop to print numbers from 1 to 5, then print "Loop Finished".

for i in range(1,6):
    print(i)
else:
    print("Loop Finished")

# 19.Use the break statement to stop printing numbers when the value becomes 5.

for i in range(1,11):
    if(i == 5):
        break
    print(i)

# 20.Use the continue statement to skip printing the number 5 while printing numbers from 1 to 10.

for i in range(1,11):
    if(i == 5):
        continue
    print(i)