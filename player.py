"""
Description: Class for player object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

class player(object):
    def __init__(self, playerNum, score:int, is_turn:bool)->None:
        self.playerNum = playerNum
        self.score = score
        self.is_turn = is_turn
        self.is_human = True

    def make_hit(self)->None:
        #Need to implement
        return

    def __str__(self):
        return ("Player %d", self.playerNum)