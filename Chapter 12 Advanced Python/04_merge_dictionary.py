# New operator | and |= allow for merging and updating dictonaries.

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
merged = dict1 | dict2
print(merged) # output: {'a':1, 'b':2, 'c':3, 'd':4}