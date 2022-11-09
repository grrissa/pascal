"""
Names: Alizea Hinz, Marissa Esteban, Gabe Krishnadasan, Aidan Rooney
Proj: Final Project- Battleship 
Class: COMP-305 SP22
Prof: A. Nuzen
Purpose: Cell Class
"""
class Cell(object):
    """
    @Class Cell
    @constructor(hit:bool, ship:bool, id:str)
    @return: None
    @purpose: 
    1/ create cell class 
    """
    def __init__(self, h:bool, s:bool, i:str)-->None:
        self.hit = h
        self.ship = s
        self.id = i

