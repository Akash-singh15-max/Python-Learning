# Write a program to find out whether a student has passed or failed if
# it require a total of 40% and atlest 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

s1 = int(input("Enter marks of subject 1 from 100: "))
s2 = int(input("Enter marks of subject 2 from 100: "))
s3 = int(input("Enter marks of subject 3 from 100: "))

ps1 = s1/100 * 100
ps2 = s2/100 * 100
ps3 = s3/100 * 100
p = (s1+s2+s3)/300 * 100

if(p>=40 and ps1>=33 and ps2>=33 and ps3>=33):
    print("Student has passed in exam with percentage ",p)
else:
    print("Student has failed in exam with percentage ",p)