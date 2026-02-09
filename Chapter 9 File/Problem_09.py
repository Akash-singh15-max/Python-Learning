# Write a program to find out whether the file is identical and matches 
# the content of another file

with open("this.txt","r") as f:
    content1 = f.read()

with open("this_copy.txt","r") as f:
    content2 = f.read()

if(content1==content2):
    print("Both files have same content")
else:
    print("Contents of both file doesn't similar")