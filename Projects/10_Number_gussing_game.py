import random

n = random.randint(1,100)
a = -1
guess = 0
while (a != n):
    a = int(input("\nGuess the number : "))
    if(a>n):
        print("\nLower number please!")
        guess+=1
    elif(a<n):
        print("\nHigher number please")
        guess+=1
    else:
        print(f"\nYou have successfully guess the number {n} correctly in {guess} attempts.")