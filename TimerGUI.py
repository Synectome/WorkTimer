from tkinter import *
import datetime


def time():
    time_string = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    lbl.config(text=time_string)
    lbl.after(1000, time)


root = Tk()

root.geometry("800x200")
frame = Frame(root)
frame.pack()

leftframe = Frame(root, bd=2, bg="#38ba41")
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text="Your on the clock")
label.pack(pady=4)

button1 = Button(leftframe, text="Start", width=8, bg="#18d9ac")
button1.pack(padx=3, pady=3)
button2 = Button(leftframe, text="Pause", width=8, bg="#18d9ac")
button2.pack(padx=3, pady=3)
button3 = Button(leftframe, text="Log Task", width=8, bg="#18d9ac")
button3.pack(padx=3, pady=3)
button4 = Button(leftframe, text="Stop", width=8, bg="#18d9ac")
button4.pack(padx=3, pady=3)

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='#38ba41',
            foreground='black',
            height=2)
lbl.pack(anchor='center', pady=12)
time()

root.title("Work Timer")
root.mainloop()
