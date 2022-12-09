"""
Description: Class for cell object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""
class cell(object):
    """
    @Class Cell
    @constructor(hit:bool, ship:bool, id:str)
    @return: None
    @purpose: 
    1/ create cell class 
    """
    def __init__(self, h:bool, s:bool, i:str, sh:bool)->None:
        self.hit = h
        self.ship = s
        self.id = i
        self.successful_hit = sh

    def __repr__(self):
        return str(self.hit) + " "+str(self.ship) + " "+self.id + " "+self.successful_hit

