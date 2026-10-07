class Employee:   # Employee (Class)
    language = "Python"  # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()   # harry (Object)
# harry.language = "Java Script"  # This is an instance attribute

harry.getInfo()
# or
Employee.getInfo(harry)

harry.greet() # or Employee.greet(harry)