from tkinter import *
from TaskLoggerGUI import *
import datetime

init_time = 0
init_break = 0
on_break = False
timing_on = False
since_start = False
time_mod = False


def start_timer():
    global init_time
    global timing_on
    timing_on = True
    init_time = datetime.datetime.now()
    task_submition('start')


def break_duration():
    return stringify_timedate(datetime.datetime.now() - init_break)


# change the task submition function to handle 'states' rather than all these true false statements
def pause_timer():
    global timing_on
    global init_break
    print(pause_button.config('text')[-1])
    if pause_button.config('text')[-1] == 'Unpause':
        print('now weere unpausing')
        task_submition('unpause', root_or_start=break_duration())
        timing_on = True
        pause_button.config(text='Pause')
    else:
        print('now were pausing')
        init_break = datetime.datetime.now()
        task_submition('pause', root_or_start=init_break)
        timing_on = False
        pause_button.config(text='Unpause')


def stringify_timedate(dt):
    seconds = dt.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return'{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))  # since.strftime("%H:%M:%S")


def time_since():
    cwt = datetime.datetime.now()
    global timing_on
    global since_start
    global time_mod

    if timing_on:
        since_start = cwt - init_time
        lbl2.config(text=stringify_timedate(since_start))
        lbl2.after(1000, time_since)
        time_mod = True
    elif ((not timing_on) and since_start) and time_mod:
        lbl2.config(text=stringify_timedate(since_start))
        lbl2.after(1000, time_since)
        time_mod = False
    else:
        lbl2.config(text='--/--/--')
        lbl2.after(1000, time_since)
        time_mod = True


def time():
    time_string = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    lbl1.config(text=time_string)
    lbl1.after(1000, time)


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

button1 = Button(leftframe, text="Start", width=8, bg="#18d9ac", command=start_timer)
button1.pack(padx=3, pady=3)
lbl2 = Label(leftframe, font=('calibri', 12, 'bold'),
             background="#18d9ac",
             foreground='black',
             height=1)
lbl2.pack(padx=3, pady=3)
time_since()
pause_button = Button(leftframe, text="Pause", width=8, bg="#18d9ac", command=pause_timer)
pause_button.pack(padx=3, pady=3)
button3 = Button(leftframe, text="Log Task", width=8, bg="#18d9ac", command=task_log_window)
button3.pack(padx=3, pady=3)
button4 = Button(leftframe, text="Stop", width=8, bg="#18d9ac")
button4.pack(padx=3, pady=3)

lbl1 = Label(root, font=('calibri', 40, 'bold'),
            background='#38ba41',
            foreground='black',
            height=2)
lbl1.pack(anchor='center', pady=12)
time()

root.title("Work Timer")
root.mainloop()
