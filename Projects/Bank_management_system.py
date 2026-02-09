import os
import pickle

ACCOUNT_FILE = "account.dat"

class Account:
    def __init__(self,name,acc_no,balance=0.0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

def clear_screen():
    os.system("cls")

def create_account():
    try:
        with open(ACCOUNT_FILE,"ab+") as file:
            name = input("\nEnter your name : ").strip()
            acc_no = int(input("Create your account number : "))
            acc = Account(name,acc_no)
            pickle.dump(acc,file)   # The line pickle.dump(acc, file) in Python is used to serialize and store an object in a binary file using the pickle module.
            print("\nAccount created successfully!")

    except Exception as e:
        print(f"Error: {e}")

def deposite_money():
    try:
        acc_no = int(input("\nEnter your account number : "))
        money = float(input("Enter the amount to deposite : "))
        accounts = []
        found = False

        with open(ACCOUNT_FILE, "rb") as file:
            while True:
                try:
                    acc = pickle.load(file)
                    if acc.acc_no == acc_no:
                        acc.balance += money
                        found = True
                    accounts.append(acc)
                except EOFError:
                    break

        with open(ACCOUNT_FILE,"wb") as file:
            for acc in accounts:
                pickle.dump(acc,file)
        if found:
            print(f"\nSuccessfully deposited Rs.{money}")
        else:
            print(f"\nAccount number {acc_no} not found")

    except Exception as e:
        print(f"Error: {e}")

def withdraw_money():
    try:
        acc_no = int(input("\nEnter your account number : "))
        money = float(input("Enter the amount you wish to withdrawn : "))
        accounts = []
        found = False

        with open (ACCOUNT_FILE,"rb") as file:
            while True:
                try:
                    acc = pickle.load(file)
                    if acc.acc_no == acc_no:
                        if acc.balance >= money:
                            acc.balance -= money
                            found = True
                            print(f"\nSuccessfully withdrawn Rs.{money}")
                        else:
                            print("\nInsufficient balance")
                    accounts.append(acc)
                except EOFError:
                    break
        with open (ACCOUNT_FILE,"wb") as file:
            for acc in accounts:
                pickle.dump(acc,file)
            
        if not found:
            print(f"\nAccount number {acc_no} not found.")

    except Exception as e:
        print(f"Error: {e}")

def check_money():
    try:
        acc_no = int(input("\nEnter your account number : "))
        found = False

        with open (ACCOUNT_FILE,"rb") as file:
            while True:
                try:
                    acc = pickle.load(file)
                    if acc.acc_no == acc_no:
                        print(f"\nYour current balance is Rs.{acc.balance}")
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            print(f"\nAccount number {acc_no} not found.")
    
    except Exception as e:
        print(f"Error: {e}")



def main():
    clear_screen()
    while True:
        print("\n***Bank Management System***")
        print("\n1. Create account")
        print("2. Deposite money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit Bank")
        choice = int(input("\nEnter your choice : "))

        if choice==1:
            clear_screen()
            create_account()
        elif choice==2:
            clear_screen()
            deposite_money()
        elif choice==3:
            clear_screen()
            withdraw_money()
        elif choice==4:
            clear_screen()
            check_money()
        elif choice==5:
            print("\nExiting the Bank!")
            print("Thanks for your visit...")
            return
        else:
            print("\nIncorrect choice")

if __name__ == "__main__":
    main()