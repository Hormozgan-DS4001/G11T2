from Manager import ManagerView
from DS import Core
from pickle import load, dump
from os.path import exists as file_exists

if file_exists("database.bin"):
    file = open("database.bin", "rb")
    database = load(file)
    file.close()
else:
    database = Core()


tk = ManagerView(database.show_stores, database.show_all_reseller, database.view_suggestion, database.create_store,
                 database.search_store, database.create_new_reseller, database.delete_sug
                 )

tk.mainloop()

file = open("database.bin", "wb")
dump(database, file)
file.close()
