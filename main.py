# import time
#
# my_time = int(input("Enter the time in seconds: "))
#
# for x in (range(my_time, 0, -1)):
#     seconds = x % 60
#     minutes = int(x/60) % 60
#     hours = int(x / 3600)
#     print(f"{hours}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#
# print("Time's up")

from tkinter import *
from playsound import playsound
import time

root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False, False)

heading = Label(root, text="Timer", font="Comfortaa 25 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

# Clock
Label(root, font=("Comfortaa", 15, "bold"), text="Current Time:", bg="papaya whip").place(x=40, y=70)


def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font=("Comfortaa", 15, "bold"), text="", fg="#000", bg="#fff")
current_time.place(x=190, y=70)
clock()

# Timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="Comfortaa 50", bg="#000", fg="#fff", bd=0).place(x=30, y=155)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable=mins, width=2, font="Comfortaa 50", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
mins.set("00")

secs = StringVar()
Entry(root, textvariable=secs, width=2, font="Comfortaa 50", bg="#000", fg="#fff", bd=0).place(x=270, y=155)
secs.set("00")

Label(root, text="hrs", font="Comfortaa 12", bg="#000", fg="#fff").place(x=105, y=230)
Label(root, text="min", font="Comfortaa 12", bg="#000", fg="#fff").place(x=225, y=230)
Label(root, text="sec", font="Comfortaa 12", bg="#000", fg="#fff").place(x=345, y=230)

def Timer():
    timer = int(hrs.get())*3600 + int(mins.get())*60+int(secs.get())

    while timer > -1:
        minute,second=(timer//60, timer%60)

        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)

        secs.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if (timer == 0):
            playsound("timer.mp3")
            secs.set("00")
            mins.set("00")
            hrs.set("00")

        timer -= 1




def brush():
    hrs.set("00")
    mins.set("02")
    secs.set("00")


def face():
    hrs.set("00")
    mins.set("15")
    secs.set("00")


def eggs():
    hrs.set("00")
    mins.set("10")
    secs.set("00")



button = Button(root, text="Start", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="Comfortaa 10 bold", command=Timer)
button.pack(padx=5, pady=40, side=BOTTOM)


Image1 = PhotoImage(file="brush.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=brush)
button1.place(x=7, y=300)

Image2 = PhotoImage(file="face.png")
button1 = Button(root, image=Image2, bg="#000", bd=0, command=face)
button1.place(x=137, y=300)

Image3 = PhotoImage(file="eggs.png")
button1 = Button(root, image=Image3, bg="#000", bd=0, command=eggs)
button1.place(x=267, y=300)

root.mainloop()
