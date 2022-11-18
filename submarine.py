"""
Description: Class for submarine object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class submarine(ship):
    def __init__(self, name:str = "submarine", length:int = 3,  horizontal:bool = True) -> None:
        self.length = length
        self.horizontal = horizontal
        self.name = name

    def change_orientation(self):
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True