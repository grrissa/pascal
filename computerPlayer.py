"""
Description: Class for computerPlayer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

import player
class computerPlayer(player):
    def __init__(self, score:int, is_turn:bool)->None:
        self.score = score
        self.is_turn = is_turn

    def make_hit(self)->None:
        #Need to implement
        return