from configure import Button, Label, Frame, Entry, LabelFrame
import tkinter
from tkinter import messagebox


class SuggestionView(Frame):
    def __init__(self, callback_user, callback_add_suggestion, callback_view_suggestion):
        super(SuggestionView, self).__init__()
        self.callback_add_sug = callback_add_suggestion
        self.callback_user = callback_user
        self.end = callback_view_suggestion()
        self.start = self.end
        self.item = 2

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(frm1, text="* Please enter your new SUGGESTION in box *")

        frm2 = Frame(self)
        frm2.grid(row=1, column=0)
        self.box = tkinter.Text(height=6, width=25, bd=2)
        self.box.grid(row=0, column=0)
        Button(frm2, text="Add Suggestion", command=self.add_sug).grid(row=1, column=0)

        self.frm3 = Frame(self)
        self.frm3.grid(row=2, column=0)

        frm4 = Frame(self.frm3)
        frm4.grid(row=1, column=0)
        Button(frm4, text="Next", command=self.next_page).grid(row=0, column=0)
        Button(frm4, text="Prev", command=self.prev_page).grid(row=0, column=1)

    def next_page(self):
        if self.end.node.next is None:
            return
        self.start = self.end.copy()
        for widget in self.frm3.winfo_children():
            widget.destroy()
        count = 0
        for it in self.start.traverse():
            frm = Suggestion(self.frm3, it)
            frm.pack(side="bottom")
            if count >= self.item:
                self.end.next()
                break

    def prev_page(self):
        if self.end.node.next is None:
            return
        for widget in self.frm3.winfo_children():
            widget.destroy()
        self.end = self.start.copy()
        self.start.prev()
        count = 0
        for it in self.end.traverse():
            frm = Suggestion(self.frm3, it)
            frm.pack(side="bottom")
            if count >= self.item:
                break

    def add_sug(self):
        text = self.box.get("1.0", "end")
        if len(text) < 5:
            messagebox.showerror("error", "you must write more than 5 character")
            return

        self.callback_add_sug(self.callback_user, text)
        self.next_page()


class Suggestion(Frame):
    def __init__(self, master, callback_suggestion):
        super(Suggestion, self).__init__(master)
        self.config(bd=3)
        self.node = callback_suggestion
        data = callback_suggestion.get()
        delete = data.is_delete
        time = data.time
        text = data.text

        text_box = tkinter.Text(self, width=25)
        text_box.grid(row=0, column=0)
        text_box.insert(0, text)
        text_box.insert("end", f"\n{str(time)}")
        if delete:
            text_box.insert("end", f"\n*this message seen by manager")







