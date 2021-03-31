from tkinter import *
from Curtain import *


class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.leftframe = Frame(root, bd=2, bg="#38ba41")
        self.leftframe.pack(side=LEFT, padx=8)
        self.rightframe = Frame(root, bd=2, bg="#38ba41")
        self.rightframe.pack(side=RIGHT, padx=8)

        self.heading = Label(frame, text="Your on the clock")
        self.heading.pack(pady=4)

        self.start_button = Button(self.leftframe, text="Start", width=8, bg="#18d9ac", command=start_timer)
        self.start_button.pack(padx=3, pady=3)
        self.shift_timer = Label(self.leftframe, font=('calibri', 12, 'bold'),
                            background="#18d9ac",
                            foreground='black',
                            height=1)
        self.shift_timer.pack(padx=3, pady=3)
        time_since(self)
        self.pause_button = Button(self.leftframe, text="Pause", width=8, bg="#18d9ac", command=lambda: pause_timer(self))
        self.pause_button.pack(padx=3, pady=3)
        self.button3 = Button(self.leftframe, text="Log Task", width=8, bg="#18d9ac", command=self.task_log_window)
        self.button3.pack(padx=3, pady=3)
        self.button4 = Button(self.leftframe, text="Stop", width=8, bg="#18d9ac", command=lambda: stop(root))
        self.button4.pack(padx=3, pady=3)

        self.clock_label = Label(self.rightframe, font=('calibri', 40, 'bold'),
                            background="#18d9ac",
                            foreground='black',
                            height=2)
        self.clock_label.pack(anchor='center', pady=12)
        # clock_label.place(anchor='center', relx=0.5, rely=0.5)
        time(self)

    def task_log_window(self):
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
                         command=lambda: task_submition('log', root, my_entry, my_entry2))
        button1.pack(padx=3, pady=3)

        root.title("Log Entry Form")
        root.mainloop()