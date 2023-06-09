import time
import pync

def reminder() :
    pync.notify(
        title = "Drink Water Reminder", 
        execute = 'say "Drink Water Now"' , 
        message = "You should drink atleast 3 litres of water a day", 
        timeout = 20
    )

while True:
    reminder()
    time.sleep(60*60)