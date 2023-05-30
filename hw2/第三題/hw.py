import math
class boy:
    def __init__(self) -> None:
        pass
    def Count(n,m):
        value = math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
        return value