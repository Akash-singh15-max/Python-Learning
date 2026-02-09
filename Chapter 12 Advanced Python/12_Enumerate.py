l = [123,534,656,90]
# index = 0
# for i in l:
#     print(f"The item number at index {index} is {i}")
#     index+=1

# The above can be done easily by using enumerate function
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")