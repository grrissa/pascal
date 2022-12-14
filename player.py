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
    def __init__(self, playerNum, score:int, is_turn:bool)->None:
        """
        Constructor for player object
        """
        self.playerNum = playerNum
        self.score = score
        self.is_turn = is_turn

        shipCells = []
        for r in range(10):
            row = []
            for c in range(10):
                row.append(cell(False, False, "NA", False))
            shipCells.append(row)

        attackingCells = []
        for r in range(10):
            row = []
            for c in range(10):
                row.append(cell(False, False, "NA", False))
            attackingCells.append(row)

        self.shipCells = shipCells
        self.attackingCells = attackingCells
        self.numOfHits = 0
        self.playerShips = {}

    def incrementHits(self)->None:
        """
        Increment the number of hits that a player has made
        """
        self.numOfHits += 1

    def __str__(self)->str:
        """
        String representation of the player object
        """
        return ("Player %d", self.playerNum)