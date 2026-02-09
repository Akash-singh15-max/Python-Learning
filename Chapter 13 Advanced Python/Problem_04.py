# Write a program to filter a list of numbers which is 
# divisible by 5.

l = [5,2,4,15,33,65,88,95,100]
def div(n):
    if(n%5==0):
        return True
    return False
ans = filter(div,l)
print(list(ans))
