# Write a program to create a dictonary of hindi words with values
# as their english translation. Provide user with an option 
# to look it up!

words = {
    "Ghar":"Home",
    "Khana": "Food",
    "Pila": "Yellow"
}

word = input("Enter the word you want meaning of: ")
print(words[word])