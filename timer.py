#countdown timer
import time
def fun():
    a = int(input("Enter the time in seconds:"))
    while a:
        mins,secs = divmod(a,60)
        b = '{:02d}:{:02d}'.format(mins,secs)
        print(b, end = "\r")
        time.sleep(1)
        a-=1
    print("\nFinished!...\n")
fun()
repeat = input("Do you want to you use this timer again?(yes/no)").lower()
while repeat=="yes":
    fun()
    repeat = input("Do you want to you use this timer again?(yes/no)").lower()
else:
    print("Thankyou")
