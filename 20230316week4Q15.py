class Computer:

    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.harddisk = Harddisk()
        self.dvdrom = DVDRom()

    def addMonitor(self,monitor):
        self.monitor = monitor
    
    def addMouse(self,keyboard,mouse):
        self.keyboard = keyboard
        self.mouse = mouse

class CPU:
    pass

class Monitor:
    pass

class Mouse:
    pass

class Keyboard:
    pass

class Harddisk:
    pass

class RAM:
    pass

class DVDRom:
    pass

pc = Computer()
keyboard = Keyboard()
mouse = Mouse()
monitor = Monitor()
pc.addMonitor(monitor)
pc.addMouse(keyboard, mouse)