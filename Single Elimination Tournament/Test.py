import math
from  schemdraw import flow
import schemdraw



class Warrior:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.wins = 0

    def __str__(self):
        return f"Warrior {self.name} boasts {self.strength} strength"

# Getter strength
    @property
    def strength(self):
        return self._strength

# Getter name
    @property
    def name(self):
        return self._name

# Getter wins
    @property
    def wins(self):
        return self._wins

# Setter for name
    @name.setter
    def name(self, name):
        self._name = name

# Setter for strength
    @strength.setter
    def strength(self, strength):
        self._strength = strength

# Setter for wins
    @wins.setter
    def wins(self, n):
        self._wins = n

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
            return self.war2
        else:
            return None

    def get_loser(self):
        if self.get_winner==self.war1.name:
            return self.war2
        else:
            return self.war1

class Tournament:
    def __init__(self,list_war_names, list_war_stats):
        self.bouts = []
#        games=len(list_warr)-1
        combatants=list(map(Warrior, list_war_names, list_war_stats))
        p2=int(math.pow(2,math.ceil(math.log2(len(list_war_names)))))
        number_of_byes=p2 - len(list_war_names)
        combatants.extend([Warrior(None,0)] * number_of_byes)
        while len(combatants) > 1:
            mid_point=int(len(combatants)/2)
            first=combatants[0:mid_point]
            second=combatants[mid_point:]
            second.reverse()
            next = []
            for match_ups in zip(first, second):
                print(f"This bout is between {match_ups[0].name} and {match_ups[1].name}")
                if match_ups[0].name is None:
                    next.append(match_ups[1])
                    print(f"{match_ups[1]} proceeds to the next round...obviously")
                elif match_ups[1].name is None:
                    next.append(match_ups[0])
                    print(f"{match_ups[0]} proceeds to the next round...obviously")
                else:
                    fight=Match(match_ups[0],match_ups[1])
                    print(f"{fight.get_winner().name} proceeds to the next round due to his supperior strength")
                    next.append(fight.get_winner())
                    self.bouts.append(fight)
            combatants=next
        self.victor=combatants[0]
    
    def victor(self):
        return self.victor

    def get_bouts(self):
        return self.bouts

warrior_names=["Nike", "Klichke", "Milko", "Tuti", "Krisi", "Skrum"]
warrior_stats=[3, 4, 12, 23, 1, 4]

tourney1=Tournament(warrior_names,warrior_stats)




print(f"The victor of this tournament is the great and powerfull {tourney1.victor.name} with his {tourney1.victor.strength} strength! All hail {tourney1.victor.name}!")