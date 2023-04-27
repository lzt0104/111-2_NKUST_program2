from dataclasses import dataclass

@dataclass
class Account:
    money:int
    owner:str

    def __post_init__(self):
        self.money = self.money
    def income(self,dollars):
        self.money =  self.money+dollars
    def outcome(self,dollars):
        if (self.money-dollars)<0:
            return f"餘額不足"
        elif self.money ==0 :
            return f"餘額不足"
        else:
            self.money = self.money- dollars

    def getMoney(self):
        return f"存款為{self.money}"
    def getOwner(self):
        return f"持有人為{self.owner}"

a1 = Account(money=9999,owner="LZT") 
a1.income(666)
a1.getMoney()
a1.outcome(10665)
a1.getOwner()
