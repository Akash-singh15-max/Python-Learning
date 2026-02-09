# Write down the program to find out the line number where python is
# present from question 6

line = 1
with open("log.txt") as f:
    lines = f.readlines()
line_no = 1
for line in lines:
    if("python" in line):
        print(f"Yes, python is present in line number {line_no}")
        break
    line_no+=1
else:
    print(f"No, python is not present")