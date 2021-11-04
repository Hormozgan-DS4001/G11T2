from configure import Button, Label, Frame, Entry, LabelFrame
import tkinter
from tkinter import ttk


class SuggestionView(Frame):
    def __init__(self, callback_user, callback_add_suggestion, callback_view_suggestion):
        super(SuggestionView, self).__init__()
        self.callback_add_sug = callback_add_suggestion
        self.callback_list_sug = callback_view_suggestion
        self.callback_user = callback_user
        self.end = callback_view_suggestion()
        self.start = self.end

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(frm1, text="* Please enter your new SUGGESTION in box *")

        frm2 = Frame(self)
        frm2.grid(row=1, column=0)
        self.box = tkinter.Text(height=6, width=25, bd=2)
        self.box.grid(row=0, column=0)
        Button(frm2, text="Add Suggestion", command=self.add_sug).grid(row=1, column=0)

        frm3 = Frame(self)
        frm3.grid(row=2, column=0)
        self.listBox = tkinter.Text(height=8, width=25, bd=5)
        self.listBox.grid(row=0, column=0)
        frm4 = Frame(frm3)
        frm3.grid(row=1, column=0)
        Button(frm4, text="Next", command=self.next_page).grid(row=0, column=0)
        Button(frm4, text="Prev", command=self.prev_page).grid(row=0, column=1)

    def next_page(self):






    def prev_page(self):
        pass

    def add_sug(self):
        pass







