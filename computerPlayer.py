"""
Description: Class for computerPlayer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from player import player
import random

class computerPlayer(player):
    def __init__(self, playerNum, score:int, is_turn:bool) -> None:
        super().__init__(playerNum, score, is_turn)
        self.is_human = False
        self.max_ship_length_left = 5

    def random_ints(self):
        return random.randint(0,9), random.randint(0,9)

    def computer_hit(self, other_player_ships):
        rand_x, rand_y = self.random_ints()
       
       # checking whether there was already a hit to that location
        while self.attackingCells[rand_x][rand_y].hit == True:
            print("searching")
            rand_x, rand_y = self.random_ints()
        
        if other_player_ships[rand_x][rand_y].ship == True:
            self.incrementHits()
            self.attackingCells[rand_x][rand_y].successful_hit = True
            print("comp hit!")

        #Changing the hit bool in the selected cell in both players boards
        other_player_ships[rand_x][rand_y].hit = True
        self.attackingCells[rand_x][rand_y].hit = True 

    

