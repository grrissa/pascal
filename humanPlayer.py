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
    def __init__(self, score:int, is_turn:bool)->None:
        self.score = score
        self.is_turn = is_turn

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