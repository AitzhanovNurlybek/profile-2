class Player():
    def __init__(self,name,sport):
        self.name = name
        self.sport = sport

class Striker(Player):
    def __init__(self,name):
        super().__init__(name,"basketball")

striker1 = Striker("James Striker")
print(striker1.__dict__)
