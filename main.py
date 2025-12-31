import json
import os
from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from windows import *


class MainApp:
    FILENAME = "settings.json"

    DEFAULT_SETTINGS = {
        "user_text": "default placeholder",
        "menu_selection": "Select an Option",
        "total_seconds": 0,
        "lives":0
    }

    def __init__(self, root):
        self.window_map = {
            "Update Value": WindowUpdate,
            "Show Map": WindowMap,
            "Feet to Meters": WindowFeetToMeters,
        }

        self.root = root
        self.root.title("Main Window")
        #self.root.geometry("400x300")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.mainframe = Frame(self.root, padding=(3, 12, 3, 3))
        self.mainframe.grid(column=0, row=0)
        self.mainframe.columnconfigure(0, weight = 1)
        

        saved_data = self.load_data()
        self.vars = {}
        for key, value in self.DEFAULT_SETTINGS.items():
            print(f"key: {key} value: {saved_data.get(key, value)}")
            if isinstance(value, int):
                self.vars[key] = IntVar(value=saved_data.get(key, value))
            else:
                self.vars[key] = StringVar(value=saved_data.get(key, value))

        self.shared_data = StringVar(value=saved_data.get("user_text"))
        self.selection = StringVar(value=saved_data.get("menu_selection"))

        self.time_label = Label(self.mainframe)
        self.time_label.grid(column=0, row=1)

        Label(self.mainframe, text="Stored Data:").grid(column=0, row=2)
        Label(
            self.mainframe, textvariable=self.vars["user_text"], foreground="blue"
        ).grid(column=0, row=3)
        
        # Lives Label
        self.lives_label = Label(self.mainframe, text=f"lives: {self.vars["lives"].get()}")
        self.lives_label.grid(column=1, row=0, sticky=(N, E))

        # Option Menu
        Label(self.mainframe, text="Where you wanna go?").grid(column=0, row=4)
        self.options = ["Update Value", "Show Map", "Feet to Meters"]
        self.options_width = len(max(self.options, key=len)) + 4

        om = OptionMenu(
            self.mainframe, self.vars["menu_selection"], self.vars["menu_selection"].get(), *self.options
        )
        om.config(width=self.options_width)
        om.grid(column=0, row=5, pady=10)

        # Button(self.mainframe, text="clear settings", command=lambda: saved_data.set(DEFAULT_SETTINGS)).grid(row=4)
        # Button(root, text="banana", command=lambda: self.selection.set("banana")).pack()
        # Button(root, text="organe", command=lambda: self.selection.set("organe")).pack()

        Button(
            self.mainframe, text="Open Secondary Window", command=self.open_secondary
        ).grid(column=0, row=6)

        self.timer()

        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

    def timer(self):
        timer_tick = strftime("%I:%M:%S")
        self.time_label.configure(text=timer_tick)
        
        current_seconds = int(self.vars["total_seconds"].get())
        new_seconds = current_seconds + 1
        self.vars["total_seconds"].set(new_seconds)


        NEW_LIFE = 180
        if new_seconds % NEW_LIFE == 0:
            self.give_time_life(new_seconds)
        self.time_label.after(1000, self.timer)

    def give_time_life(self, total):
        minutes = total // 60
        self.vars["lives"].set(self.vars["lives"].get() + 1)
        self.lives_label.configure(text=f"lives: {self.vars["lives"].get()}")
        print(f"+1 life triggered at {minutes} minutes!")
        messagebox.showinfo("Reward!", f"You get +1 life at {minutes} minutes!")

    # loads data from filename
    def load_data(self):
        if os.path.exists(self.FILENAME):
            try:
                with open(self.FILENAME, "r") as f:
                    data = json.load(f)
                    return {**self.DEFAULT_SETTINGS, **data}
            except (json.JSONDecodeError, FileNotFoundError):
                return self.DEFAULT_SETTINGS

    # save data to file
    def save_and_exit(self):
        current_state = {key: var.get() for key, var in self.vars.items()}
        final_data = {**self.DEFAULT_SETTINGS, **current_state}

        try:
            with open(self.FILENAME, "w") as f:
                json.dump(final_data, f, indent=4)
        except Exception as e:
            print(f"Error saving to {self.FILENAME}: {e}")

        self.root.destroy()

    def open_secondary(self):
        choice = self.vars["menu_selection"].get()

        if choice == "Update Value":
            WindowUpdate(self)
        elif choice == "Show Map":
            WindowMap(self)
        elif choice == "Feet to Meters":
            WindowFeetToMeters(self)


if __name__ == "__main__":
    root = Tk()
    #root.minsize(400, 300)
    #root.resizable(False, False)
    app = MainApp(root)
    root.mainloop()
