"""
Description: Class for humanPlayer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from player import player
from cell import cell
class humanPlayer(player):
    def __init__(self, playerNum, score:int, is_turn:bool)->None:
        super().__init__(playerNum, score, is_turn)

        shipCells = []
        for r in range(10):
            row = []
            for c in range(10):
                row.append(cell(False, False, "NA"))
            shipCells.append(row)

        attackingCells = []
        for r in range(10):
            row = []
            for c in range(10):
                row.append(cell(False, False, "NA"))
            attackingCells.append(row)

        self.shipCells = shipCells
        self.attackingCells = attackingCells

    def make_hit(self)->None:
        #Need to implement
        return
    #AIDANS CODE START 
    def setHits(self, ship_types):
        self.hit = {}
        self.ship_size = {}
        for item in ship_types:
            print(item.name)
            self.ship_size[item.name] = item.length
            self.hit[item.name] = 0
    #AIDANS CODE FINISH