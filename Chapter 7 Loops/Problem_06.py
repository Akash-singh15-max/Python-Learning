# Write a program to calculate the factorial of given number using
# for loops

# 5! = 1*2*3*4*5

n = int(input("Enter any number: "))


fact = 1
for i in range(1,n+1):
    fact*=i
    
print(f"The factorial of {n} is {fact}")