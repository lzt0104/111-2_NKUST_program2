#Composition


class Store:
    def __init__(self):
        self.signboard = Signboard()
        self.shelf = Shelf()
        self.cashier = Cashier()
        self.freezer = Freezer()

class Signboard:
    pass

class Shelf:
    pass

class Cashier:
    pass

class Freezer:
    pass