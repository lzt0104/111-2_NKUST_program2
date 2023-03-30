class Animal:
    def sound(self):
        pass
    def food(self):
        pass

class Cat(Animal):
    def sound(self):
        print("cat sound")
    def food(self):
        print("cat food")

class Dog(Animal):
    def sound(self):
        print("dog sound")
    def food(self):
        print("dog food")

dog = Dog()
dog.food()
