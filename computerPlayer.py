"""
Description: Class for computerPlayer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from player import player
class computerPlayer(player):
    def __init__(self, playerNum, score:int, is_turn:bool)->None:
        super().__init__(playerNum, score, is_turn)
        self.is_human = False