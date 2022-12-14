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
        """
        Constructor for ship object
        """
        self.length = length
        self.horizontal = True
        self.timeHit = 0

    def change_orientation(self)->None:
        """
        Funtion to change the orientation of a ship object
        """
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True

    def isSunk(self)->bool:
        """
        Function to check if the ship is sunk
        """
        if self.timeHit == self.length:
            return True
        return False