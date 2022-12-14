"""
Description: File that is used to run the game
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

import tkinter as tk
from gameboard import Gameboard
from gameIntro import GameIntro
from endgame import EndGame
from battleship import battleship
from destroyer import destroyer
from cruiser import cruiser
from submarine import submarine
from carrier import carrier
from ship import ship
from humanPlayer import humanPlayer
from cell import cell
from computerPlayer import computerPlayer
from enum import IntEnum
import random
class Control:
    def __init__(self)->None:
        """ Initializes a game of battleship """
        # Define parameters
        self.NUM_ROWS = 10
        self.NUM_COLS = 10

        #Keeps track of users last clicked cell
        self.lastRow = -1
        self.lastColumn = -1

        #Initilizes a human player (Always going to be at least 1)
        self.player1 = humanPlayer(1, 0, True)

        #Variables to keep track of which player is the one making the move and which player is not
        self.curr_player = self.player1
        self.other_player = 0
        
        # Create view
        self.board1 = GameIntro()
        self.last_cell_clicked = [-1, -1]

        self.ship = ship(0, False)
        self.ship_to_place = False
        self.ready_to_hit = False
        self.ships_placed = 0
        self.done_placing_ships = False
        self.ship_types = [battleship(), carrier(), cruiser(), submarine(), destroyer()]
       
        self.board1.set_human_handler(self.human_handler)
        self.board1.set_ai_handler(self.ai_handler)

        self.ship_types_placed = []
        self.last_ship = ship(0, False)
        self.change_orientation = False
        self.delete_mode = False
        self.mod_color = "gray"
        # Start the simulation
        self.board1.window.mainloop()

    def cell_click_handler1(self, row:int, column:int)->None:
        """
        This handler is for the top 100 cells of the window, mostly for making hits
        """
        if self.done_placing_ships == True:
            #When the user clicks for the second time, we want to reset their last clicked cell to blue
            if (self.lastRow != -1):
                self.board.cells[self.lastRow][self.lastColumn].configure(bg='blue')

            #When the user clicks a cell, we store where the clicked and change the color of the place they clicked from blue to yellow
            #Only able to click cells that they have not previously shot a missle at
            if (self.ships_placed == 5 and self.other_player.shipCells[row][column].hit == False): 
                self.board.cells[row][column].configure(bg='yellow')
                self.lastRow = row
                self.lastColumn = column

    def cell_click_handler2(self, row:int, column:int)->None:
        """
        This handler is for the bottom 100 cells of the window, for placing ships
        """
        if self.delete_mode == True: #ensures it does not place ship if delete mode is on
            if self.curr_player.shipCells[row][column].ship == True:
                self.delete_mode_func(self.curr_player.shipCells[row][column].id)
        else:
            switch_point = -1
            if self.ship == self.last_ship and self.curr_player.shipCells[row][column].id == self.ship.name:
                self.ship.change_orientation()
                self.ship_start = 0
                if not self.ship.horizontal == True: # was horizontal switching to vertical
                    for c in range(self.NUM_COLS):
                        if self.curr_player.shipCells[row][c].id == self.ship.name: # first instance of ship in row
                            self.ship_start = c
                            break
                    # switching to vertical from horixontal
                    switch_point = column-self.ship_start
                    if (row-switch_point >= 0 ) and (row-switch_point+self.ship.length <= self.NUM_ROWS): # if new ship won't go out of bounds, continue on
                            self.clear_ship(row, column-switch_point, 0, self.ship.length, not self.ship.horizontal, self.ship.name) # clear original ship
                            for first_half in range(0, self.ship.length):
                                #check if their is another ship in the way of changing direction
                                if self.curr_player.shipCells[row-switch_point+first_half][column].ship == True and self.curr_player.shipCells[row-switch_point +first_half][column].id != self.ship.name:
                                    self.ship.change_orientation()
                                    self.clear_ship(row-switch_point, column, 0, self.ship.length, not self.ship.horizontal, self.ship.name)
                                    self.place_ship(row, self.ship_start, 0, self.ship.length, self.ship.horizontal, self.ship.name)
                                    break
                
                                else:
                                    self.ship_board_update(row-switch_point+first_half, column)
                    else: #change orientation back
                        self.ship.change_orientation()

                else: # was vertical switching to horizontal
                    for r in range(self.NUM_ROWS):
                        if self.curr_player.shipCells[r][column].id == self.ship.name: # first instance of ship in row
                            self.ship_start = r
                            break
                    switch_point = row-self.ship_start
                    if (column-switch_point >= 0) and (column-switch_point+self.ship.length <= self.NUM_COLS): # if new ship won't go out of bounds, continue on
                            self.clear_ship(row-switch_point, column, 0, self.ship.length, not self.ship.horizontal, self.ship.name)
                            for first_half in range(0, self.ship.length):
                                #check if their is another ship in the way of changing direction
                                if self.curr_player.shipCells[row][column-switch_point+first_half].ship == True and self.curr_player.shipCells[row][column-switch_point+first_half].id != self.ship.name:
                                    self.ship.change_orientation()
                                    self.clear_ship(row, column-switch_point, 0, self.ship.length, not self.ship.horizontal, self.ship.name)
                                    self.place_ship(self.ship_start, column, 0, self.ship.length, self.ship.horizontal, self.ship.name)
                                    break
                                else:
                                    self.ship_board_update(row, column-switch_point+first_half)
                    else: #change orientaation back
                        self.ship.change_orientation()

            #first time placing ship
            elif (self.ship_to_place == True and self.ship not in self.ship_types_placed) and self.curr_player.shipCells[row][column].ship == False: 
                illegal_ship = True
                illegal_index = 0
                if self.ship.horizontal == True: # place ship horizontally
                    if self.ship.length + column <= self.NUM_COLS:
                        for c in range(self.ship.length):
                            if self.curr_player.shipCells[row][c+column].ship == True and self.curr_player.shipCells[row][c+column].id != self.ship.name:
                                illegal_ship = True
                                illegal_index = c
                                break
                            else:
                                self.ship_board_update(row, column+c)
                                illegal_ship = False
                elif self.ship.horizontal == False: #for the computer player to be able to place vertically the first time
                    if self.ship.length + row <= self.NUM_ROWS:
                        for r in range(self.ship.length):
                            if self.curr_player.shipCells[row+r][column].ship == True and self.curr_player.shipCells[row+r][column].id != self.ship.name:
                                illegal_ship = True
                                illegal_index = r
                                break
                            else:
                                self.ship_board_update(row+r, column)
                                illegal_ship = False
   
                if illegal_ship == False:
                    self.ship_to_place = False
                    self.ship_types_placed.append(self.ship.name)
                    self.ships_placed += 1
                    self.last_ship = self.ship
                    self.update_ship_labels(self.ship.name, self.mod_color)
                else: # illegal ship is true
                    self.clear_ship(row, column, 0, illegal_index, self.ship.horizontal, self.ship.name)
                    self.update_ship_labels(self.ship.name, "black")
            else:
                self.update_ship_labels(self.ship.name, "black")

    def ship_board_update(self, row:int, column:int)->None:
        """
        Updates the board and user lists when ship is placed
        """
        self.board.cells2[row][column].configure(bg = "gray")
        self.curr_player.shipCells[row][column].ship = True
        self.curr_player.shipCells[row][column].id = self.ship.name
        if self.ship.name == "destroyer":
            self.curr_player.playerShips["destroyer"] = destroyer()
        elif self.ship.name == "submarine":
            self.curr_player.playerShips["submarine"] = submarine()
        elif self.ship.name == "cruiser":
            self.curr_player.playerShips["cruiser"] = cruiser()
        elif self.ship.name == "battleship":
            self.curr_player.playerShips["battleship"] = battleship()
        else:
            self.curr_player.playerShips["carrier"] = carrier()

    def place_ship(self, row:int, column:int, start_range:int, end_range:int, horizontal:bool, ship_name:str)->None:
        """
        Sets up for loop for placing ships
        """
        if horizontal == True:
            for c in range(start_range, end_range):
                self.ship_board_update(row, c+column)
        else:
            for r in range(start_range, end_range):
                self.ship_board_update(r+row, column)

    def clear_ship(self, row:int, column:int, start_range:int, end_range:int, horizontal:bool, ship_name:str)->None:
        """
        Removes ships from board that are not valid or deleted
        """
        if horizontal == True:
            if column + end_range <= self.NUM_COLS:
                for c in range(start_range, end_range):
                    if self.curr_player.shipCells[row][c+column].id == ship_name:
                        self.board.cells2[row][c+column].configure(bg = "blue")
                        self.curr_player.shipCells[row][c+column].ship = False
                        self.curr_player.shipCells[row][c+column].id = ""
        else:
            if row + end_range <= self.NUM_ROWS:
                for r in range(start_range, end_range):
                    if self.curr_player.shipCells[row+r][column].id == ship_name:
                        self.board.cells2[r+row][column].configure(bg = "blue")
                        self.curr_player.shipCells[r+row][column].ship = False
                        self.curr_player.shipCells[r+row][column].id = ""

    def confirm_hit_handler(self)->None:
        """
        Handler for the confirm hit button
        """
        #Checks to see if the user has chosen a cell to attack or if cell has been attacked already, if not do nothing (Button has no function)
        if (self.lastRow != -1 or self.other_player.shipCells[self.lastRow][self.lastColumn].hit == True):
            #If the cell that is attacked is one with a ship
            if self.other_player.shipCells[self.lastRow][self.lastColumn].ship == True:
                temp = self.other_player.playerShips.get(self.other_player.shipCells[self.lastRow][self.lastColumn].id)
                temp.timeHit += 1
                if temp.isSunk() == True:
                    self.board.shipSinkNotification['text'] = "Player " + str(self.other_player.playerNum) + "'s " + self.other_player.shipCells[self.lastRow][self.lastColumn].id + " has sunk!"
                self.board.cells[self.lastRow][self.lastColumn].configure(bg='red')
                self.curr_player.attackingCells[self.lastRow][self.lastColumn].successful_hit = True
                self.curr_player.incrementHits()
            #No ship in the cell attacked
            else:
                self.board.cells[self.lastRow][self.lastColumn].configure(bg='grey')

            #Changing the hit bool in the selected cell in both players boards
            self.other_player.shipCells[self.lastRow][self.lastColumn].hit = True
            self.curr_player.attackingCells[self.lastRow][self.lastColumn].hit = True

            #resets lastRow and lastColumn
            self.lastRow = -1
            self.lastColumn = -1 
                
            #If no one has won, we update window to show other players ships and attacking board
            
            self.board.window.update()
            self.board.window.after(1000, self.update_player())

    def update_player(self)->None:
        """
        Switches player and updates the screen
        """
        if (self.curr_player.numOfHits == 17): #check game over
            self.board.window.destroy()
            self.end_game_setup()
        else: #game not over yet
            self.board.shipSinkNotification['text'] = ""

            #Updates curr_player and other_player
            if (self.curr_player.playerNum == 1):
                self.curr_player = self.player2
                self.other_player = self.player1
            else:
                self.curr_player = self.player1
                self.other_player = self.player2

            #Updating the game board, hits and player turn
            self.board.your_hits['text'] = "Your Hits: " + str(self.curr_player.numOfHits)
            self.board.opponent['text'] = "Opponent: " + str(self.other_player.numOfHits)
            
            if self.curr_player.is_human == True:
                if self.player2.is_human == True:
                    if (self.curr_player.playerNum == 2):
                        self.board.player['text'] = "PLAYER 2S TURN"
                    else:
                        self.board.player['text'] = "PLAYER 1S TURN"

                    self.player_switch_screen_management(False)

                #Updates window for the curr_player
                self.update_cells()
            else:
                self.player2.computer_hit(self.other_player.shipCells, self.other_player.playerShips)
                self.update_player()

    def end_game_setup(self)->None:
        """
        For endgame, displays winner and allows for reset of game
        """
        self.end_board = EndGame()
        self.end_board.who_won['text'] = "PLAYER " + str(self.curr_player.playerNum) + " WON"
        self.end_board.set_quit_handler(self.quit_handler)
        self.end_board.set_repeat_handler(self.repeat_handler)
        self.end_board.window.mainloop()

    def board_setup(self)->None:
        """
        Sets up gameboard once type of game is chosen
        """
        # Cell clicks.  (Note that a separate handler function is defined for 
        # each cell.)
        self.board = Gameboard(self.NUM_ROWS, self.NUM_COLS)
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                def handler(event, row = r, column = c):
                    self.cell_click_handler1(row, column)
                self.board.set_cell_click_handler_top(r, c, handler)

        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                def handler(event, row = r, column = c):
                    self.cell_click_handler2(row, column)
                self.board.set_cell_click_handler_bottom(r, c, handler)
        def handler(event):
            self.confirm_hit_handler()
        self.board.set_confirm_hit_handler(handler)

        self.initializing_board_handlers()
        self.player_switch_screen_management()
        self.board.window.mainloop()

    def initializing_board_handlers(self)->None:
        """
        Initializes all handlers for the gameboard
        """
        self.board.set_battleship_handler(self.battleship_handler)
        self.board.set_carrier_handler(self.carrier_handler)
        self.board.set_submarine_handler(self.submarine_handler)
        self.board.set_cruiser_handler(self.cruiser_handler)
        self.board.set_destroyer_handler(self.destroyer_handler)
        self.board.set_done_placing_ships_handler(self.done_placing_ships_handler)
        self.board.set_delete_ship_handler(self.delete_ship_handler)
        self.board.set_random_ships_handler(self.place_random_ships)
        self.board.set_switch_players_handler(self.player_switch_screen_management)

    def player_switch_screen_management(self, delete:bool = True)->None:
        """
        Covers board when players switch to ensure fairness of game
        """
        if delete == True:
            self.board.switch_frame.grid_remove()
        else:
            self.board.switch_frame.grid()
            self.board.switch_players.configure(fg = "black")
            self.board.switch_players.configure(text = "Player "+str(self.curr_player.playerNum) +": Ready to Play!")

    def delete_mode_func(self, ship_name:str)->None:
        """
        Deletes ships from board
        """
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                if (self.curr_player.shipCells[r][c].id == ship_name):
                    self.board.cells2[r][c].configure(bg="blue")  
                    self.curr_player.shipCells[r][c].id = ""
                    self.curr_player.shipCells[r][c].ship = False
        
        self.ships_placed -= 1
        self.ship_types_placed.remove(ship_name)
        self.update_ship_labels(ship_name, "black")

    def update_ship_labels(self, ship_name:str, color:str)->None:
        """
        Changes the button text colors when pressed
        """
        if ship_name == "carrier":
            self.board.carrier.configure(fg = color)
        elif ship_name == "destroyer":
            self.board.destroyer.configure(fg = color)
        elif ship_name == "battleship":
            self.board.battleship.configure(fg = color)
        elif ship_name == "submarine":
            self.board.submarine.configure(fg = color)
        elif ship_name == "cruiser":
            self.board.cruiser.configure(fg = color)

    def delete_ship_handler(self)->None:
        """
        Handles the delete mode switches
        """
        if self.delete_mode == False:
            self.board.delete_ship['text'] = "Delete Mode: ON"
            self.delete_mode = True
        else:
            self.board.delete_ship['text'] = "Delete Mode: OFF"
            self.delete_mode = False

    def done_placing_ships_handler(self)->None:
        """
        Switches player and ensures player is done placing ships
        """
        # checks to ensure first player is done
        if self.ships_placed == 5 and self.curr_player == self.player1:
            self.curr_player = self.player2
            self.ships_placed = 0
            self.reset_cells2()
            for s in self.ship_types_placed:
                self.update_ship_labels(s, "black")
            self.ship_types_placed = []
            self.board.player['text'] = "PLAYER 2: Place your ships"
            
            # if against a computer player, place computer ships automatically and allow player one to hit
            if self.player2.is_human == False: 
                # randomly placing ships
                self.place_random_ships()
                self.curr_player = self.player1
                self.update_cells()
                self.board.ship_frame.destroy()
                self.done_placing_ships = True
                self.board.player['text'] = "PLAYER 1S TURN"

        # ensures player 2 is done placing ships 
        elif self.ships_placed == 5 and self.curr_player == self.player2:
            self.curr_player = self.player1
            self.player_switch_screen_management(False)
            self.update_cells()
            self.board.ship_frame.destroy()
            self.board.player['text'] = "PLAYER 1S TURN"
            self.done_placing_ships = True

    def ship_list(self)->list:
        """
        Returns a list containing the ship objects that have been placed
        """
        ship_list = []
        for ship in self.ship_types:
            if ship.name not in self.ship_types_placed:
                ship_list.append(ship)
        return ship_list

    def place_random_ships(self)->None:
        """
        Places ships on board randomly
        """
        if self.ships_placed != 5 and self.delete_mode == False:
            ship_list = self.ship_list()
            for ship in ship_list:
                self.ship_to_place = True
                self.ship = ship
                self.ship.orientation = bool(random.randint(0,1))
                self.update_ship_labels(self.ship.name, self.mod_color)
                while self.ship.name not in self.ship_types_placed:
                    self.cell_click_handler2(random.randint(0,9), random.randint(0, 9))

    def carrier_handler(self)->None:
        """
        Handles when the carrier ship type button is pushed, and ensures push is legal
        """
        if "carrier" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = carrier()
            self.board.carrier.configure(fg = self.mod_color)
   
    def battleship_handler(self)->None:
        """
        Handles when the battleship ship type button is pushed, and ensures push is legal
        """  
        if "battleship" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = battleship()
            self.board.battleship.configure(fg = self.mod_color)

    def submarine_handler(self)->None:
        """
        Handles when the submarine ship type button is pushed, and ensures push is legal
        """
        if "submarine" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = submarine()
            self.board.submarine.configure(fg = self.mod_color)

    def cruiser_handler(self)->None:
        """
        Handles when the cruiser ship type button is pushed, and ensures push is legal
        """
        if "cruiser" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = cruiser()
            self.board.cruiser.configure(fg = self.mod_color)

    def destroyer_handler(self)->None:
        """
        Handles when the destroyer ship type button is pushed, and ensures push is legal
        """
        if "destroyer" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = destroyer()
            self.board.destroyer.configure(fg = self.mod_color)

    def reset_cells2(self)->None:
        """
        Resets all cells on bottom board to blue
        """
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                self.board.cells2[r][c].configure(bg="blue")   

    def update_cells(self)->None:
        """
        Updates window with the curr_players ship and attacking board
        """
        #Nested for loop to go through all cells
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                #For upper 100 cells
                #If there was a ship, and its been hit
                if (self.other_player.shipCells[r][c].ship == True and self.curr_player.attackingCells[r][c].hit == True):
                    self.board.cells[r][c].configure(bg="red")
                #If there was a hit with no ship
                elif (self.curr_player.attackingCells[r][c].hit == True):
                    self.board.cells[r][c].configure(bg="grey")
                #No hit or ship
                else:
                    self.board.cells[r][c].configure(bg="blue")

                #For lower 100 cells
                #If there was a ship, and its been hit
                if (self.curr_player.shipCells[r][c].ship == True and self.other_player.attackingCells[r][c].hit == True):
                    self.board.cells2[r][c].configure(bg="orange")
                #If there is a ship no hit
                elif(self.curr_player.shipCells[r][c].ship == True):
                    self.board.cells2[r][c].configure(bg="grey")
                #If there was a hit no ship
                elif(self.other_player.attackingCells[r][c].hit == True):
                    self.board.cells2[r][c].configure(bg="black")
                #No ship no hit
                else:
                    self.board.cells2[r][c].configure(bg="blue")         

    def human_handler(self)->None:
        """
        Handles when human vs human button is pushed
        """
        self.player2 = humanPlayer(2, 0, False)
        self.other_player = self.player2
        self.board1.window.destroy()
        self.board_setup()

    def ai_handler(self)->None:
        """
        Handles when human vs computer is pushed
        """  
        self.player2 = computerPlayer(2, 0, False)
        self.other_player = self.player2
        self.board1.window.destroy()
        self.board_setup()
    
    def quit_handler(self)->None:
        """
        Once game has ended, allow for window to be quit
        """
        self.end_board.window.destroy()

    def repeat_handler(self)->None:
        """
        Allows game to be repeated
        """
        self.end_board.window.destroy()
        self.__init__()

if __name__ == "__main__":
    battleship = Control()