class Employee:
    company = "ITC"
    name = "Akash"
    salary = 1000000
    def show(self):
        print(f"The name is {self.name}\nThe salary is {self.salary}")

class Programmer(Employee):     # Inheritance employee class in programmer class
    company = "ITC InfoTech"
    language = "JavaScript"
    def showlanguage(self):
        print(f"The name is {self.name}\nHe is good with {self.language} language")


a = Employee()
b = Programmer()
print(a.company,b.company)

a.show(),b.show(),b.showlanguage()