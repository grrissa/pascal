"""
Description: Class for battleship object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class battleship(ship):
    def __init__(self, name:str = "battleship", length:int = 4,  horizontal:bool = True) -> None:
        self.length = length
        self.horizontal = horizontal
        self.name = name

    #is this class not inherited from ship class, this question goes for all ship subclasses (would be a good use of inheritence)
    def change_orientation(self):
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True