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
    def __init__(self, name:str = "carrier", length:int = 5,  horizontal:bool = True) -> None:
        self.length = length
        self.horizontal = horizontal
        self.name = name

    def change_orientation(self):
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True