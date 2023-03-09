class Circle:
    def __init__(self, r): #新的、初始化
        self.radius = r

    def __repr__(self): #設計當物件被查詢時要顯示什麼內容
        return f'Circle(radius={self.radius})'

    def __str__(self): #使用print()來列印變數，可以得到變數的值；使用__str__()來設定，print()列印的結果
        return print("This is a Circle.")

    def __eq__(self, other): #透過定義__eq__()來進行兩個物件的比較
        return self.radius == other.radius


circle = Circle(10)
circle2 = Circle(10)
print(circle)
if (circle==circle2):
    print(True)
else:
    print(False)


#practice1
class ground:
    def __init__(self,l):
        self.lon=l
    def __repr__(self):
        return f'long so long{self.long}'
    def __str__(self):
        return print("I have long")
    def __eq__(self, other):
        return self.lon == other.lon

lon = ground(10)
lon2 = ground(100)
print(lon)
if (lon==lon2):
    print(True)
else:
    print(False)
