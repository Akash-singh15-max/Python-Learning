# If we want to made methods in class then we have to use self, whether it is used or not

class Employee:
    language = "Python"    # This is a class attribute
    salary = 1200000 

    def getInfo(self):
        print(f"The language is {self.language}.\nThe salary is: {self.salary}")      
    def greet(self):
        print("Good Morning")
    
    @staticmethod   # decorator
    def greet2():
        print("Thank you")
    # This means that greet2 is a static method and it doesn't need any properties
    # of object

akash = Employee()
akash.language = "JavaScript"
akash.greet()

akash.getInfo()
# Employee.getInfo(akash)

akash.greet2()