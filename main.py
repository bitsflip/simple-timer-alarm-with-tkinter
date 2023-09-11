import time
from tkinter import *
from tkinter import ttk
from plyer import notification


def sendNotification():
    notification.notify(
    title = 'Timer',
    message = 'your food is done',
    app_icon = None,
    timeout = 10,
    )   

def getTime():
    t = time.strftime("%H:%M:%S")

    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    return hour, minute, seconds



# set time up
def hourUp():
    setHour = int(hourLabel["text"])
    if setHour < 24:
        setH = setHour
        setH = setH + 1
        hourLabel.configure(text=setH)
def minuteUp():
    setMinute = int(minuteLabel["text"])
    if setMinute < 59:
        setM = setMinute
        setM = setM + 1
        minuteLabel.configure(text=setM)
def secondUp():
    setSecond = int(secondLabel["text"])
    if setSecond < 59:
        setS = setSecond
        setS = setS + 1
        secondLabel.configure(text=setS)

# set time down
def hourDown():
    setHour = int(hourLabel["text"])
    if setHour > 0:
        setH = setHour
        setH = setH - 1
        hourLabel.configure(text=setH)
def minuteDown():
    setMinute = int(minuteLabel["text"])
    if setMinute > 0:
        setM = setMinute
        setM = setM - 1
        minuteLabel.configure(text=setM)
def secondDown():
    setSecond = int(secondLabel["text"])
    if setSecond > 0:
        setS = setSecond
        setS = setS - 1
        secondLabel.configure(text=setS)

# remaing time for timer
def getTimer(seconds):

    hours = seconds / 3600
    minutes = float("0." + str(hours).split(".")[1]) * 60
    seconds = float("0." + str(minutes).split(".")[1]) * 60

    hours = str(hours).split(".")[0]
    minutes = str(minutes).split(".")[0]
    seconds = round(seconds)

    

    print(hours)
    print(minutes)
    print(seconds)
    print(f"{hours}:{minutes}:{seconds}")

    return [hours, minutes, seconds]

# timer down
def submit():
    x=0
    hour = int(hourLabel["text"]) *60 *60
    minute = int(minuteLabel["text"])*60
    second = int(secondLabel["text"])
    totalSecond = hour + minute + second
    print(totalSecond)
    if totalSecond != 0:
        while totalSecond != 0:
            totalSecond -= 1
            time.sleep(1)

            hours_left = getTimer(totalSecond)[0]
            minutes_left = getTimer(totalSecond)[1]
            seconds_left = getTimer(totalSecond)[2]
            hourLabel.configure(text=hours_left)
            minuteLabel.configure(text=minutes_left)
            secondLabel.configure(text=seconds_left)
            root.update()

        sendNotification()
        print("DONE!")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

#menu buttons
menuLabel = ttk.Label(frm)
alarmButton = ttk.Button(frm)
timerButton = ttk.Button(frm)

#time labels
hourLabel = ttk.Label(frm)
minuteLabel = ttk.Label(frm)
secondLabel = ttk.Label(frm)


# timer layout
startButton = ttk.Button(frm)


# up buttons
hourUpButton = ttk.Button(frm)
minuteUpButton = ttk.Button(frm)
secondUpButton = ttk.Button(frm)


# down buttons
hourDownButton = ttk.Button(frm)
minuteDownButton = ttk.Button(frm)
secondDownButton = ttk.Button(frm)






def setPos():
    hourLabel.grid(column=0, row=2)
    minuteLabel.grid(column=1, row=2)
    secondLabel.grid(column=2, row=2)
    menuLabel.grid(column= 1, row=0)
    
    hourUpButton.grid(column=0, row=1)
    minuteUpButton.grid(column=1, row=1)
    secondUpButton.grid(column=2, row=1)
    hourDownButton.grid(column=0, row=3)
    minuteDownButton.grid(column=1, row=3)
    secondDownButton.grid(column=2, row=3)

    hourUpButton.configure(text="  ˄  ", command=hourUp)
    minuteUpButton.configure(text="  ˄  ", command=minuteUp)
    secondUpButton.configure(text="  ˄  ", command=secondUp)

    hourDownButton.configure(text="  ˅  ", command=hourDown)
    minuteDownButton.configure(text="  ˅  ", command=minuteDown)
    secondDownButton.configure(text="  ˅  ", command=secondDown)

    startButton.grid(column=1, row=4)

def timerScreen():
    clearScreen()
    setPos()
    

    menuLabel.configure(text="Timer")



    hourLabel.configure(text="0")
    minuteLabel.configure(text="0")
    secondLabel.configure(text="0")



    startButton.configure(text="start", command=submit)
    
    # time labels

def clearScreen():
    alarmButton.grid_forget()
    timerButton.grid_forget()

    hourUpButton.grid_forget()
    minuteUpButton.grid_forget()
    secondUpButton.grid_forget()

    hourDownButton.grid_forget()
    minuteDownButton.grid_forget()
    secondDownButton.grid_forget()

    menuLabel.grid_forget()
    startButton.grid_forget()

    hourLabel.grid_forget()
    minuteLabel.grid_forget()
    secondLabel.grid_forget()

clearScreen()


def alarmScreen():
    clearScreen()
    setPos()

    secondLabel.grid_remove()
    secondDownButton.grid_remove()
    secondUpButton.grid_remove()
    minuteUpButton.grid(column=2,  row=1)
    minuteLabel.grid(column=2,row=2)
    minuteDownButton.grid(column=2, row=3)

    menuLabel.configure(text="ALARM")
    hourLabel.configure(text=getTime()[0])
    minuteLabel.configure(text=getTime()[1])
    secondLabel.configure(text=getTime()[2])

    startButton.grid(column=1, row=4)
    startButton.configure(text="start", command=alarmCheck)


def menuScreen():
    clearScreen()
    menuLabel.grid(column= 1, row=0)
    menuLabel.configure(text="Menu")

    alarmButton.grid(column=3, row=1)
    alarmButton.configure(text="alarm", command=alarmScreen)
    timerButton.grid(column=0, row=1)
    timerButton.configure(text="timer", command=timerScreen)

def alarmCheck():
    hour = int(hourLabel["text"])
    minute = int(minuteLabel["text"])
    print(hour, minute)
    startButton.configure(text="stop", command=menuScreen)
    while True:
        if hour == getTime()[0] and minute == getTime()[1]:
            sendNotification()
            print("alarm doNE")
            break

        time.sleep(10)
        print("check")


menuScreen()


root.mainloop()



#ttk.Label(frm, text="CLOCK").grid(column=0, row=0)

#ttk.Button(frm, text="QUIT", command=getTime).grid(column=0, row=1)
