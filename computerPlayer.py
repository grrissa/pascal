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
    def __init__(self, playerNum:int, score:int, is_turn:bool)->None:
        """
        Constructor for computerPlayer object
        """
        super().__init__(playerNum, score, is_turn)
        self.is_human = False
        self.max_ship_length_left = 5
        self.last_missile_success = False
        self.direction = 0
        self.curr_direction = 0
        self.original_success = (-1,-1)
        self.last_hit = (-1, -1)
        self.flip_attack = False

    def random_ints(self)->tuple:
        """
        Function generates random cell coordinates and returns them as a tuple of ints
        """
        return random.randint(0,9), random.randint(0,9)

    def computer_hit(self, other_player_ships, other_player_sunk_data)->None:
        """
        Will make either a computer generated smart hit or a random hit depending on the 
        outcome of the previous hit
        """
        next_x = -1
        next_y = -1
        # if we should make a random computer hit or a smart computer hit
        if self.last_missile_success == True:

            # After first hit, checking neighboring cells to see which direction we should go
            if self.curr_direction == 0:
                valid = False
                count = 0

                #Random int 1-4 to choose where we go next (1 = North, 2 = East, 3 = West, 4 = South)
                while valid == False:
                    count += 1
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

                    # checking on whether these points are valid
                    if not( self.out_of_bounds(next_x, next_y) or self.attackingCells[next_x][next_y].hit == True):
                        valid = True
                    elif count > 4:
                        valid = True
                        next_x, next_y = self.random_hit(other_player_ships, other_player_sunk_data)
                if other_player_ships[next_x][next_y].ship == True:
                    self.curr_direction = self.direction

            else:
                valid = False
                center_x = self.last_hit[0]
                center_y = self.last_hit[1]
                count = 0

                # will attempt a hit in a neighboring cell
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
                    count +=1

                    # checking if this hit is valid or whether to flip sides
                    if ((not self.out_of_bounds(next_x, next_y) and self.attackingCells[next_x][next_y].hit != True) and (self.flip_attack == False)):
                        valid = True
                    elif count >4:
                        valid = True
                        next_x, next_y = self.random_hit(other_player_ships, other_player_sunk_data)
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

            # reset direction variables
            if other_player_ships[next_x][next_y].ship == True:
                temp = other_player_sunk_data.get(other_player_ships[next_x][next_y].id)
                temp.timeHit += 1
                self.numOfHits +=1
                if temp.isSunk() == True:
                    self.last_missile_success = False
                    self.curr_direction = 0
                    self.direction = 0
                    self.original_success = (-1,-1)
                    self.last_hit = (-1, -1)
                self.attackingCells[next_x][next_y].successful_hit = True

        else:
            next_x, next_y = self.random_hit(other_player_ships, other_player_sunk_data)

        #Changing the hit bool in the selected cell in both players boards
        other_player_ships[next_x][next_y].hit = True
        self.attackingCells[next_x][next_y].hit = True 
        
        self.last_hit = (next_x, next_y)

    def random_hit(self, other_player_ships, other_player_sunk_data)->tuple:
        """
        Generates a completely random set of coordinates
        """
        next_x, next_y = self.random_ints()

        # checking whether there was already a hit to that location
        while self.attackingCells[next_x][next_y].hit == True or False not in self.check_neighbors(next_x, next_y):
            print("searching")
            next_x, next_y = self.random_ints()

        # updating the board for the ships
        if other_player_ships[next_x][next_y].ship == True:
            self.last_missile_success = True
            self.original_success = (next_x, next_y)
            temp = other_player_sunk_data.get(other_player_ships[next_x][next_y].id)
            temp.timeHit += 1
            self.attackingCells[next_x][next_y].successful_hit = True
            self.numOfHits += 1
        return next_x, next_y

    def out_of_bounds(self, x, y)->bool:
        """ 
        Checks if coordinate pairs are out of bounds 
        """
        if x < 0 or x > 9 or y < 0 or y > 9:
            return True
        else:
            return False

    def check_neighbors(self, x, y)->list:
        """
        Returns information about contents of neighboring cells
        """
        if(x+1 >= 10):
            to_right = True
        else:
            to_right = self.attackingCells[x+1][y].hit == True and self.attackingCells[x+1][y].successful_hit == False
        if(x-1 < 0):
            to_left = True
        else:
            to_left = self.attackingCells[x-1][y].hit == True and self.attackingCells[x-1][y].successful_hit == False
        if(y-1 <0):
            to_top = True
        else:
            to_top = self.attackingCells[x][y-1].hit == True and self.attackingCells[x][y-1].successful_hit == False
        if(y+1>=10):
            to_bottom = True
        else:
            to_bottom = self.attackingCells[x][y+1].hit == True and self.attackingCells[x][y+1].successful_hit == False
        return [to_top, to_right, to_bottom, to_left]
    

