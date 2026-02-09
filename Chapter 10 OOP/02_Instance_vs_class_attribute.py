class Employee:
    language = "Python"    # This is a class attribute
    salary = 1200000 

akash = Employee()
akash.language = "JavaScript" # This is an instance attribute
print(akash.language,akash.salary)

# instances attributes get preference over class attributes