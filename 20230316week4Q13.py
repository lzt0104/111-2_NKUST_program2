#Aggregation 聚合範例

class Car:
    def __init__(self):
        print("car init")

    def addEngine(self,engine):
        self.engine = engine

    def addTire1(self,tire):
        self.tire1 = tire
    
    def addTire2(self,tire):
        self.tire2 = tire

    def addTire3(self,tire):
        self.tire3 = tire

    def addTire4(self,tire):
        self.tire4 = tire

class Engine:
    def __init__(self,size):
        self.size = size

class Tire:
    def __init__(self,position):
        self.position = position

car1 = Car()
engine = Engine(2000)
car1.addEngine(engine)
tire1 = Tire(1)
tire2 = Tire(2)
tire3 = Tire(3)
tire4 = Tire(4)
car1.addTire1(tire1)
car1.addTire2(tire2)
car1.addTire3(tire3)
car1.addTire4(tire4)