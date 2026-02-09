# Write a python program using function to convert Fahrenheit to Celcius
# C = 5*(f-32)/9
def func():
    f = int(input("Enter the temperature in Celcius: "))
    c = 5*(f-32)/9
    print(c)
    print(f"{round(c,2)} degree C")
func()