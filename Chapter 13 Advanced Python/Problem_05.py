# Write a program to find out the maximum of the numbers in
# a list using the reduce function.

from functools import reduce
l = [12,4,89,232,52,999,0,69]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))