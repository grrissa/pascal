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
    def __init__(self, name:str = "battleship", length:int = 4,  horizontal:bool = True)->None:
        """
        Constructor for battleship object
        """
        super().__init__(length, horizontal)
        self.name = name