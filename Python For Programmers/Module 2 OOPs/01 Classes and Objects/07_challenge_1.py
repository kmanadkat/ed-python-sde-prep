class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2


pt = Point(1, 3, 5)
print(pt.sqSum())
