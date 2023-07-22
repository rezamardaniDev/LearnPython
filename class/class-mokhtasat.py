from math import sqrt
class Mokhtasat:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


    def tool(point1, point2 ):
        print(((point2.y - point1.y) ** 2 + (point2.x - point1.x) ** 2) ** 0.5)

    def shib(point1, point2):
        print((point2.y - point1.y) / (point2.x - point1.x))

p1 = Mokhtasat(1, 1)
p2 = Mokhtasat(3, 3)

Mokhtasat.tool(p1, p2)
Mokhtasat.shib(p1, p2)

