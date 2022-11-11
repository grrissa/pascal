"""
Description: Class for battleship object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

import ship
class battleship(ship):
    def __init__(self, length:int) -> None:
        self.length = 4