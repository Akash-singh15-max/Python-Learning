# Write a python function which convert inches to cms.

def con(inch):
    return inch*2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {con(n)}")