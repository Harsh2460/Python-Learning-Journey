# Revision

# 1.Create a dictionary of student details.

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

student = {
    "Name": name,
    "Age": age,
    "Course": course
}

print(student)

# 2.Print all dictionary keys.

student = {
    "name" : "Rohan",
    "age" : 28
}

print(student.keys())

# 3.Print all dictionary values.

student = {
    "name" : "Rohan",
    "age" : 28
}

print(student.values())

# 4.Update a dictionary.

student = {
    "name" : "Rohan",
    "age" : 28
}

city = input("Enter city: ")

student.update({"City": city})
print(student)

# 5.Remove a key using pop().

student = {
    "name" : "Rohan",
    "age" : 28
}

student.pop("age")
print(student)

# 6.Create a set and add three new elements.

s = set()

s.add(int(input("Enter element: ")))
s.add(int(input("Enter element: ")))
s.add(int(input("Enter element: ")))

print(s)

# 7.Find the union of two sets.

s1 = {1,2,3}
s2 = {4,2,6}

print(s1.union(s2))

# 8.Find the intersection of two sets.

s1 = {1,2,3}
s2 = {4,2,6}

print(s1.intersection(s2))

# 9.Find the difference between two sets.

s1 = {1,2,3}
s2 = {4,2,6}

print(s1.difference(s2))

# 10.Check whether one set is a subset of another.

s1 = {1,2,3}
s2 = {1,2,3,4,5}

print(s1.issubset(s2))