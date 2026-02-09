myList = [1,29,5,3,5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# this above can be done easily by list comprehension
squaredList = [i*i for i in myList]

print(squaredList)