from dataclasses import dataclass,field

@dataclass
class Tixing:
    top:int
    bottom:int
    height:int
    amount:float= field(init=False)

    def __post_init__(self):
        self.amount = (self.top+self.bottom)*self.height/2

    def getArea(self):
        return self.amount

W0 = Tixing(top=4,bottom=6,height=10)
print(W0.getArea())