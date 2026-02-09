# Constructor:- It is automatically called
class Employee:
    language = "Python"    # This is a class attribute
    salary = 1200000 

    # __ se start hone wale methods ko python me dunder methods khte hai, which is automatically called
    def __init__(self,name,salary,language): 
            self.name = name
            self.salary = salary
            self.language = language
            print("I am creating an object")

    
akash = Employee("Akash",1500000,"JavaScript")
print(akash.name,akash.salary,akash.language)
