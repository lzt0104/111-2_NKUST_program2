class Account:
    def __init__(self,init):
        self.__money=init

    def deposit(self,number):
        self.__money+=number
        self.balance()
    
    def withdraw(self,number):
        self.__money-=number
        self.balance()

    def balance(self):
        print("money=",self.__money)
    
    def addInteresst(self,number):
        self.__money+=number
        self.balance()

cash = Account(500)
cash.balance()
cash.deposit(60)
cash.withdraw(40)
