class Car:
    def __init__(self,color):
        self.color = color

    def show(self):
        print(f'color={self.color}')


class Truck(Car):
    def __init__(self, dr,ow,co):
        self.door = dr
        self.owner = ow
        super().__init__(co)

    def show(self):
        print(f'door={self.door}, owner={self.owner},color={self.color}')

truck = Truck(2, "ow", "red")
truck.show()