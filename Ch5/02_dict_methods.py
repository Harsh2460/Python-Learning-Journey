marks = {
    "Harry": 100,
    "Shubham": 90,
    "Rohan": 88,
    0 : "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

# Differece
# print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error

# marks.pop("Rohan")
# print(marks)

# marks.popitem() # Last item deleted
# print(marks)

# marks.clear()
# print(marks)

# new_marks = marks.copy()
# print(new_marks)

# marks.setdefault("Sumit",92)
# print(marks)

print(len(marks))