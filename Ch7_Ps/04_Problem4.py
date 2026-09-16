# 4. Write a program to find whether a given number is prime or not. 

# Q.What is prime number - A prime number is a number greater than 1 that is divisible only by 1 and itself.

n = int(input("Enter a number: "))

for i in range(2,n):
    if (n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

