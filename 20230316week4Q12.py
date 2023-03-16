#Composition 組合範例

class Car:
    def __init__(self,size):
        self.engine = Engine(size)
        self.tire1 = Tire(1)
        self.tire2 = Tire(2)
        self.tire3 = Tire(3)
        self.tire4 = Tire(4)

class Engine:
    def __init__(self,size):
        self.size = size

class Tire:
    def __init__(self,position):
        self.position = position

car1 = Car(2000)