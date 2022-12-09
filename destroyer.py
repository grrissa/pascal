"""
Description: Class for destroyer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class destroyer(ship):
    def __init__(self, name:str = "destroyer", length:int = 2, horizontal:bool = True) -> None:
        """Constructor for variables for name length and orientation of destroyer"""
        super().__init__(length, horizontal)
        self.name = name

