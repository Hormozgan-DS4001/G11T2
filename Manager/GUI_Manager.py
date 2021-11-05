from configure import Entry, Frame, LabelFrame, Button, Label, Tk
from tkinter import ttk
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


