# Write a program to read the text from given file 'poems.txt' and find out 
# whether it contain the word 'twinkle'.

with open("poems.txt") as f:
    content = f.read()
    print(content)
    if("twinkle" in content):
        print("\nThe word twinkle is present in the content")
    else:
        print("\nThe word twinkle is not present in the content")