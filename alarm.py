import datetime
import winsound
from win10toast import ToastNotifier

timing=input("Enter time in ( Hours:Minutes ) \n use 24hrs format = ")
message=input("Type the purpose of the alarm = ")

while True:
    current_time=datetime.datetime.now()
    alarm_time=str(current_time.hour)+":"+str(current_time.minute)

    if alarm_time==timing:
        notification=ToastNotifier()
        winsound.Beep(frequency=200,duration=1000)
        notification.show_toast("Alarm",message,duration=50)
        break
    

