from DS import Core, Reseller
from GUI_login import LoginWindow
from Reseller import ResellerView

database = Core()
user1 = database.create_new_reseller("kamand", 1234, "123")
database.add_suggestion(user1, "faksfalkalk")
stor = database.create_store("dbd")
stor2 = database.create_store("dnd")
stor3 = database.create_store("dndgfsd")
stor4 = database.create_store("dndadadf")
stor5 = database.create_store("dndaggdg")
stor6 = database.create_store("dndcvvbdb")
stor7 = database.create_store("dndqrtqer")
stor.add_reseller(user1, 100.2)
stor2.add_reseller(user1, 320.2)
stor3.add_reseller(user1, 65.1)
stor4.add_reseller(user1, 96.1)
stor5.add_reseller(user1, 54.3)
stor6.add_reseller(user1, 56.0)
stor7.add_reseller(user1, 3647.0)
print(user1.stores_list)


def show_stores(user: "Reseller"):
    result = user.show_stores_user()
    print(result.node, "ll")
    return result


def add_suggestion(user: "Reseller", text):
    database.add_suggestion(user, text)


def successfully_login(user: "Reseller"):
    login.destroy()
    win_reseller = ResellerView(user, show_stores, add_suggestion, user.view_suggestion())
    win_reseller.mainloop()


login = LoginWindow(database.login, successfully_login)
login.mainloop()





