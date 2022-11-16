from warrior import Warrior
from match import Match
import math

class Tournament:
    def __init__(self,list_warr):
        self.bouts=[]
#        games=len(list_warr)-1
        combatants=list(map(Warrior, list_warr))
        p2=int(math.pow(2,math.ceil(math.log2(list_warr))))
        number_of_byes=p2-len(list_warr)
        combatants.extend([None] * number_of_byes)

        while combatants>1:
            mid_point=len(combatants)/2
            first=combatants[0:mid_point]
            second=combatants[mid_point:]
            second.reverse()
            next=[]
            for match_ups in zip(first, second):
                if match_ups[0] is None:
                    next.append(match_ups[1])
                elif match_ups[1] is None:
                    next.append(match_ups[0])
                else:
                    match=Match(match_ups)
                    next.append(match.winner)
                    self.bouts.append(match)
            combatants=next
        self.victor=combatants[0]
    
    def victor(self):
        return self.victor

    def get_bouts(self):
        return self.bouts