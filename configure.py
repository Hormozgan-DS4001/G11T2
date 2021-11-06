import tkinter as tk


class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#D2DFFD"

        if "relief" not in kwargs:
            kwargs["relief"] = "groove"

        if "activebackground" not in kwargs:
            kwargs["activebackground"] = "#C7D7FE"

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
            kwargs["bg"] = "#E8EEFC"
        super(Entry, self).__init__(master, **kwargs)


class Tk(tk.Tk):
    def __init__(self):
        super(Tk, self).__init__()
        self.config(bg="#E2EAFC")


class Frame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"
        super(Frame, self).__init__(master, kwargs)


class Label(tk.Label):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"

        if "font" not in kwargs:
            kwargs["font"] = ('Helvetica', 11, 'bold')
        super(Label, self).__init__(master, kwargs)


class LabelFrame(tk.LabelFrame):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"
        super(LabelFrame, self).__init__(master, kwargs)





