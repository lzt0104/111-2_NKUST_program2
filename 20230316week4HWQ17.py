class Lab:
    def __init__(self,table,chair,beaker,scale):
        self.table = table
        self.chair = chair
        self.beaker = beaker
        self.scale = scale

    def addComputer(self,computer):
        self.computer = computer

class Table:
    pass

class Chair:
    pass

class Beaker:
    pass

class Scale:
    pass

table = Table()
chair = Chair()
beaker = Beaker()
scale = Scale()

lab = Lab(table, chair, beaker, scale)
computer = computer
lab.addComputer(computer)