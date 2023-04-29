from abc import abstractmethod,ABCMeta
class Car(metaclass=ABCMeta):
    def __init__(self,co):
        self.color = co
        self.oil = None
    def show(self):
        print(f'color={self.color}')
    @abstractmethod
    def setOil(self,oil):
        self.oil = oil
    @abstractmethod
    def getOil(self):
        return self.oil
class Truck(Car):
    def __init__(self, dr,ow,co,oil):
        self.door = dr
        self.owner = ow
        super().__init__(co)
        self.oil = oil

    def setOil(self, oil):
        self.oil = oil
    def getOil(self):
        return self.oil

    def show(self):
        print(f"door={self.door}")
        print(f"owner={self.owner}")
        print(f"color={self.color}")
        print(f"Oil={self.oil}")

myTruck = Truck(2, "Me", "blue", 95)
myTruck.show()
    