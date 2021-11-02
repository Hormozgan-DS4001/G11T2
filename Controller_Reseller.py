from DS import Core
from GUI_login import LoginWindow
from GUI_Reseller import ResellerView

database = Core()


def successfully_login(user):
    pass


login = LoginWindow(database.login, successfully_login)
login.mainloop()





