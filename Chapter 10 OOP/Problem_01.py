# Create a class "Programmer" for storing information of few programmers working
# at Microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Akash",1500000,273010)
print(p.company,p.name,p.salary,p.pin)

a = Programmer("Aditya",100000,841101)
print(a.company,a.name,a.salary,a.pin)