# 2. Write a python program using function to convert Fahrenheit to Celsius.

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter the number: "))
c = f_to_c(f)
print(f"{round(c,2)}°C")