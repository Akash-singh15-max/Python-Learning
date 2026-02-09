# Create a class with a class attribute a; create an object from it and set 'a'
# directly using object.a = 0. Does this change the class attribute

class simple:
    a = 4
o = simple()
print(o.a)  # print class attribute because instance attribute is not present
o.a = 0     # instance attribute is set 
print(o.a)  # print instance attribute because instance attribute is present
print(simple.a)     # 

# Therefore, class attribute doesn't change