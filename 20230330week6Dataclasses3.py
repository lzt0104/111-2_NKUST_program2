from abc import abstractclassmethod,ABCMeta
class Parent(metaclass=ABCMeta):
    @abstractclassmethod
    def method1(self):
        pass
    
    def method2(self):      
        pass
    
    def method3(self):
        pass

class Child(Parent):
    def method1(self):
        pass

c=Child()