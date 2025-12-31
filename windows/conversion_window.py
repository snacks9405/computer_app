from tkinter import *
from tkinter.ttk import *
from time import strftime

class WindowFeetToMeters:
    def __init__(self, parent_app):
            self.parent_app = parent_app

            self.top = Toplevel(self.parent_app.root)
            self.top.title("Feet to Meters")
            # self.top.geometry("400x300")

            self.mainframe = Frame(self.top, padding=(3, 3, 12, 12))
            self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

            self.feet = StringVar()
            self.feet_entry = Entry(self.mainframe, width=7, textvariable=self.feet)
            self.feet_entry.grid(column=2, row=1, sticky=(W, E) )

            self.meters = StringVar()
            Label(self.mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

            Button(self.mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

            Label(self.mainframe, text="feet").grid(column=3, row=1, sticky=W)
            Label(self.mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
            Label(self.mainframe, text="meters").grid(column=3, row=2, sticky=W)

            self.time_label = Label(self.mainframe, text="clock")
            self.time_label.grid(column=1, row=1, sticky=(N, W))

            self.top.columnconfigure(0, weight=1)
            self.top.rowconfigure(0, weight=1)
            self.mainframe.columnconfigure(2, weight=1)
            for child in self.mainframe.winfo_children():
                child.grid_configure(padx=5, pady=5)

            self.feet_entry.focus()
            Button(self.mainframe, text="Done", command=self.top.destroy).grid(column=2, row=4, sticky=( W, E))
            self.top.bind("<Return>", self.calculate)
            self.timer()
    
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(round(0.3048 * value, 4))
        except ValueError:
            pass
    def timer(self):
         if self.top.winfo_exists():
            timer_tick = strftime("%I:%M:%S")
            self.time_label.configure(text=timer_tick)
            self.time_label.after(1000, self.timer)
