# Can you change the self parameter inside a class to something else (say "Akash"),
# try changing self to "slf" or "Akash" and see the effects.

# Anser:- No change

from random import randint
class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    def book(Akash, fro, to):
        print(f"Ticket is booked in Train no: {Akash.trainNo} from {fro} to {to}.")
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    def getFare(self, fro, to):
        print(f"Ticket fare in Train no: {self.trainNo} from {fro} to {to} is {randint(222,55555)}")
        
t = Train(15027)
t.book("Gorakhpur","Sonpur")
t.getStatus()
t.getFare("Gorakhpur","Sonpur")