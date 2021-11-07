from configure import Button, Frame
from tkinter import messagebox, ttk


class SuggestionView(Frame):
    def __init__(self, callback_all_suggestion, callback_delete, master=None):
        super(SuggestionView, self).__init__(master)
        self.all_suggestion = callback_all_suggestion
        self.delete_sug = callback_delete
        self.start = self.all_suggestion()
        self.end = self.all_suggestion()
        self.item = 4
        self.li_sug = []
        self.node = None

        frm = Frame(self)
        frm.grid(row=0, column=0)
        self.tree = ttk.Treeview(frm, show="headings", selectmode="browse")
        self.tree["column"] = ("NAME", "NC", "TEXT", "TIME")
        self.tree.heading("NAME", text="Name")
        self.tree.heading("NC", text="National Code")
        self.tree.heading("TEXT", text="Text")
        self.tree.heading("TIME", text="Time")
        self.tree.grid(row=0, column=0)

        frm1 = Frame(self)
        frm1.grid(row=1, column=0)
        Button(frm1, text="Next", command=self.next_page).grid(row=0, column=1)
        Button(frm1, text="Prev", command=self.prev_page).grid(row=0, column=0)

        frm2 = Frame(self)
        frm2.grid(row=2, column=0)
        Button(frm2, text="Delete", command=self.delete_suggestion).grid(row=0, column=0)
        self.next_page()

    def delete_suggestion(self):
        select = self.tree.selection()
        if select == ():
            messagebox.showerror("error", "please select one suggestion")
        ID = self.tree.item(select)["text"]
        node = self.li_sug[int(ID)]
        print(ID)
        for it in self.li_sug:
            print(it.node.data.reseller.name)
        node.delete_node()
        self.delete_sug(node.node.data)

    def next_page(self):
        if self.end.node.next is None:
            return
        self.start = self.end.copy()
        count = 0
        self.li_sug = []
        self.tree.delete(*self.tree.get_children())
        self.nod = None
        for it in self.end.traverse():
            self.nod = self.end.copy()
            self.li_sug.append(self.nod)
            ite = (it.reseller.name, str(it.reseller.national_code), it.text, str(it.time))
            self.tree.insert("", "end", value=ite, text=str(count))
            if count >= self.item:
                self.end.next()
                break
            count += 1

    def prev_page(self):
        if self.start.node.prev is None:
            return
        self.end = self.start.copy()
        self.start.prev()
        self.li_sug = []
        count = 0
        self.nod = None
        self.tree.delete(*self.tree.get_children())
        for it in self.start.traverse(True):
            self.nod = self.start.copy()
            self.li_sug.append(self.nod)
            ite = (it.reseller.name, str(it.reseller.national_code), it.text, str(it.time))
            self.tree.insert("", 0, value=ite, text=str(count))
            if count >= self.item:
                break
            count += 1
