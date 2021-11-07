from GUI_login import LoginWindow
from Reseller import ResellerView
from DS import Core, Reseller

database = Core()


def add_suggestion(user: "Reseller", text):
    database.add_suggestion(user, text)


def successfully_login(user: "Reseller"):
    login.destroy()
    win_reseller = ResellerView(user, user.show_stores_user, add_suggestion, user.view_suggestion())
    win_reseller.mainloop()


login = LoginWindow(database.login, successfully_login)
login.mainloop()
