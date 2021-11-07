from configure import Entry, Frame, LabelFrame, Button, Label, Tk
from Manager.manager_suggestion import SuggestionView
from Manager.store_panel import StorePanel
from Manager.create_store import CreateStore
from tkinter import ttk, messagebox


class ManagerView(Tk):
    def __init__(self, callback_all_stores, callback_all_users, callback_all_suggestion, callback_create_store,
                 callback_search_store, callback_new_user, callback_delete_sug):
        super(ManagerView, self).__init__()
        self.all_stores = callback_all_stores
        self.all_users = callback_all_users
        self.all_suggestion = callback_all_suggestion
        self.create_store = callback_create_store
        self.search_store = callback_search_store
        self.new_user = callback_new_user
        self.delete_sug = callback_delete_sug
        self.end = self.all_stores()
        self.start = self.end.copy()
        self.item = 5

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        self.main_tab = Frame(self)
        self.main_tab.grid(row=0, column=0)
        self.not_tab.add(self.main_tab, text="Manager")

        frm_lbl = LabelFrame(self.main_tab)
        frm_lbl.grid(row=0, column=1)

        frm1 = Frame(frm_lbl)
        frm1.grid(row=0, column=0)
        Label(frm1, text="Store Code:").grid(row=0, column=0, padx=10)
        self.entry_cs = Entry(frm1)
        self.entry_cs.grid(row=0, column=1, padx=5)

        frm2 = Frame(frm_lbl)
        frm2.grid(row=1, column=0)
        Button(frm2, text="Search", command=self.store_search).grid(row=0, column=0, pady=3)
        Button(frm2, text="Suggestion", command=self.suggestion_view).grid(row=0, column=1, pady=3)

        frm3 = Frame(frm_lbl)
        frm3.grid(row=2, column=0)
        self.tree = ttk.Treeview(frm3, show="headings", selectmode="browse")
        self.tree["column"] = ("SC", "ADDRESS")
        self.tree.heading("SC", text="Store Code")
        self.tree.heading("ADDRESS", text="Address")
        self.tree.grid(row=0, column=0)
        self.tree.bind("<Double-1>", self.double)

        frm4 = Frame(frm_lbl)
        frm4.grid(row=3, column=0)
        Button(frm4, text="prev", command=self.prev_page).grid(row=0, column=0)
        Button(frm4, text="next", command=self.next_page).grid(row=0, column=1, sticky="w")

        frm5 = Frame(frm_lbl)
        frm5.grid(row=4, column=0)
        Button(frm5, text="New Store", command=self.new_store).grid(row=0, column=0)

        self.next_page()

    def double(self, even):
        result = self.tree.selection()
        if result == ():
            return
        ID, address = self.tree.item(result)["values"]
        panel = StorePanel(self.search_store(ID), self.all_users, self.new_user, self.not_tab)
        self.not_tab.add(panel, text=ID)
        self.not_tab.select(panel)
        self.tree.selection_remove()

    def suggestion_view(self):
        panel = SuggestionView(self.all_suggestion, self.delete_sug, self.not_tab)
        self.not_tab.add(panel, text="Suggestion")

    def store_search(self):
        cs = self.entry_cs.get()
        if cs == "":
            return
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

    def next_page(self):
        if not self.end.has_next():
            return
        self.start = self.end.copy()
        count = 0
        self.tree.delete(*self.tree.get_children())
        for it in self.end.traverse():
            ite = (str(it.code), it.address)
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
            ite = (str(it.code), it.address)
            self.tree.insert("", 0, value=ite)
            if count >= self.item:
                break

    def new_store(self):
        panel = CreateStore(self.create_store, self.not_tab)
        self.not_tab.add(panel)
        self.not_tab.select(panel)
