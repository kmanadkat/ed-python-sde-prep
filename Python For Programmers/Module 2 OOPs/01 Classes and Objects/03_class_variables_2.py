class Player:
    # Class Variable
    teamName = 'India'
    teamPlayers = []

    def __init__(self, name) -> None:
        # Instance Variable
        self.name = name
        self.teamPlayers.append(self.name)


p1 = Player("Rohit")
p2 = Player("Rahul")
print(p1.__dict__, p1.teamName, p1.teamPlayers)
print(p2.__dict__, p2.teamName, p2.teamPlayers)
