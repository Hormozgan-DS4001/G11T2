from configure import Tk, Frame, Button, Entry, Label, LabelFrame


class ResellerView(Tk):
    def __init__(self, callback_user, callback_show_stores,
                 callback_add_suggestion, callback_show_suggestion
                 ):
        super(ResellerView, self).__init__()

        self.callback_user = callback_user
        self.callback_show_stores = callback_show_stores
        self.callback_show_suggestion = callback_show_suggestion
        self.callback_add_sug = callback_add_suggestion

        self.title("Reseller")
        self.geometry("500x500+200+200")
        self.resizable(False, False)

        frm1 = Frame(self)
        frm1.grid(row=0, column=0)
        Label(text=f"Name: {callback_user.name}").grid(row=0, column=0)
        Label(text=f"National Code: {callback_user.national_code}").grid(row=1, column=0)

        Button(self, text="Add Suggestion", command=self.sug_cmd)

    def sug_cmd(self):
        pass










