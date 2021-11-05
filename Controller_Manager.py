from DS import Core
from Manager import ManagerView


database = Core()
# database.create_store("afdafaf")
# database.create_store("afdafafdasf")
# database.create_store("afdafafgds")
# database.create_store("afdafafuyuju")
# database.create_store("afdafafuyuju")
# database.create_store("afdafafuyuju")
# database.create_store("afdafafuyuju")


tk = ManagerView(database.show_stores, database.show_all_reseller, database.view_suggestion, database.create_store
                 , database.search_store, database.create_new_reseller)

tk.mainloop()

