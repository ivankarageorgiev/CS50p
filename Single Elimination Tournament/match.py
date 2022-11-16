from warrior import Warrior

class Match:
    def __init__(self,war1,war2):
        self.war1=war1
        self.war2=war2

    def __str__(self):
        return f"Warrior {self.war1.name} and {self.war2.name} will face off"

    def result(self):
        if self.war1.strength>self.war2.strength:
            self.war1.wins+=1
            return f"{self.war1.name} is victorious"
        elif self.war1.strength<self.war2.strength:
            self.war2.wins+=1
            return f"{self.war2.name} is victorious"
        else:
            return "Draw"

    def get_winner(self):
        if self.war1.strength>self.war2.strength:
            self.war1.wins+=1
            return self.war1
        elif self.war1.strength<self.war2.strength:
            self.war2.wins+=1
            return  self.war2
        else:
            return None

    def get_loser(self):
        if self.get_winner==self.war1:
            return self.war2
        else:
            return self.war1

war1=Warrior("Miko", 12)
war2=Warrior("Siko", 2)

match1=Match(war1,war2)
print(match1.get_winner().strength)




