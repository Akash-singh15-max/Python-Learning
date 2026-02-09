class Employee:
    language = "Python"    # This is a class attribute
    salary = 1200000 

akash = Employee()
print(akash.language,akash.salary) 

aditya = Employee()
aditya.name ="Aditya"   # This is an instance attritute
print(aditya.name,aditya.language,aditya.salary)

# Here name is instance attribute and salary and language are class attributes 
# as they are directly belong to the class