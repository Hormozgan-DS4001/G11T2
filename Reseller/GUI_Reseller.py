from configure import Tk, Frame, Button, Entry, Label, LabelFrame
from tkinter import ttk
from Reseller.Suggestion_View import SuggestionView


class ResellerView(Tk):
    def __init__(self, callback_user, callback_show_stores,
                 callback_add_suggestion, callback_show_suggestion
                 ):
        super(ResellerView, self).__init__()

        self.callback_user = callback_user
        self.callback_show_suggestion = callback_show_suggestion
        self.callback_add_sug = callback_add_suggestion
        self.start = callback_show_stores(callback_user)
        print(type(self.start))
        self.end = self.start
        self.item = 2

        self.title("Reseller")
        self.geometry("500x500+200+200")
        # self.resizable(False, False)

        self.not_tab = ttk.Notebook(self)
        self.not_tab.grid(row=0, column=0)
        self.not_main = Frame(self)
        self.not_main.grid(row=0, column=0)
        self.not_tab.add(self.not_main, text="Home")

        frm_lbl = LabelFrame(self.not_main)
        frm_lbl.grid(row=0, column=1)

        frm1 = Frame(frm_lbl)
        frm1.grid(row=0, column=0)
        Label(frm1, text=f"Name: {callback_user.name}").grid(row=0, column=0)
        Label(frm1, text=f"National Code: {callback_user.national_code}").grid(row=1, column=0)

        frm2 = Frame(frm_lbl)
        frm2.grid(row=1, column=0)
        Button(frm2, text="Suggestion", command=self.sug_cmd).grid(row=0, column=0)

        frm3 = Frame(frm_lbl)
        frm3.grid(row=2, column=0)
        self.tree_view = ttk.Treeview(frm3, show="headings", selectmode="browse", height=10)
        self.tree_view["column"] = ("SC", "AR")
        self.tree_view.heading("SC", text="Store Code")
        self.tree_view.heading("AR", text="Amount of Rant")
        self.tree_view.grid(row=0, column=0)

        frm4 = Frame(frm_lbl)
        frm4.grid(row=3, column=0)
        Button(frm4, text="Next", command=self.next_page).grid(row=0, column=1)
        Button(frm4, text="Prev", command=self.prev_page).grid(row=0, column=0)
        self.next_page()

    def next_page(self):
        if self.end.node.next is None:
            return
        self.tree_view.delete(*self.tree_view.get_children())
        self.start = self.end.copy()
        count = 0
        for it in self.end.traverse():
            if it.reseller != self.callback_user:
                it.delete()
                continue
            ite = (it.code, it.rant)
            self.tree_view.insert("", "end", value=ite)
            if count >= self.item:
                self.end.next()
                break
            count += 1

    def prev_page(self):
        if self.start.node.prev is None:
            return
        self.end = self.start.copy()
        self.tree_view.delete(*self.tree_view.get_children())
        self.start.prev()
        count = 0
        for it in self.start.traverse(True):
            if it.reseller != self.callback_user:
                it.delete()
                continue
            ite = (it.code, it.rant)
            self.tree_view.insert("", 0, value=ite)
            if count >= self.item:
                break
            count += 1

    def sug_cmd(self):
        panel = SuggestionView(self.callback_user, self.callback_add_sug, self.callback_show_suggestion, self.not_tab)
        self.not_tab.add(panel, text="suggestion")
        self.not_tab.select(panel)










