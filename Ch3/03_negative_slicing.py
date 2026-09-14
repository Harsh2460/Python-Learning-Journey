name = "Harry"

print(name[0:3])

print(name[-4:-1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])

# Slicing with skip value
word = "amazing"

print(word[0:6:2])
print(word[1:7:3])

print(word[::-1]) # Reverse a String