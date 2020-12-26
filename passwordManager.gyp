import tkinter as Tk

class PasswordManager:

    def __init__(self):
        self.root = Tk.Tk()
        self.canvas = Tk.Canvas(self.root, width = 500, height = 500)
        self.canvas.pack()
        
        