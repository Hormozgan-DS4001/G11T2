from configure import Button, Label, Frame
from tkinter import messagebox, ttk
import tkinter


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
        self.tree = ttk.Treeview(self.frm8, show="headings", selectmode="browse", height=10)
        self.tree["column"] = ("text", "time", "manager seen")
        self.tree.heading("text", text="TEXT")
        self.tree.heading("time", text="TIME")
        self.tree.heading("manager seen", text="SEEN")
        self.tree.grid(row=0, column=0)

        frm4 = Frame(self)
        frm4.grid(row=3, column=0)
        Button(frm4, text="Next", command=self.next_page).grid(row=0, column=1)
        Button(frm4, text="Prev", command=self.prev_page).grid(row=0, column=0)
        self.next_page()

    def next_page(self):
        if not self.end.has_next():
            return
        self.start = self.end.copy()
        count = 0
        self.tree.delete(*self.tree.get_children())
        for it in self.end.traverse():
            if it.is_delete:
                ite = (it.text, str(it.time), "+")
            else:
                ite = (it.text, str(it.time), "-")
            self.tree.insert("", "end", value=ite)
            if count >= self.item:
                break
            count += 1

    def prev_page(self):
        if not self.start.has_prev():
            return
        self.end = self.start.copy()
        count = 0
        self.tree.delete(*self.tree.get_children())
        for it in self.start.traverse(True):
            if it.is_delete:
                ite = (it.text, str(it.time), "+")
            else:
                ite = (it.text, str(it.time), "-")
            self.tree.insert("", 0, value=ite)
            if count >= self.item:
                break

    def add_sug(self):
        text = self.box.get("1.0", "end")
        if len(text) < 5:
            messagebox.showerror("error", "you must write more than 5 character")
            return

        self.callback_add_sug(self.callback_user, text)
        self.next_page()
