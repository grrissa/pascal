"""
Description: Class for computerPlayer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from player import player
from cell import cell
class computerPlayer(player):
    def __init__(self, playerNum, score:int, is_turn:bool)->None:
        super().__init__(playerNum, score, is_turn)
        self.is_human = False

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
        self.numOfHits = 0

    def incrementHits(self):
        self.numOfHits += 1

    def make_hit(self)->None:
        #Need to implement
        return