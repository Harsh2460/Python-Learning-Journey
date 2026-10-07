class Employee:   # Employee (Class)
    language = "Py"  # This is a class attribute
    salary = 1200000

harry = Employee()   # harry (Object)
harry.name = "Harry"  # This is an instance attribute
print(harry.name,harry.salary,harry.language)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name,rohan.language,rohan.salary)

# Here name is instance attribute and salary and language are class attribute as they directly belong to the class
 