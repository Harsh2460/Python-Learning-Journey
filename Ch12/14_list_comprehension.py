myList = [1,2,9,5,3,5]

# squareList = []
# for item in myList:
#     squareList.append(item*item)

# This can be simplified using List Comprehension
squareList = [i*i for i in myList]

print(squareList)