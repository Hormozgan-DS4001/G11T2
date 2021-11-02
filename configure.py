import tkinter as tk


class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#C9DBBA"

        if "relief" not in kwargs:
            kwargs["relief"] = "groove"

        if "activebackground" not in kwargs:
            kwargs["activebackground"] = "#9FDBC4"

        if "width" not in kwargs:
            kwargs["width"] = 15

        if "bd" not in kwargs:
            kwargs["bd"] = 2

        super(Button, self).__init__(master, **kwargs)


class Entry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        if "bd" not in kwargs:
            kwargs["bd"] = 2

        if "bg" not in kwargs:
            kwargs["bg"] = "#CEDBB6"
        super(Entry, self).__init__(master, **kwargs)


class Tk(tk.Tk):
    def __init__(self):
        super(Tk, self).__init__()
        self.config(bg="#E3D8A8")


class Frame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E3D8A8"
        super(Frame, self).__init__(master, kwargs)


class Label(tk.Label):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E3D8A8"
        super(Label, self).__init__(master, kwargs)


class LabelFrame(tk.LabelFrame):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E3D8A8"
        super(LabelFrame, self).__init__(master, kwargs)





