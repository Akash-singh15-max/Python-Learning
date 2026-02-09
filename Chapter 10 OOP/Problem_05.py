# Write a class Train which has methods to book a ticket, get status(no of seats)
# and get fare information of train running under Indian Railays.
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Ticket is booked in Train no: {self.trainNo} from {fro} to {to}.")
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    def getFare(self, fro, to):
        print(f"Ticket fare in Train no: {self.trainNo} from {fro} to {to} is {randint(222,55555)}")
        
t = Train(15027)
t.book("Gorakhpur","Sonpur")
t.getStatus()
t.getFare("Gorakhpur","Sonpur")