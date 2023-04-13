from typing import final

class Base:
    @final(f)
    def foo(self):
        pass


class Derived(Base):
    def foo(self):
        pass