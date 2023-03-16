#Aggregation

class Store:

    def __init__(self):
        print("init store")

    def addDevices(self,signboard,shelf,cashier,freezer):
        self.signboard = signboard
        self.shelf = shelf
        self.cashier = cashier
        self.freezer = freezer



class Signboard:
    pass

class Shelf:
    pass

class Cashier:
    pass

class Freezer:
    pass

store = Store()
signboard = Signboard()
shelf = Shelf()
cashier = Cashier()
freezer = Freezer()
store.addDevices(signboard, shelf, cashier, freezer)