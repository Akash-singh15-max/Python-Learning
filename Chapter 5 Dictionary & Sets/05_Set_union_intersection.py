s1 = {1,45,8,79}
s2 = {7,9,1,79}
print(s1.union(s2))
print(s1.intersection(s2))

print({1,79}.issubset(s1))
print({3,6}.issubset(s2))

print(s1.issuperset({1,8}))