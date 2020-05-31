import datetime
from time import sleep

def getDateTime():
    date , time = str(datetime.datetime.now()).split()
    year ,month, day = date.split("-")
    hour , minute , second = time[:8].split(":") 
    
    
