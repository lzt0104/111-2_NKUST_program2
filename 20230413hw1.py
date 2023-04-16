class Window:
    def __init__(self , w=10,h=5): 
        self.width = w
        self.heigh= h
    
    def getArea(self):
        return self.width * self.heigh

    def __eq__(self, other):
        if self.width*self.heigh == other.width*other.heigh:
            return True
        else:
            return False

    
w0 = Window(w=12,h=8)
w0.getArea()
w1 =Window(w=12,h=8)
w1.getArea()
if w0==w1:
    print("True")
else:
    print("False")



