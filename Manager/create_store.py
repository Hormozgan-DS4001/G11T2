from configure import Label, Entry, Button, Frame
from tkinter import messagebox


class CreateStore(Frame):
    def __init__(self, create_store, master=None):
        super(CreateStore, self).__init__(master)
        self.create = create_store

        frm = Frame(self)
        frm.grid(row=0, column=0)
        Label(frm, text="Enter Address: ").grid(row=0, column=0)
        self.entry = Entry(frm)
        self.entry.grid(row=0, column=1)

        frm1 = Frame(self)
        frm1.grid(row=1, column=0)
        Button(frm1, text="Add", command=self.add_store).grid(row=0, column=0)

    def add_store(self):
        result = self.entry.get()
        if result == "":
            messagebox.showerror("error", "please enter address")
            return
        self.create(result)
        self.entry.delete(0, "end")


