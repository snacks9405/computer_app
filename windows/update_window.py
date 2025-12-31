from tkinter import *
from tkinter.ttk import *

class WindowUpdate:
    def __init__(self, parent_app):
        #store reference to main window class instance
        self.parent_app = parent_app

        #create toplevel window
        self.top = Toplevel(self.parent_app.root)
        self.top.title("Update Data")
        self.top.geometry("300x150")

        #access variable
        Label(self.top, text="Enter new text").pack(pady=10)

        #entry and button to update main window
        self.entry = Entry(self.top, textvariable=self.parent_app.vars["user_text"])
        self.entry.pack(pady=5)
        self.entry.focus_set()
        self.top.bind("<Return>", self.top.destroy)

        Button(self.top, text="Done", command=self.top.destroy).pack(pady=10)

    def update_main(self):
        self.parent_app.shared_data.set(self.new_entry.get())
        self.top.destroy()