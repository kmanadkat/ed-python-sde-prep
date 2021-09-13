class Student:
    def __init__(self, name='', phy=0, chem=0, bio=0):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        total = self.totalObtained()
        return total // 3


st1 = Student('Philip', 80, 90, 40)
print(st1.totalObtained())
print(st1.percentage())
