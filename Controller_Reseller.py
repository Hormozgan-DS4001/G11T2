from GUI_login import LoginWindow
from Reseller import ResellerView
from DS import Core, Reseller
from pickle import load, dump
from os.path import exists as file_exists

if file_exists("database.bin"):
    file = open("database.bin", "rb")
    database = load(file)
    file.close()
else:
    database = Core()


def successfully_login(user: "Reseller"):
    login.destroy()
    win_reseller = ResellerView(user, user.show_stores_user, database.add_suggestion, user.view_suggestion)
    win_reseller.mainloop()


login = LoginWindow(database.login, successfully_login)
login.mainloop()

file = open("database.bin", "wb")
dump(database, file)
file.close()
