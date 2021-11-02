from data_structure import SArray, Dll, DArray
import datetime


class Suggestion:
    def __init__(self, text, time):
        self.text = text
        self.time = time
        self.is_delete = False


class Manager:

    def __init__(self, name, national_code, password):
        self.name = name
        self.national_code = national_code
        self.password = password
        self.suggestion_list = Dll()

    def view_suggestion(self):
        return self.suggestion_list.get_node_handler(len(self.suggestion_list) - 1)

    def add_suggestion_manager(self, suggestion: "Suggestion"):
        self.suggestion_list.append(suggestion)


class Reseller:

    def __init__(self, name: str, national_code: int, password: str = "123"):
        self.name = name
        self.national_code = national_code
        self.password = password
        self.suggestion_user = DArray()
        self.stores_list = Dll()

    def add_suggestion(self):
        pass

    def view_suggestion(self):
        pass

    def show_stores_user(self):
        pass


class Store:
    STORE_CODE = 1

    def __init__(self, address, rant):
        self.code = Store.STORE_CODE
        self.address = address
        self.rant = rant
        self.time = 0
        self.reseller = None

    def add_reseller(self, reseller: "Reseller"):
        self.reseller = reseller
        self.time = datetime.date.today().strftime("%b-%d-%Y")
        reseller.stores_list.append(self)

    def delete_reseller(self):
        self.reseller = None
        self.time = 0


class Core:

    def __init__(self):
        self.stores = SArray(200)
        self.resellers = SArray(200)
        self.number_reseller = -1

    def create_new_reseller(self):
        pass

    def delete_reseller(self):
        pass

    def show_stores(self):
        pass

    def search_store(self):
        pass

    def add_suggestion(self):
        pass

    def create_store(self):
        pass

    def login(self, national_code, password):
        # use binary search
        minimum = 0
        maximum = self.number_reseller
        while minimum <= maximum:
            mid = (maximum - minimum) + minimum // 2
            if national_code == self.resellers[mid].national_code and password == self.resellers[mid].password:
                return self.resellers[mid]

            elif national_code > self.resellers[mid].national_code:
                minimum = mid + 1

            else:
                maximum = mid - 1
