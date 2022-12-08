"""
Description: Class for ship object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

class ship(object):
    def __init__(self, length:int, horitontal:bool) -> None:
        self.length = length
        self.horizontal = True
        self.numHits = 0

    def change_orientation(self):
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True

    def set_orientation(self, orientation):
        self.horizontal = orientation
    
    def isSunk(self)->bool:
        if self.length == self.numHits:
            return True
        return False

    def __str__(self)->str:
        return self.name + "Testing"