# Revision

# 1.Find the length of a string.

a = input("Enter string: ")

print("Length:",len(a))

# 2.Convert a string to uppercase.

a = input("Enter string: ")

print("Uppercase:",a.upper())

# 3.Convert a string to lowercase.

a = input("Enter string: ")

print("Lowercase:",a.lower())

# 4.Count the occurrence of a character.

a = input("Enter string: ")

c = input("Enter counts: ")

print("Counts:",a.count(c))

## 5.Replace one word with another.

a = input("Enter string: ")

old = input("Enter old word: ")
new = input("Enter new word: ")

print("Replace:",a.replace(old,new))

# 6.Display the first and last character of a string.

a = input("Enter string: ")

print("First:",a[0])
print("Last:",a[-1])

# 7.Print the first five characters using slicing

a = input("Enter string: ")

print("Five:",a[:5])

# 8.Reverse a string using slicing.

a = input("Enter string: ")

print("Reverse:",a[::-1])

# 9.Check whether a string starts with a given character.

a = input("Enter string: ")

s = input("Enter starting: ")

print("Start:",a.startswith(s))

# 10.Remove extra spaces using strip().

a = input("Enter string: ")

print("Extra:",a.strip())