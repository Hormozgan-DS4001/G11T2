from DS import Core, Reseller
from GUI_login import LoginWindow
from Reseller import ResellerView

database = Core()
user1 = database.create_new_reseller("kamand", 1234, "123")
stor1 = database.create_store("f10")
database.create_store("f11")
database.create_store("f12")
database.create_store("f13")
database.create_store("f14")
database.create_store("f15")
database.create_store("f16")
uer1 = database.create_new_reseller("kamand", 4562, "kargar")
uer2 = database.create_new_reseller("kasra", 456572, "kargar")
uer3 = database.create_new_reseller("keyvan", 45602, "kh")
uer4 = database.create_new_reseller("mamad", 45162, "kargar")
database.add_suggestion(uer1, "hallo")
database.add_suggestion(uer2, "hallo hi")
s1 = database.add_suggestion(uer3, "hallo how are you")
database.delete_sug(s1)
database.add_suggestion(user1, "faksfalkalk")
stor = database.create_store("dbd")
stor2 = database.create_store("dnd")
stor3 = database.create_store("dndgfsd")
stor4 = database.create_store("dndadadf")
stor5 = database.create_store("dndaggdg")
stor6 = database.create_store("dndcvvbdb")
stor7 = database.create_store("dndqrtqer")
stor2.add_reseller(uer3, 320.2)
stor.add_reseller(uer3, 100.2)
stor3.add_reseller(uer3, 65.1)
stor4.add_reseller(uer3, 96.1)
stor5.add_reseller(user1, 54.3)
stor6.add_reseller(user1, 56.0)
stor7.add_reseller(user1, 3647.0)
print(user1.stores_list)



def add_suggestion(user: "Reseller", text):
    database.add_suggestion(user, text)


def successfully_login(user: "Reseller"):
    login.destroy()
    win_reseller = ResellerView(user, user.show_stores_user, add_suggestion, user.view_suggestion())
    win_reseller.mainloop()


login = LoginWindow(database.login, successfully_login)
login.mainloop()





