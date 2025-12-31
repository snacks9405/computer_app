import os
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

class WindowMap:
    def __init__(self, parent_app):
        self.parent_app = parent_app
        self.top = Toplevel(self.parent_app.root)
        self.top.title("Map View")
        self.top.geometry("400x300")

        self.img_path = "images/map.png"

        if os.path.exists(self.img_path):
            pil_img = Image.open(self.img_path)
            pil_img = pil_img.resize((350,200), Image.Resampling.LANCZOS)

            self.tk_img = ImageTk.PhotoImage(pil_img)

            img_label = Label(self.top, image=self.tk_img)
            img_label.image = self.tk_img
            img_label.pack(pady=20)
        else:
            Label(self.top, text="Error: map.png not found in /images folder", foreground="red").pack(pady=50)
        
        Button(self.top, text="Done", command=self.top.destroy).pack()