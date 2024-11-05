class Player:
    def __init__(self, position, name):
        self.position = position
        self.name = name

joeMontana = Player("Quarter Back", "Joe Montana")
barrySanders = Player("Running Back", "Barry Sanders")
jerryRice = Player("Wide Receiver", "Jerry Rice")
grahamGano = Player("Kicker", "Graham Gano")

teamPlayers = [joeMontana.name, joeMontana.position, jerryRice.name, jerryRice.position, barrySanders.name, barrySanders.position, grahamGano.name, grahamGano.position]

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
myTeam = Team("Python Warriors", teamPlayers)

print(myTeam.name)
print(myTeam.players)
