class Employee:
    company = "Google"

e = Employee()
print("Before =",e.company)

Employee.company = "Microsoft"
print("After =",e.company)