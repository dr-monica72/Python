from datetime import datetime
import speech_recognition as sr


i=0
while (i==0):
    ch=str(input("What's your command: "))
    if ch=="hey friday":
        print("What's up, Boss")
    elif ch=="hey buddy":
        print("Yes, Boss")
    elif ch=="hey bud":
        print("Good to see you too, sir")
    elif ch=="fri":
        time = datetime.now().time()
        print("Current time is:",time)
    elif ch=="day":
        today=datetime.today()
        print("Today's date is: ",today)
    elif ch=="stop":
        i=1
        print("Bye Sir")
    elif ch=="glad to have you back buddy":
        print("That's my Pleasure, Boss")