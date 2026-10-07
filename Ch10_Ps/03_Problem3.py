# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 

# No 

class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute beacuse instance attribute is not present

o.a = 0 # Instance Attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present

print(Demo.a) # Prints the class attribute