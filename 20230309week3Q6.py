import math
class Sphere:
    def __init__(self,r):
        self.rad=r
    def volume(self):
        return math.pow(self.rad, 3)*4/3*math.pi
    def surfacr_arrea(self):
        return math.pow(self.rad, 2)*4*math.pi
    def __repr__(self):
        return f'Sphere object,rad ={self.rad}'
    def __str__(self):
        return "Sphere object,rad={self.rad},valume={s0.volume()},surface_area={s0.surfacr_arrea()}"
s0 = Sphere(2)
print("volume:",s0.volume())
print("surface:",s0.surfacr_arrea())
print(s0)