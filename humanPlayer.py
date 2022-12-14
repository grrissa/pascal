"""
Description: Class for humanPlayer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from player import player
class humanPlayer(player):
    def __init__(self, playerNum, score:int, is_turn:bool)->None:
        """
        Constructor for humanPlayer object
        """
        super().__init__(playerNum, score, is_turn)
        self.is_human = True

    
