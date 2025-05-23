import time
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
h = int(input("Enter the hour part of countdown: "))
m = int(input("Enter the minute part: "))
s = int(input("Enter the seconds part: "))
total = h * 3600 + m * 60 + s
while total >= 0:
    hrs = total // 3600
    mins = (total % 3600) // 60
    secs = total % 60
    print(f"{hrs}:{mins}:{secs}")
    time.sleep(1)
    total=total-1

print("Time's up!")
speaker.speak("Time's up")
