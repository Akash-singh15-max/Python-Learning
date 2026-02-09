class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)
# print(o.b) # show an error as there is no b attribute in Employee class

o = Programmer()
print(o.a)
print(o.b)

a = Manager()
print(a.a,a.b,a.c)