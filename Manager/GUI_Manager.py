from configure import Entry, Frame, LabelFrame, Button, Label, Tk
from tkinter import ttk, messagebox
import tkinter


class ManagerView(Tk):
    def __init__(self, callback_all_stores, callback_all_users, callback_all_suggestion, callback_create_store,
                 callback_search_store, callback_new_user):
        super(ManagerView, self).__init__()
        self.all_stores = callback_all_stores
        self.all_users = callback_all_users
        self.all_suggestion = callback_all_suggestion
        self.create_store = callback_create_store
        self.search_store = callback_search_store
        self.new_user = callback_new_user

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        self.main_tab = Frame(self)
        self.main_tab.grid(row=0, column=0)
        self.not_tab.add(self.main_tab)

        frm_lbl = LabelFrame(self.main_tab)
        frm_lbl.grid(row=0, column=1)

        frm1 = Frame(frm_lbl)
        frm1.grid(row=0, column=0)
        Label(frm1, text="Store Code: ").grid(row=0, column=0)
        self.entry_cs = Entry(frm1)
        self.entry_cs.grid(row=0, column=1, padx=5)

        frm2 = Frame(frm_lbl)
        frm2.grid(row=1, column=0)
        Button(frm2, text="Search", command=self.store_search).grid(row=0, column=0)

        frm3 = Frame(frm_lbl)
        frm3.grid(row=2, column=0)
        self.tree = ttk.Treeview(frm3)
        self.tree["column"] = ("SC", "ADDRESS")
        self.tree.heading("SD", text="Store Code")
        self.tree.heading("ADDRESS", text="Address")
        self.tree.grid(row=0, column=0)

        frm4 = Frame(frm_lbl)
        frm4.grid(row=3, column=0)
        Button(frm4, text="prev", command=self.prev_page).grid(row=0, column=0)
        Button(frm4, text="next", command=self.next_page).grid(row=0, column=1)

    def store_search(self):
        cs = self.entry_cs.get()
        if not cs.isnumeric:
            messagebox.showerror("error", "please enter number")
            self.entry_cs.delete(0, "end")
            return
        if not 1 <= int(cs) <= 200:
            messagebox.showerror("error", "please enter number between 1 and 200")
            self.entry_cs.delete(0, "end")
            return

        result = self.search_store(int(cs))
        self.tree.delete(*self.tree.get_children())
        finish = (cs, result.address)
        self.tree.insert("", "end", value=finish)























