from configure import Entry, Button, Tk, Frame, Label
from tkinter import messagebox


class LoginWindow(Tk):
    def __init__(self, callback_login, callback_successfully):
        super(LoginWindow, self).__init__()

        self.callback_login = callback_login
        self.callback_successfully = callback_successfully

        self.title("Login")
        self.resizable(False, False)
        self.geometry("500x500+200+200")

        f_np = Frame(self).grid(row=0, column=0)
        Label(f_np, text="National Code: ").grid(row=0, column=0, sticky="w")
        self.entry_name = Entry(f_np)
        self.entry_name.grid(row=0, column=1)
        Label(f_np, text="password: ").grid(row=1, column=0, sticky="w")
        self.entry_password = Entry(f_np, show="*")
        self.entry_password.grid(row=1, column=1)

        self.lbl = Label(self, text="", fg="#ff0000")

        Button(self, text="login", command=self.cmd_login).grid(row=3, column=1, pady=10)

    def cmd_login(self):
        national_code = self.entry_name.get()
        password = self.entry_password.get()

        if national_code.isnumeric():
            national_code = int(national_code)

        else:
            self.message("National code or Password is wrong")

        user = self.callback_login(national_code, password)
        if user:
            self.callback_successfully(user)

        else:
            self.message("National code or Password is wrong")

    def message(self, text):
        self.lbl.config(text=text)
        self.lbl.grid(row=2, column=1)
        self.lbl.after(4000, self.disappear)

    def disappear(self):
        self.lbl.config(text="")
        self.lbl.grid_forget()





