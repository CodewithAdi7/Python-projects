import time
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
alarm=input("Enter the alarm time as HH:MM \n")
while True:
    current_time=time.strftime("%H:%M")
    if current_time==alarm:
        print("It's time get up !! ")
        speaker.speak("Get up!! ")
        break

