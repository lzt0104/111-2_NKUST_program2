class NoteBook:
    def __init__(self):
        self.__CPU = CPU()
        self.__monitor = Monitor()
        self.__keyboard = Keyboard()
        self.__SSD = SSD()
        self.__reader = Reader()
        
    def addMouse(self,mouse):
        self.mouse = mouse

    def addUsbhub(self,usbhub):
        self.usbhub = usbhub

    def addPrinter(self,printer):
        self.printer = printer

class CPU:
    pass
class Monitor:
    pass
class Keyboard:
    pass
class SSD:
    pass
class Reader:
    pass
n1 = NoteBook()
n1.addMouse(mouse)
n1.addPrinter(printer)
n1.addUsbhub(usbhub)