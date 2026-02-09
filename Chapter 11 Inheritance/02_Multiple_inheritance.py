# Multiple Inheritance

class Programmer:
    name = "Akash"
    company = "ITC"
    def show(self):
        print(f"The name of the programmer is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all programming language here is your language: {self.language}")

class Employee(Programmer,Coder):
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
    
a = Programmer()
b = Coder()
c = Employee()

c.show()
c.printLanguage()
c.showlanguage()