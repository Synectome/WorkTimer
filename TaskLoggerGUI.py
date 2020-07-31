from tkinter import *
import os
import csv
import datetime


def task_submition(state, root_or_start=False, entr1=False, entr2=False):
    logtime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if state == 'start':
        # Timer Starting
        data = [logtime, 'Day Starting', '00:00:00']
    elif state == 'pause':
        # pause button initiated
        data = [logtime, 'Break started', root_or_start]
    elif state == 'unpause':
        # unpause initiated
        data = [logtime, 'Break ended', root_or_start]
    elif state == 'stop':
        None
    elif state == 'log':
        task_name = entr1.get()
        description = entr2.get()
        data = [logtime, task_name, description]
    else:
        return 'a huge fucking error'

    cwd = os.getcwd()
    filename = "timerlog.csv"
    filepath = os.path.join(cwd, filename)
    if os.path.exists(filepath):
        # open with append
        with open(filename, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    else:
        # open with write
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerows([["Time", "TaskName", "Description"], data])
    if state == 'log':
        # regular log entry form closure
        root_or_start.destroy()


def task_log_window():
    root = Tk()
    root.geometry("300x300")

    frame = Frame(root)
    frame.pack()

    my_entry = Entry(frame, width=20)
    my_entry.insert(0, 'Task Name')
    my_entry.pack(padx=5, pady=5)

    my_entry2 = Entry(frame, width=30)
    my_entry2.insert(0, 'Description')
    my_entry2.pack(padx=5, pady=5)

    button1 = Button(frame, text="Submit Log", width=8, bg="#18d9ac",
                     command=lambda: task_submition(root, my_entry, my_entry2))
    button1.pack(padx=3, pady=3)

    root.title("Log Entry Form")
    root.mainloop()