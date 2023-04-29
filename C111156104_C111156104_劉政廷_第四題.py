class Base:
    def __init__(self):
        pass

    def __foo(self):
        pass

class AnotherBase:
    def __init__(self):
        pass

    def foo2(self):
        pass

class Derived(Base, AnotherBase):
    def __init__(self):
        Base.__init__(self)
        AnotherBase.__init__(self)

    def foo2(self):
        pass

d = Derived()
d.foo2()
