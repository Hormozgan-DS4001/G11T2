from data_structure import SArray, Dll, DArray


class Suggestion:
    def __init__(self, text, time):
        self.text = text
        self.time = time
        self.is_delete = False


class Manager:
    suggestion_manager = Dll

    def __init__(self):
        pass

    def add_reseller(self):
        pass

    def create_reseller(self):
        pass

    def delete_reseller(self):
        pass

    def create_store(self):
        pass

    def view_suggestion(self):
        pass


class Reseller:
    SUGGESTION_RESELLER = DArray

    def __init__(self):
        pass

    def add_suggestion(self):
        pass

    def view_suggestion(self):
        pass


class Store:
    STORE_CODE = 1

    def __init__(self):
        pass

    def add_reseller(self):
        pass

    def delete_reseller(self):
        pass


class Core:
    STORES = SArray(200)
    RESELLER = SArray(200)

    def __init__(self):
        pass

    def show_stores(self):
        pass

    def search_store(self):
        pass

    def add_suggestion(self):
        pass

    def login(self):
        pass









