# Easy Level Practice Questions

# 1.Create a list containing five fruits and print the list.

fruits = ["Mango","Orange","Banana","Grapes","Apple"]
print(fruits)

# 2.Create a list of five numbers and print:
# First element
# Third element
# Last element

num = [78,88,86,94,90]

print(num[0])
print(num[2])
print(num[-1])

# 3.Create a list of colors and print:
# Last element
# Second last element

c = ["Red","Green","Yellow","Orange","White"]

print(c[-1])
print(c[-2])

# 4.Create a list of numbers from 1 to 10 and print:
# First 5 elements
# Last 5 elements

n = [1,2,3,4,5,6,7,8,9,10]

print(n[:5])
print(n[-5:])

# 5.Create two lists and concatenate them into a new list.

l1 = [1,2,3,4]
l2 = [5,6,7,8]

print(l1 + l2)

# 6.Create a list containing "Python" and repeat it 4 times using the repetition operator.

list = ["Python"]

print(list * 4)

# 7.Create a list of fruits and check whether "Apple" is present in the list.

fruits = ["Mango","Orange","Banana","Grapes","Apple"]

print("Apple" in fruits)

# 8.Create a list of six elements and print its length using len().

fruits = ["Mango","Orange","Banana","Grapes","Apple","Watermellon"]

print(len(fruits))

# 9.Create a list of numbers and print:
# Maximum value
# Minimum value

list = [88,76,84,904,90,426,568,86]

print(max(list))
print(min(list))

# 10.Create a list of numbers and print the sum of all elements.

list1 = [6,4,8,5,7,2]

print(sum(list1))

# 11.Create an empty list and add three numbers using the append() method.

list = []

list.append(1)
list.append(4)
list.append(8)

print(list)

# 12.Create a list of four numbers and insert 100 at index 2.

num = [10,92,284,8]

num.insert(2,100)
print(num)

# 13.Create a list of colors and remove "Blue" from the list.

colors = ["Red","Green","Yellow","Blue","Orange","White"]

colors.remove("Blue")
print(colors)

# 14.Create a list of five numbers and remove the last element using pop().

numbers = [6,4,8,5,7]

numbers.pop()
print(numbers)

# 15.Create a list of numbers in random order and sort them in ascending order.

numbers = [6,4,8,5,7]

numbers.sort()
print(numbers)

# 16.Create a list of numbers and reverse the order of the list.

num = [10,20,30,40,50]

num.reverse()
print(num)

# 17.Create a list and count how many times the number 5 appears.

n = [1,2,3,5,4,8,5,6,9]

print(n.count(5))

# 18.Create a list of fruits and find the index of "Mango".

fruits = ["Orange","Banana","Mango","Grapes","Apple"]

print(fruits.index("Mango"))

# 19.Create two lists:
# Clear the first list.
# Extend it using the second list.

l1 = [1,2,3,4]
l2 = [5,6,7,8]

l1.clear()
l1.extend(l2)
print(l1)

# 20.Create a tuple of five numbers and perform the following:
# Print the first element
# Print the last element
# Print the length of the tuple
# Print the maximum value
# Print the minimum value
# Print the sum of all elements

t = (4,2,10,8,6)

print(t[0])
print(t[-1])
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

# 21.Create a tuple and print:
# First three elements
# Last three elements

t = (1,2,3,4,5,6,7,8)

print(t[:3])
print(t[-3:])

# 22.Create two tuples and concatenate them.

t1 = (1,2,3,4)
t2 = (5,6,7,8)

print(t1 + t2)

# 23.Repeat a tuple three times using the repetition operator.

t1 = (1,2,3,4)

print(t1 * 3)

# 24.Check whether the number 20 is present in a tuple.

t1 = (10,20,30,40)

print(20 in t1)

# 25.Create a tuple (10, 20, 30, 20, 40) and:
# Count the occurrences of 20
# Find the index of the first occurrence of 20

tuple = (10,20,30,20,40)

print(tuple.count(20))
print(tuple.index(20))