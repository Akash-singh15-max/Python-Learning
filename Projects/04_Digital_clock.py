# Digital clock
from datetime import datetime

now = datetime.now()
currentTime = now.strftime("%H:%M:%S %p")
currentDate = now.strftime("%A, %d %B %Y")
print("Current time :",currentTime)
print("Current date :",currentDate)