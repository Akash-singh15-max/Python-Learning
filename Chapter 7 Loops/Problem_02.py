# Write a program to greet all the person names stored in a list "l"
# and which start with S.

l = ["Akash","Sumit","Suman","Suresh","Varsha","Aditya"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")