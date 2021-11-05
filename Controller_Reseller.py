from DS import Core, Reseller, Suggestion, Store
from GUI_login import LoginWindow
from GUI_Reseller import ResellerView

database = Core()
user1 = database.create_new_reseller("kamand", 1234, "123")
database.add_suggestion(user1, "faksfalkalk")
stor = database.create_store("dbd", "200")
stor2 = database.create_store("dnd", "500")
stor3 = database.create_store("dndgfsd", "500")
stor4 = database.create_store("dndadadf", "500")
stor5 = database.create_store("dndaggdg", "500")
stor6 = database.create_store("dndcvvbdb", "500")
stor7 = database.create_store("dndqrtqer", "500")
stor.add_reseller(user1)
stor2.add_reseller(user1)
stor3.add_reseller(user1)
stor4.add_reseller(user1)
stor5.add_reseller(user1)
stor6.add_reseller(user1)
stor7.add_reseller(user1)
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





