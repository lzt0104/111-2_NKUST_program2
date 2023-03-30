from dataclasses import dataclass,field

@dataclass
class Account:
    amount: int


    def withdraw(self,number):
        if number > self.amount:
            self.amount = self.amount- number
        else:
            print("存款不足")

    def deposit(self,number):
        self.amount = self.amount + number

    def getAccount(self):
        return self.amount

account = Account(1000)
account.deposit(1000)
account.withdraw(200)       