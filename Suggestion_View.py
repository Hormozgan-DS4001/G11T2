from configure import Button, Label, Frame, Entry, LabelFrame
import tkinter
from tkinter import messagebox


class SuggestionView(Frame):
    def __init__(self, callback_user, callback_add_suggestion, callback_view_suggestion, master=None):
        super(SuggestionView, self).__init__(master)
        self.callback_add_sug = callback_add_suggestion
        self.callback_user = callback_user
        self.end = callback_view_suggestion
        self.start = self.end.copy()
        self.item = 2

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(frm1, text="* Please enter your new SUGGESTION in box *").grid(row=0, column=0)

        frm2 = Frame(self)
        frm2.grid(row=1, column=0)
        self.box = tkinter.Text(frm2, height=6, width=25, bd=2)
        self.box.grid(row=0, column=0)
        Button(frm2, text="Add Suggestion", command=self.add_sug).grid(row=1, column=0)

        self.frm8 = Frame(self)
        self.frm8.grid(row=2, column=0)

        frm4 = Frame(self)
        frm4.grid(row=3, column=0)
        Button(frm4, text="Next", command=self.next_page).grid(row=0, column=1)
        Button(frm4, text="Prev", command=self.prev_page).grid(row=0, column=0)

    def next_page(self):
        if not self.end.has_next():
            return
        self.start = self.end.copy()
        count = 0
        print(self.start.traverse())
        for it in self.start.traverse():
            frm = Suggestion(self.frm8, it)
            frm.grid(row=count, column=0)
            if count >= self.item:
                break
            count += 1

    def prev_page(self):
        if not self.start.has_prev():
            return
        self.end = self.start.copy()
        count = 0
        for it in self.end.traverse(True):
            frm = Suggestion(self.frm8, it)
            frm.grid(row=count, column=0)
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
        self.config(bd=3, bg="#fff1e6")
        self.node = callback_suggestion
        print(type(callback_suggestion))
        delete = callback_suggestion.is_delete
        time = callback_suggestion.time
        text = callback_suggestion.text

        text_box = tkinter.Text(self, width=20, height=10)
        text_box.grid(row=0, column=0)
        text_box.insert("end", text)
        text_box.insert("end", f"({str(time)})")
        if delete:
            text_box.insert("end", f"(*this message seen by manager)")







