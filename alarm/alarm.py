import os
from datetime import datetime
import time
def saat_kur(saat,dakika):
    while True:
        if datetime.now().strftime("%H:%M") == f"{saat}:{dakika}":
            print("uyu")
            break

def alarm_kur(saat=0,dakika=0):
    for i in range(1,saat+1):
        time.sleep(3600)
        print("bir saat doldu")
        print(f"kalan süre --> {saat - i} saat {dakika} dakika")
    for i in range(dakika):
        time.sleep(60)
        if dakika - (i+1) <= 10:
            print(f"son {dakika - (i+1)} dakika")
    print("UYAN")
    for i in range(20):
        os.system("start alarm.mp4")
        time.sleep(15)



alarm_kur(0,5)

#saat_kur("05","41")
#alarm_kur(saat=2,dakika=20)
    