# Write a program which finds out whether a given name is present in 
# a list or not

l = ["Akash","Sumit","Harry","Aditya","Varsha"]
name = input("Enter the name: ")
if(name in l):
    print(name,"is present in list") # , makes a space after it
else:
    print(name,"is not present in list")