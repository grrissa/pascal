"""
Description: Class for player object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from cell import cell
class player(object):
    def __init__(self, playerNum, score:int, is_turn:bool) -> None:
        self.playerNum = playerNum
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
        self.numOfHits = 0

    def incrementHits(self) -> None:
        self.numOfHits += 1

    def __str__(self) -> str:
    def __str__(self):
        return ("Player %d", self.playerNum)