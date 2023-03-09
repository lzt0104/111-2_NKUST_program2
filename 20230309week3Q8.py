class West:
    def __init__(self,height,name,weapon):
        self.h = height
        self.n = name
        self.w = weapon
    
    def printName(self):
        print(self.n)

    def printWeapon(self):
        print(self.w)

    def __str__(self):
        return f'Name={self.n},Weapon={self.w}'

    def __eq__(self, other):
        if self.n == other.n:
            return True
        else:
            return False

n1 = West(187, "Master", 87)
n2 = West(223, "Monkey", 23)
n3 = West(564, "Pig", 43)
n4 = West(665, "Sandy", 32)
print(n1)
print(n2)
print(n3)
print(n4)
if n1==n2:
    print("True")
else:
    print("False")