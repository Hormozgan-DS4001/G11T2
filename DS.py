from data_structure import SArray, Dll, DArray
import datetime


class Suggestion:
    def __init__(self, text, time):
        self.text = text
        self.time = time
        self.is_delete = False


class Reseller:

    def __init__(self, name: str, national_code: int, password: str = "123"):
        self.name = name
        self.national_code = national_code
        self.password = password
        self.suggestion_user = DArray()
        self.stores_list = Dll()

    def add_suggestion(self, suggestion: "Suggestion"):
        self.suggestion_user.append(suggestion)

    def view_suggestion(self):
        return self.suggestion_user.get_node_handler(len(self.suggestion_user) - 1)

    def show_stores_user(self):
        return self.stores_list.get_node_handler(0)


class Store:
    STORE_CODE = 1

    def __init__(self, address):
        self.code = Store.STORE_CODE
        self.address = address
        self.rant = 0.0
        self.time = 0
        self.reseller = None
        Store.STORE_CODE += 1

    def add_reseller(self, reseller: "Reseller", rant: float):
        self.reseller = reseller
        self.rant = rant
        self.time = datetime.date.today().strftime("%b-%d-%Y")
        reseller.stores_list.append(self)

    def delete_reseller(self):
        self.reseller = None
        self.time = 0
        self.rant = 0.0


class Core:

    def __init__(self):
        self.suggestion_list = Dll()
        self.stores = SArray(200)
        self.resellers = DArray(200)

    def create_new_reseller(self, name, national_code, password):
        new_reseller = Reseller(name, national_code, password)
        self.resellers.append(new_reseller)
        return new_reseller

    def show_stores(self):
        return self.stores.get_node_handler(0)

    def show_all_reseller(self):
        return self.resellers.get_node_handler(0)

    def search_store(self, store_code: int):
        return self.stores[store_code - 1]

    def create_store(self, address):
        store = Store(address)
        self.stores[store.code - 1] = store
        return store

    def view_suggestion(self):
        return self.suggestion_list.get_node_handler(len(self.suggestion_list) - 1)

    def add_suggestion(self, reseller: "Reseller", text: str):
        time = datetime.date.today().strftime("%b-%d-%Y")
        suggestion = Suggestion(text, time)
        self.suggestion_list.append(suggestion)
        reseller.add_suggestion(suggestion)

    def login(self, national_code, password):
        # use binary search
        minimum = 0
        maximum = len(self.resellers) - 1
        while minimum <= maximum:
            mid = (maximum - minimum) + minimum // 2
            if national_code == self.resellers[mid].national_code and password == self.resellers[mid].password:
                return self.resellers[mid]

            elif national_code > self.resellers[mid].national_code:
                minimum = mid + 1

            else:
                maximum = mid - 1
