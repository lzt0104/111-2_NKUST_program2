class NoteBook:
    def __init__(self):
        self.CPU = CPU()
        self.screen = Screen()
        self.kb = Kb()
        self.disk = Disk()

    def addMouse(self,mouse):
        self.mouse = mouse

class CPU:
    pass

class Screen:
    pass

class Kb:
    pass

class Disk:
    pass

cpu = CPU()
screen = screen()
kb = Kb()
disk = Disk()

nb = NoteBook(cpu,screen,kb,disk)
mouse = Mouse()

nb.addMouse(mouse)