class Trapezoid:
    def __init__(self,top,botton,height):
        self.top = top
        self.botton = botton
        self.height = height
        self.__no = 999
    def getTop(self):
        return self.top
    def getBotton(self):
        return self.bottom
    def getHeight(self):
        return self.height
    def setTop(self,top):
        if top <0:
            self.top = 0
            return print("請輸入大於0的數")
        else:
            self.top = top
    def setBotton(self,botton):
        if botton <0:
            self.botton = 0
            return print("請輸入大於0的數")
        else:
            self.botton = botton
    def setHeight(self,height):
        if height <0:
            self.height = 0
            return print("請輸入大於0的數")
        else:
            self.height = height
    def __str__(self):
        print(f"top:{self.top}")
        print(f"botton:{self.botton}")
        print(f"height:{self.height}")
    def getArea(self):
        self.area = (self.top+self.botton)*self.height/2
        return print(f"梯形面積為:{self.area}")
    def __lt__(self,other):
        return (self.top+self.botton)*self.height/2 < (other.top+other.botton)*other.height/2


c1 = Trapezoid(top=10,botton=10,height=10)
c1.getArea()
c1.setTop(top=6)
c1.getTop()
c1.setTop(top=-3)
c2 = Trapezoid(top=2,botton=4,height=6)
c2.getArea()
c1.area < c2.area
