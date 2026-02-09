class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()  # super is used to inherit constructor also
        print("Constructor of Manager")
    c = 3

a = Manager()
print(a.a,a.b,a.c)