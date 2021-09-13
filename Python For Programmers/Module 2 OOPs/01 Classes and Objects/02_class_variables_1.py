class Player:
    # Class Variable
    teamName = 'India'

    def __init__(self, name) -> None:
        # Instance Variable
        self.name = name


p1 = Player("Rohit")
p2 = Player("Rahul")
print(p1.__dict__, p1.teamName)
print(p2.__dict__, p2.teamName)

# Modify Class Variable -> Reflects in all objects
Player.teamName = 'West'
print(p1.__dict__, p1.teamName)
print(p2.__dict__, p2.teamName)
