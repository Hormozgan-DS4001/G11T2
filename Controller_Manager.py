from Manager import ManagerView
from DS import Core

database = Core()

tk = ManagerView(database.show_stores, database.show_all_reseller, database.view_suggestion, database.create_store,
                 database.search_store, database.create_new_reseller, database.delete_sug
                 )

tk.mainloop()
