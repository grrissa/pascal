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

        self.last_missile_success = False
        self.direction = 0
        self.curr_direction = 0
        self.original_success = (-1,-1)
        self.last_hit = (-1, -1)


    def random_ints(self):
        return random.randint(0,9), random.randint(0,9)

    def computer_hit(self, other_player_ships):

        # if we should make a random computer hit or a smart computer hit
        if self.last_missile_success == True:
            next_x = -1
            next_y = -1
            
            if self.direction == 0:
                valid = False

                self.direction = random.randint(1,4)
                while valid == False:
                    self.curr_direction = self.direction

                    if self.direction == 1:
                        next_x = self.original_success[0]
                        next_y = self.original_success[1]-1
                        self.direction = 2
                        
                    elif self.direction == 2:
                        next_x = self.original_success[0]+1
                        next_y = self.original_success[1]
                        self.direction = 3

                    elif self.direction == 3:
                        next_x = self.original_success[0]
                        next_y = self.original_success[1]+1
                        self.direction = 4

                    else:
                        next_x = self.original_success[0] - 1
                        next_y = self.original_success[1]
                        self.direction = 1

                    if not(self.attackingCells[next_x][next_y].hit == True or next_x < 0 or next_x > 9 or next_y < 0 or next_y > 9):
                        valid = True

            else:
                valid = False
                center_x = self.last_hit[0]
                center_y = self.last_hit[1]

                while valid == False:
                    if self.curr_direction == 1:
                        next_y = center_y - 1
                    elif self.curr_direction == 2:
                        next_x = center_x + 1               
                    elif self.curr_direction == 3:
                        next_y = center_y - 1
                    else:
                        next_x = center_x - 1
                    
                    if not(self.attackingCells[next_x][next_y].hit == True or next_x < 0 or next_x > 9 or next_y < 0 or next_y > 9):
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
            self.incrementHits()
            self.attackingCells[next_x][next_y].successful_hit = True
            print("comp hit!")

        #Changing the hit bool in the selected cell in both players boards
        other_player_ships[next_x][next_y].hit = True
        self.attackingCells[next_x][next_y].hit = True 
        
        self.last_hit = (next_x, next_y)

            

    

