from DS import Core
from Manager import ManagerView


database = Core()
stor1 = database.create_store("afdafaf")
database.create_store("afdafafdasf")
database.create_store("afdafafgds")
database.create_store("afdafafuyuju")
database.create_store("afdafafuyuju")
database.create_store("afdafafuyuju")
database.create_store("afdafafuyuju")
uer1 = database.create_new_reseller("kamand", 4562, "kargar")
uer2 = database.create_new_reseller("kamsdafand", 456572, "kargar")
uer3 = database.create_new_reseller("kamfhgand", 45602, "kargar")
uer4 = database.create_new_reseller("kamdsgand", 45162, "kargar")
stor1.add_reseller(uer1, 2.2)

tk = ManagerView(database.show_stores, database.show_all_reseller, database.view_suggestion, database.create_store
                 , database.search_store, database.create_new_reseller)

tk.mainloop()

