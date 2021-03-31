import os
import csv
import datetime
from tkinter import *
from TimerGUI import *
from Curtain import *


if __name__ == "__main__":
    root = Tk()
    root.geometry("760x230")
    app = App(root)
    root.title("Work Timer")
    root.mainloop()