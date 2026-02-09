# CalculateMyDahej.com
import pyttsx3
import pyaudio

import os
import pickle

ACCOUNT_FILE = "Dahej.com"

class Dahej:
    def __init__(self,name,age,pocket_money,cows,khet,sarkari_naukri):
        self.name = name
        self.age = age
        self.pocket_money = pocket_money
        self.cows = cows
        self.khet = khet
        self.sarkari_naukri = sarkari_naukri

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def clear_screen():
    os.system("cls")

def main():
    clear_screen()
    
    print("\n*** Welcom to CalculateMyDahej.com ***")
    print("\nTell my about yourself : ")
    name = input("\nEnter your name : ").strip()
    age = int(input("Enter your age : "))
    pocket_money = float(input("Enter your pocket money : "))
    khet = int(input("How much khet do you have in acer : "))
    cows = int(input("How much cows do you have : "))
    sarkari_naukri = input("Do you have a sarkari naukri in your family (yes or no) : ")
        
    if(age<18):
        print("Jaaa kar padhaai karo chotu, attharah(18) ke baad aana.")
        speak("Jaaa kar padhaai karo chotu, attharah ke baad aana.")

    elif(age in range(17,26) and pocket_money in range(-1,10001) and 
         khet in range(-1,1) and cows in range(-1,1) and sarkari_naukri == "no"):
        print("\nDahej = 5,000 (Udhar)")
        speak("\nDahej 5000 (Udhar)")
    
    elif(age in range(17,26) and pocket_money in range(-1,10001) and 
         khet in range(-1,6) and cows in range(-1,6) and sarkari_naukri == "no"):
        print("\nDahej = 1,00,000")
        speak("\nDahej Ek Lakh")
    
    
        
    elif(age in range(17,26) and pocket_money in range(9999,50001) and 
        khet in range(-1,1) and cows in range(-1,1) and sarkari_naukri == "no"):
        print("\nDahej = 15,000 (15 Thousand)")
        speak("\nDahej Pandra Hazar")
    
    elif(age in range(17,26) and pocket_money in range(9999,50001) and 
        khet in range(-1,11) and cows in range(-1,11) and sarkari_naukri == "no"):
        print("\nDahej = 20,000 (20 Thousand)")
        speak("\nDahej Bis Hazar")
        
    elif(age in range(17,26) and pocket_money in range(49999,200001) and 
        khet in range(-1,1) and cows in range(-1,1) and sarkari_naukri == "no"):
        print("\nDahej = 25,000 (25 Thousand)")
        speak("\nDahej Pachhis Hazar")

    elif(age in range(17,26) and pocket_money in range(49999,200001) and 
        khet in range(0,11) and cows in range(0,11) and sarkari_naukri == "no"):
        print("\nDahej = 40,000 (40 Thousand)")
        speak("\nDahej Chalis Hazar")

    elif(age in range(17,26) and pocket_money in range(49999,200001) and 
        khet in range(-1,1) and cows in range(-1,1) and sarkari_naukri == "no"):
        print("\nDahej = 35,000 (35 Thousand)")
        speak("\nDahej Paitis Hazar")
        
    elif(age in range(17,25) and pocket_money in range(49999,200001) and 
        khet in range(-1,5) and cows in range(-1,5) and sarkari_naukri == "no"):
        print("\nDahej = 40,000 (40 Thousand)")
        speak("\nDahej Chalis Hazaar")
        


    elif(age in range(17,31) and pocket_money in range(-1,5000) and 
        khet in range(-1,6) and cows in range(-1,6) and sarkari_naukri == "yes"):
        print("\nDahej = 10,00,000 (10 Lakh)")
        speak("\nDahej Das Lakh")
        
    elif(age in range(17,31) and pocket_money in range(-1,5000) and 
        khet in range(-1,11) and cows in range(-1,11) and sarkari_naukri == "yes"):
        print("\nDahej = 20,00,000 (20 Lakh)")
        speak("\nDahej Bis Lakh")

    elif(age in range(17,31) and pocket_money in range(4999,50000) and 
        khet in range(0,11) and cows in range(-1,11) and sarkari_naukri == "yes"):
        print("\nDahej = 35,00,000 (35 Lakh)")
        speak("\nDahej Paitish Lakh")

    elif(age in range(17,31) and pocket_money in range(49999,200001) and 
        khet in range(-1,21) and cows in range(-1,21) and sarkari_naukri == "yes"):
        print("\nDahej = 50,00,000 (50 Lakh)")
        speak("\nDahej Pachaas Lakh")

        


if __name__=="__main__":
    main()
        