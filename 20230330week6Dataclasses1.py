from dataclasses import dataclass,field

@dataclass
class Cube:
    long2: int
    width: int
    height: int
    volume: int = field(init=False) #表示不初始化


    def __post_init__(self):
        self.volume = self.long2*self.width*self.height
    
    def getVolume(self):
        return self.volume

cube = Cube(long2=8, width=10, height=3)
print(cube.getVolume())
