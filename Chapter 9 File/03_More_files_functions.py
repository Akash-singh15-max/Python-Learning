f = open("akash.txt","r")
lines = f.readlines()
print(lines,type(lines))
f.close()


# we can use this process also 
# line = f.readline()
# while(line!=""):
#     print(line)
#     line = f.readline()
# f.close()