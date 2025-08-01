import os
import time


maxTime = 60
timeRemained = maxTime

while(timeRemained > maxTime/2):
    print(timeRemained)
    time.sleep(1)
    timeRemained -= 1

print("get ready")

while(timeRemained <= maxTime/2):
    print(timeRemained)
    time.sleep(1)
    timeRemained -= 1

os.system("shutdown -s -f -t 0")