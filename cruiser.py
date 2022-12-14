"""
Description: Class for cruiser object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class cruiser(ship):

    def __init__(self, name:str = "cruiser", length:int = 3, horizontal:bool = True) -> None:
        """Constructor for variables for name length and orientation of cruiser"""
        super().__init__(length, horizontal)
        self.name = name


