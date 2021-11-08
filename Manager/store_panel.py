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
        self.end = callback_resellers()
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
        Label(frm1, text=f"Store Address {sc}:     {address}").grid(row=0, column=0, sticky="w", pady=3)
        Label(frm1, text=f"Reseller:                  {name_reseller}").grid(row=1, column=0, sticky="w", pady=3)
        Label(frm1, text=f"National Code:        {nc_reseller}").grid(row=2, column=0, sticky="w", pady=3)
        Label(frm1, text=f"Contract Time:        {time}").grid(row=3, column=0, sticky="w", pady=3)
        Label(frm1, text=f"Rant Amount:          {rant}").grid(row=4, column=0, sticky="w", pady=3)

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

        frm5 = Frame(self)
        frm5.grid(row=5, column=0)
        Button(frm5, text="Next", command=self.next_page).grid(row=1, column=1)
        Button(frm5, text="Prev", command=self.prev_page).grid(row=1, column=0)

        frm5 = Frame(self)
        frm5.grid(row=3, column=0)
        Label(frm5, text="Rant Amount:").grid(row=0, column=0)
        self.ent_rant = Entry(frm5)
        self.ent_rant.grid(row=0, column=1)

        frm6 = Frame(self)
        frm6.grid(row=6, column=0)
        Label(frm6, text="Name: ").grid(row=0, column=0)
        self.ent_name = Entry(frm6)
        self.ent_name.grid(row=0, column=1)
        Label(frm6, text="National code: ").grid(row=1, column=0)
        self.ent_nc = Entry(frm6)
        self.ent_nc.grid(row=1, column=1)
        Label(frm6, text="password: ").grid(row=2, column=0)
        self.ent_pas = Entry(frm6)
        self.ent_pas.grid(row=2, column=1)
        Label(frm6, text="create password: ").grid(row=3, column=0)
        self.ent_CPas = Entry(frm6)
        self.ent_CPas.grid(row=3, column=1)
        Button(frm6, text="Add New Reseller", command=self.new_user).grid(row=4, column=0)

        self.next_page()

    def add_reseller(self):
        select = self.tree.selection()
        if self.store.reseller:
            messagebox.showerror("error", "this store have reseller")
            self.tree.selection_remove()
            return
        if select == ():
            messagebox.showerror("error", "please select one reseller")
            self.tree.selection_remove()
            return

        res = self.ent_rant.get()
        if res == "":
            messagebox.showerror("error", "please enter rant")
            self.tree.selection_remove()
            return

        ID = self.tree.item(select)["text"]

        user = self.list_res[int(ID)]
        self.store.add_reseller(user, float(res))
        self.next_page()

    def delete_reseller(self):
        result = messagebox.askokcancel("Sure", f"are you sure delete this reseller")
        if result:
            self.store.delete_reseller()
        self.tree.selection_remove()

    def next_page(self):
        if self.start is None:
            return
        if not self.end.has_next():
            return
        self.tree.delete(*self.tree.get_children())
        self.start = self.end.copy()
        self.list_res = []
        count = 0
        for it in self.end.traverse():
            if it == 0:
                continue
            ite = (it.name, it.national_code)
            self.list_res.append(it)
            self.tree.insert("", "end", value=ite, text=count)
            if count >= self.item:
                break
            count += 1

    def prev_page(self):
        if self.start is None:
            return
        if not self.start.has_prev():
            return
        count = 0
        self.end = self.start.copy()
        self.tree.delete(*self.tree.get_children())
        self.list_res = []
        for it in self.start.traverse(True):
            if it == 0:
                continue
            ite = (it.name, it.national_code)
            self.list_res.append(it)
            self.tree.insert("", 0, value=ite, text=count)
            if count >= self.item:
                break
            count += 1

    def new_user(self):
        name = self.ent_name.get()
        nat_code = self.ent_nc.get()
        password = self.ent_pas.get()
        create_pass = self.ent_CPas.get()
        if not nat_code.isnumeric():
            messagebox.showerror("error", "please enter correct national code")
            self.ent_nc.delete(0, "end")
            return
        if password != create_pass:
            messagebox.showerror("error", "tow password is not same")
            self.ent_pas.delete(0, "end")
            self.ent_CPas.delete(0, "end")
            return
        self.new_reseller(name, int(nat_code), create_pass)
        self.ent_name.delete(0, "end")
        self.ent_nc.delete(0, "end")
        self.ent_pas.delete(0, "end")
        self.ent_CPas.delete(0, "end")


