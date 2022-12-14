"""
Description: Class for carrier object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class carrier(ship):
    def __init__(self, name:str = "carrier", length:int = 5,  horizontal:bool = True)->None:
        """
        Constructor for battleship object
        """
        super().__init__(length, horizontal)
        self.name = name
