class Employee:   # Employee (Class)
    language = "Python"  # This is a class attribute
    salary = 1200000

harry = Employee()   # harry (Object)
harry.language = "Java Script"  # This is an instance attribute
print(harry.language,harry.salary)

# Instance attributes, take preference over class attributes during assignment & retrieval. 