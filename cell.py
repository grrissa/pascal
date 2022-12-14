"""
Description: Class for cell object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""
class cell(object):
    def __init__(self, h:bool, s:bool, i:str, sh:bool)->None:
        """
        Constructor for cell object
        """
        self.hit = h
        self.ship = s
        self.id = i
        self.successful_hit = sh

    def __repr__(self)->str:
        """
        String representation of a cell object
        """
        return str(self.hit) + " "+str(self.ship) + " "+self.id + " "+self.successful_hit

