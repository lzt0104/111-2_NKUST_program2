#繼承
class Grand:
    def Gooo(self):
        print("GG")

class Father(Grand):
    def F2(self):
        print("F2")

class Child(Father):
    def F1(self):
        print("f1")


c = Child()
c.F2()
c.F1()
c.Gooo()

#多重繼承
class GrandMa:
    def F4(self):
        print("F4")

class AAA:
    def A(self):
        print("AAA")

class BBB(GrandMa,AAA):
    def B(self):
        print("BBB")


A =BBB()
A.A()

#複寫
class GrandMa:
    def F4(self):
        print("F4")

class AAA:
    def A(self):
        print("AAA")

class BBB(GrandMa,AAA):
    def B(self):
        print("BBB")
    def A(self):
        print("LLL")
        super().A()

c = BBB()
c.A()

