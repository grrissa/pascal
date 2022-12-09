"""
Description: Class for computerPlayer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

import time
from player import player
import random

class computerPlayer(player):
    def __init__(self, playerNum, score:int, is_turn:bool) -> None:
        super().__init__(playerNum, score, is_turn)
        self.is_human = False
        self.max_ship_length_left = 5

        self.last_missile_success = False
        self.direction = 0
        self.curr_direction = 0
        self.original_success = (-1,-1)
        self.last_hit = (-1, -1)
        self.flip_attack = False


    def random_ints(self):
        return random.randint(0,9), random.randint(0,9)

    def computer_hit(self, other_player_ships, other_player_sunk_data):
        next_x = -1
        next_y = -1
        # if we should make a random computer hit or a smart computer hit
        if self.last_missile_success == True:
            # After first hit, checking neighboring cells to see which direction we should go
            if self.curr_direction == 0:
                valid = False
                #Random int 1-4 to choose where we go next (1 = North, 2 = East, 3 = West, 4 = South)
                while valid == False:
                    self.direction = random.randint(1,4)
                    if self.direction == 1:
                        next_x = self.original_success[0]
                        next_y = self.original_success[1]-1
                    elif self.direction == 2:
                        next_x = self.original_success[0]+1
                        next_y = self.original_success[1]
                    elif self.direction == 3:
                        next_x = self.original_success[0]
                        next_y = self.original_success[1]+1
                    else:
                        next_x = self.original_success[0] - 1
                        next_y = self.original_success[1]
                    if not(self.attackingCells[next_x][next_y].hit == True or next_x < 0 or next_x > 9 or next_y < 0 or next_y > 9):
                        valid = True
                if other_player_ships[next_x][next_y].ship == True:
                    self.curr_direction = self.direction
                    print("Curr direction " + str(self.curr_direction))
            else:
                valid = False
                center_x = self.last_hit[0]
                center_y = self.last_hit[1]
                print("DB")
                while valid == False:
                    if self.curr_direction == 1:
                        center_y -= 1
                    elif self.curr_direction == 2:
                        center_x += 1             
                    elif self.curr_direction == 3:
                        center_y += 1
                    else:
                        center_x -= 1       
                    next_x = center_x
                    next_y = center_y
                    print(str(next_x) + " " + str(next_y))
                    if ((self.attackingCells[next_x][next_y].hit != True and next_x >= 0 and next_x <= 9 and next_y >= 0 and next_y <=9) and (self.flip_attack == False)):
                        valid = True
                    else:
                        center_x = self.original_success[0]
                        center_y = self.original_success[1]
                        if self.curr_direction ==  1:
                            self.curr_direction = 3
                        elif self.curr_direction == 2:
                            self.curr_direction = 4
                        elif self.curr_direction == 3:
                            self.curr_direction = 1
                        else:
                            self.curr_direction = 2
                        self.flip_attack = False
                if other_player_ships[next_x][next_y].ship == False:
                    self.flip_attack = True
            if other_player_ships[next_x][next_y].ship == True:
                temp = other_player_sunk_data.get(other_player_ships[next_x][next_y].id)
                temp.timeHit += 1
                if temp.isSunk() == True:
                    self.last_missile_success = False
                    self.curr_direction = 0
                    self.direction = 0
                    self.original_success = (-1,-1)
                    self.last_hit = (-1, -1)
                self.attackingCells[next_x][next_y].successful_hit = True
                print("comp hit!")
        else:
            next_x, next_y = self.random_ints()
            # checking whether there was already a hit to that location
            while self.attackingCells[next_x][next_y].hit == True:
                print("searching")
                next_x, next_y = self.random_ints()
        # updating the board for the ships
            if other_player_ships[next_x][next_y].ship == True:
                self.last_missile_success = True
                self.original_success = (next_x, next_y)
                temp = other_player_sunk_data.get(other_player_ships[next_x][next_y].id)
                temp.timeHit += 1
                self.attackingCells[next_x][next_y].successful_hit = True
                print("comp hit!")
        #Changing the hit bool in the selected cell in both players boards
        other_player_ships[next_x][next_y].hit = True
        self.attackingCells[next_x][next_y].hit = True 
        
        self.last_hit = (next_x, next_y)

            

    

