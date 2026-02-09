class Employee:
    language = "Python"
    salary = 1200000
    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

e = Employee("Akash",1400000,"JavaScript")
print(e.name,e.salary,e.language)