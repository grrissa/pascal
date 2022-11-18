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

    def change_orientation(self):
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True