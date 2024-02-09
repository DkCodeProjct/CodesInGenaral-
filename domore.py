import time

""" //saw this on Utube short's while serching for time
     module,, coolCode, **and comment's as my understanding the code** """

def countdown(timeSec):
    while timeSec:
        
        min,sec = divmod(timeSec, 60) #kind of 
        timeFormat = '{:02d}:{:02d}'.format(min,sec)
        print(timeFormat,end='\r')
        
        time.sleep(0.5) #what speed you wanna countDown
        timeSec -= 1

    print('doomed')

countdown(5)