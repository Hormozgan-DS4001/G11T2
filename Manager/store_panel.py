from configure import Entry, Label, Button, Frame
from tkinter import ttk, messagebox


class StorePanel(Frame):
    def __init__(self, store_object, callback_resellers, callback_create_reseller, master=None):
        super(StorePanel, self).__init__(master)
        self.store = store_object
        self.resellers_list = callback_resellers
        self.new_reseller = callback_create_reseller
        self.item = 5
        self.start = callback_resellers()
        self.end = self.start.copy()
        self.list_res = []

        sc = self.store.code
        address = self.store.address
        if not self.store.reseller:
            name_reseller = "nobody"
            time = "-"
            rant = "-"
            nc_reseller = "-"

        else:
            name_reseller = self.store.reseller.name
            nc_reseller = str(self.store.reseller.national_code)
            time = str(self.store.time)
            rant = str(self.store.rant)

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(frm1, text=f"Store Address {sc}: {address}").grid(row=0, column=0)
        Label(frm1, text=f"Reseller: {name_reseller}").grid(row=1, column=0)

        frm2 = Frame(self)
        frm2.grid(row=1, column=0)
        Label(frm2, text=f"National Code: {nc_reseller}").grid(row=0, column=0)
        Label(frm2, text=f"Contract Time: {time}").grid(row=1, column=0)
        Label(frm2, text=f"Rant Amount: {rant}").grid(row=1, column=1)

        frm3 = Frame(self)
        frm3.grid(row=2, column=0)
        Button(frm3, text="Add Reseller", command=self.add_reseller).grid(row=0, column=0)
        Button(frm3, text="Delete Reseller", command=self.delete_reseller).grid(row=0, column=1)

        frm4 = Frame(self)
        frm4.grid(row=4, column=0)
        self.tree = ttk.Treeview(frm4, show="headings", selectmode="browse")
        self.tree["column"] = ("Name", "National Code")
        self.tree.heading("Name", text="Name")
        self.tree.heading("National Code", text="National Code")
        self.tree.grid(row=0, column=0)
        Button(frm4, text="Next", command=self.next_page).grid(row=1, column=1)
        Button(frm4, text="Prev", command=self.prev_page).grid(row=1, column=0)

        frm5 = Frame(self)
        frm5.grid(row=3, column=0)
        Label(frm5, text="Rant Amount:").grid(row=0, column=0)
        self.ent_rant = Entry(frm5)

    def add_reseller(self):
        select = self.tree.selection()
        if self.store.reseller:
            messagebox.showerror("error", "this store have reseller")
            return
        if select == ():
            messagebox.showerror("error", "please select one reseller")
            return

        self.ent_rant.grid(row=0, column=1)
        res = self.ent_rant.get()

        if res == "":
            messagebox.showerror("error", "please enter rant")
            return

        ID = self.tree.item(select)["text"]

        user = self.list_res[int(ID)]
        self.store.add_reseller(user, float(res))

    def delete_reseller(self):
        result = messagebox.askokcancel("Sure", f"are you sure delete this reseller")
        if result:
            self.store.delete_reseller()

    def next_page(self):
        if not self.end.has_next():
            return
        self.start = self.end.copy()
        count = 0
        self.list_res = []
        self.tree.delete(*self.tree.get_children())
        for it in self.end.traverse():
            ite = (it.name, it.national_code)
            self.list_res.append(it)
            self.tree.insert("", "end", value=ite, text=str(count))
            if count >= self.item:
                break
            count += 1

    def prev_page(self):
        if not self.start.has_prev():
            return
        count = 0
        self.list_res = []
        self.end = self.start.copy()
        self.tree.delete(*self.tree.get_children())
        for it in self.start.traverse(True):
            ite = (it.name, it.national_code)
            self.list_res.append(it)
            self.tree.insert("", "end", value=ite, tag=count)
            if count >= self.item:
                break
            count += 1




