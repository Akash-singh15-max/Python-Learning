'''
    Write a program to print the following star pattern
      *
     ***
    ***** for n = 3 

'''
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(" "*(n-1),end="")     # we use end="", because print statement
                                # bydefault a new line, to prevent new line 
                                # we use end=""
    print("*"*(2*i-1),end="")
    print("")   # we are not using "\n" because print statement itself give
                # a new line