# find greater
a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 1: "))
a3 = int(input("Enter number 1: "))
a4 = int(input("Enter number 1: "))
if(a1>a2 and a2>a3 and a3>a4):
    print(f"{a1} is greatest number")
elif(a2>a1 and a1>a3 and a3>a4):
    print(f"{a2} is greatest")
elif(a3>a4 and a4>a1 and a1>a2):
    print(f"{a3} is greatest")
else:
    print(f"{a4} is greatest")