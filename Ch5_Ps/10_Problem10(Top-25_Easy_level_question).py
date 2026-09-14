# Easy Level Practice Questions

# 1.Create a dictionary to store name, age, and city. Print the dictionary.

d = {
    "name": "Rahul",
    "age": 26,
    "city": "Kanpur"
}

print(d)

# 2.Create a dictionary containing student details and print the value of the "name" key.

d = {
    "name": input("Enter name: "),
    "age": input("Enter age: ")
}

print(d["name"])

# 3.Create a dictionary of three subjects and their marks. Print all the keys.

marks = {
    "Maths": 86,
    "Hindi": 90,
    "English": 88
}

print(marks.keys())

# 4.Create a dictionary of three fruits and their prices. Print all the values.

fruits = {
    "Mango": 100,
    "Orange": 110,
    "Grapes": 120
}

print(fruits.values())

# 5.Create a dictionary and print all key-value pairs using the items() method.

d = {
    "name": "Sumit",
    "city": "Mumbai"
}

print(d.items())

# 6.Create a dictionary of employee details. Use the get() method to print the employee's salary.

emp = {
    "name": "Roshan",
    "salary": 60000
}

print(emp.get("salary"))

# 7.Create a dictionary and add a new key-value pair using the update() method.

d = {
    "name": "Sohan",
    "age": 16
}

d.update({"city": "Jaipur"})
print(d)

# 8.Create a dictionary and remove one key using the pop() method.

r = {
    "name": "Amit",
    "age": 28
}

r.pop("age")
print(r)

# 9.Create a dictionary of five items and remove the last inserted item using the popitem() method.

c = {
    "oli": 200,
    "mango": 110,
    "bat": 400,
    "kit-kate": 10,
    "maaza": 100
}

c.popitem()
print(c)

# 10.Create a copy of a dictionary using the copy() method and print both dictionaries.

c = {
    "oli": 200,
    "mango": 110,
    "bat": 400,
    "kit-kate": 10,
    "maaza": 100
}

new_c = c.copy()

print(c)
print(new_c)

# 11.Create a dictionary and use the setdefault() method to add a new key with a default value.

d = {
    "name": "Rahul",
    "age": 26,
    "city": "Kanpur"
}

d.setdefault("hobby","Cricket")
print(d)

# 12.Create a dictionary and print the total number of key-value pairs using the len() function.

c = {
    "oli": 200,
    "mango": 110,
    "bat": 400,
    "kit-kate": 10,
    "maaza": 100
}

print(len(c))

# 13.Create a dictionary and remove all elements using the clear() method.

d = {
    "name": "Sohan",
    "age": 16
}

d.clear()
print(d)

# 14.Create a set containing five numbers and print the set.

s = {1,2,3,4,5}

print(s)

# 15.Create a set and add a new element using the add() method.

a = {6,7,8,9}

a.add(10)
print(a)

# 16.Create two sets and combine them using the update() method.

s1 = {1,2,3,4}
s2 = {5,6,7,8}

s1.update(s2)
print(s1)

# 17.Create a set and remove an element using the remove() method.

s = {1,2,3,4}

s.remove(2)
print(s)

# 18.Create a set and remove an element using the discard() method.

s = {1,2,3,4}

s.discard(2)
print(s)

# 19.Create a set and remove a random element using the pop() method.

s = {5,6,7,8}

s.pop()
print(s)

# 20. Create two sets and perform the following operations:
# Union
# Intersection
# Difference
# Check whether one set is a subset of another
# Check whether one set is a superset of another
# Check whether the two sets are disjoint

s1 = {1,2,3,4}
s2 = {2,6,7,8}

print("Union:",s1.union(s2))
print("Intersection:",s1.intersection(s2))
print("Difference",s1.difference(s2))
print("Subset:",s1.issubset(s2))
print("Superset:",s1.issuperset(s2))
print("Disjoint:",s1.isdisjoint(s2))

# 21.Create a dictionary of five students and their marks. Update the marks of one student.

marks = {
    "Rohan": 90,
    "Sumit": 92,
    "Amit": 88,
    "Mohan": 84,
    "Sohan": 91
}

marks.update({"Mohan": 94})
print(marks)

# 22.Create a set from a list containing duplicate values and print the set.

l = [1,2,3,4,2,5,4,6]

s = set(l)
print(s)

# 23.Create a dictionary and check whether a key exists using the get() method.

d = {
    "name": "Sumit",
    "age": 28
}

print(d.get("city"))

# 24.Create three sets and check whether any two sets are disjoint.

s1 = {1,2,3}
s2 = {4,5,2}
s3 = {6,7,8}

print(s2.isdisjoint(s3))

# 25.Create two sets and print only the elements that are present in the first set but not in the second using the difference() method.

s1 = {1,2,3}
s2 = {4,5,2}

print(s1.difference(s2))