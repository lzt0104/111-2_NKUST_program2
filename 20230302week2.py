class 關鍵字:
    變數attribute or 函數method
    """需要使用self.屬性 or self.方法"""

#類別
class Circle:
    PI = 3.14
    r = 1

    def getArea(self): #()一定要寫self
        return self.PI * self.r**2

    def getRValue(self):
        return self.r

    def getArea2(self):
        self.getArea()   #呼叫別的method

"""
類別注意事項
1.需要以Class為基準
2.縮排必須對齊(4個空白)
3.類別定義的方法 = 與函數差不多 差別在於方法內一定要寫self
4.呼叫方法，參數不用傳遞self
5.class 開頭以大寫來撰寫
6.屬性的開頭以名詞開頭 例如: radius、userName
7.方法的開頭以動詞開 ，例如: showName、getArea
"""
#物件
#C1 = circle()
#C2 = C1 #指向同一個物件

C1 = Circle()
print("半徑為",C1.r,"的圓面積為", C1.getArea())

C2 = C1
C2.r = 10
print("半徑為",C1.r,"的圓面積為", C1.getArea())

C1 = Circle()
print(C1.getRValue())

#__init__()方法
class Circle2:
    PI = 3.14

    def __init__(self,r=1): #初始化
        self.r = r

    def getArea(self):
        return self.PI * self.r**2
C1 = Circle2()
print("半徑為",C1.r,"的圓面積為", C1.getArea())

#匿名物件
class Circle3:
    PI = 3.14

    def __init__(self,r=1):
        self.r = r
    
    def getArea(self):
        return self.PI * self.r**2

print("半徑為", Circle3().r, "的圓面積為", Circle3().getArea())
print("半徑為", Circle3(10).r, "的圓面積為", Circle3(10).getArea())

"""
私有屬性(private attribute)的名稱前面要加上兩個底線_
1.兩個底線_開頭的屬性為私有屬性(private attribute)
2.兩個底線_開頭的方法為私有方法(private method)
"""

"""
1.
(1) 建立一個Windows類別的物件w0，其屬性width與height為預設值。
(2)修改Windows類別的物件w0，使其屬性width與height為12和8。
(3)建立一個Windows類別的物件w1，其屬性其屬性width與height為16和7。
(4)新增一個方法，計算w0和w1的面積。然後印出較大的面積。
"""
#1.1
class Window:
    def __init__(self,w=10,h=5):
        self.width = w
        self.height = h
        

w0 = Window()
print("width:",w0.width , "height:",w0.height)

#1.2
w0.height = 8
w0.width = 12
print("width:",w0.width , "height:",w0.height)

#1.3
w1 =Window(16,7)
print("width:",w1.width , "height:",w1.height)

#1.4
class Window:
    def __init__(self,w=10,h=5):
        self.width = w
        self.height = h

    def getArea(self):
        return self.height * self.width
    

w0 = Window()
print("w0",w0.getArea())

w1 =Window(16,7)
print("w1",w1.getArea())

if w0.getArea() > w1.getArea():
    print("w0 is larger")
else:
    print("w1 is larger")

"""
2.
有一class Pen
(1) 請查詢Pen.price，值為多少?
(2) 建立一個p1物件，查詢p1.price 值為多少?
"""

#2.1
class Pen:
    price = 30

print(Pen.price)

#2.2
p1 = Pen()
print(p1.price)


"""
3.
1.撰寫一個類別Student，包含屬性name, grade
2設計一個__init__(na,gr)函數，可將name和grade 分別設為na和gr
3.設計一個函數getGPA，可以依照grade 輸出GPA
4.建立一個name為Tom，grade 為89，之Student 類別的物件
"""
class Student:
    def __init__(self, na,gr):
        self.name = na
        self.grade = gr

    def getGPA(self):
        if self.grade >=80:
            return 4
        elif self.grade >= 70:
            return 3
        elif self.grade >= 60:
            return 2
        else:
            return 0

stu = Student("Tom", 89)
print(stu.getGPA())

"""
4.
設計一個Calculator類別，內含__init__(a,b)函數，可以n1與n2屬性分別設為a與b，然後以物件c0=Calculator(4,10)來進行測試，分別為
(1)設計add()函數，回傳n1與n2之和。
(2)設計gcd()函數，回傳n1與n2之最大公因數。
(3)設計lcm()函數，回傳n1與n2之最小公倍數。
(4)設計power()函數，回傳n1與n2次方，即n1n2。
註:2,3可以使用importmath，使用math.gcd()和math.lcm()
"""
import math
class Calculator:
    def __init__(self, a,b):
        self.n1 = a
        self.n2 = b
    
    def getAdd(self):
        return self.n1+self.n2

    def getGcd(self):
        return math.gcd(self.n1, self.n2)
    
    def getLcm(self):
        return math.lcm(self.n1) , math.lcm(self.n2)

    def getPower(self):
        return self.n1**self.n2

c0=Calculator(4,10)
#print(c0.n1,c0.n2)
print(c0.getAdd())
print(c0.getGcd())
print(c0.getLcm())
print(c0.getPower())

"""
5.
建立一個類別Pet，可以儲存屬性:寵物名、年紀、毛顏色
(1)讓使用者建立3隻動物，並輸入寵物名、年紀、毛顏色。輸入完後，印出結果。 提示:可存入陣列[]
(2) 使用者輸入完後找出年紀最大與最小，並印出如下範例:
寵物名1，是年紀最大者年紀1 歲
寵物名2，是最年輕為年紀2 歲
"""
class Pet:


    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def getStr(self):
        return f"{self.name}，{self.age}歲，毛色為{self.color}"

pets = []
for i in range(3):
    name = input("請輸入寵物名稱：")
    age = int(input("請輸入寵物年紀："))
    color = input("請輸入寵物毛色：")
    pet = Pet(name, age, color)
    pets.append(pet)


#hw
old_pet = max(pets, key=lambda p: p.age)
young_pet = min(pets, key=lambda p: p.age)
print(f"{old_pet.name}，是年紀最大者，{oldest_pet.age}歲")
print(f"{young_pet.name}，是最年輕者，{youngest_pet.age}歲")