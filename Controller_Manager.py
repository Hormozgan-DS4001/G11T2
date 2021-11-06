from DS import Core
from Manager import ManagerView


database = Core()
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
stor1.add_reseller(uer1, 2.2)

tk = ManagerView(database.show_stores, database.show_all_reseller, database.view_suggestion, database.create_store
                 , database.search_store, database.create_new_reseller)

tk.mainloop()

