class Pizza:
    def __init__(self,size,cheese,pepperoni,ham):
        self.__size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.ham = ham
    
    def setSize(self,size):
        if size == "small" or size=="medium" or size =="large" :
            self.__size = size
        else:
            print("Wrong size")

    def getSize(self):
        return self.__size

    def calcCost(self):

        num_of_toppings = self.cheese+self.ham+self.pepperoni
        cost_of_toppings = 2*self.num_of_toppings

        if self.__size == "small":
            return 10 + self.cost_of_toppings
        elif self.__size == "medium":
            return 12 + self.cost_of_toppings
        elif self.__size == "large":
            return 14 + self.cost_of_toppings

    def getDescription(self):
        
        description = "size：{0},Cheese：{1},Pepperoni：{2},Ham：{3}".format(self.__size,self.cheese,self.pepperoni,self.ham)

        return description



pizza = Pizza("large", 10, 2, 3)

pizza.setSize("large")

print(pizza.getDescription())
