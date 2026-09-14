# Revision

# 1.Create a list of five numbers and print it.

numbers = []

numbers.append(int(input("Enter number 1: ")))
numbers.append(int(input("Enter number 2: ")))
numbers.append(int(input("Enter number 3: ")))
numbers.append(int(input("Enter number 4: ")))
numbers.append(int(input("Enter number 5: ")))

print(numbers)

# 2.Find the maximum element of a list.

l = [1,2,3,4,5]

print("Maximum:",max(l))

# 3.Find the minimum element of a list.

l = [1,2,3,4,5]

print("Minimum:",min(l))

# 4.Find the sum of all elements.

l = [1,2,3,4,5]

print("Sum:",sum(l))

# 5.Sort a list.

l = [2,4,3,1,5]

l.sort()
print("Sorted:",l)

# 6.Reverse a list.

l = [1,2,3,4,5]

l.reverse()
print("Reverse:",l)

# 7.Insert an element at a given index.

l = [1,2,3,4,5]

l.insert(4,8)
print("Insert:",l)

# 8.Remove an element using remove().

l = [1,2,3,4,5]

l.remove(4)
print("Remove:",l)

# 9.Create a tuple and count the occurrence of an element.

l = [2,1,2,3,2,4,5,2]

a = l.count(2)
print("Count:",a)

# 10.Concatenate two tuples.

l1 = [1,2,3,4]
l2 = [5,6,7,8]

print("Concatenation:", l1 + l2)