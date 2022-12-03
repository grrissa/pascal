"""
Description: Class to create GUI gameboard
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

import tkinter as tk
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
ship_types = [battleship(), carrier(), cruiser(), submarine(), destroyer()]

class Control:
    """ The controller. """
    def __init__(self):
        """ Initializes the game of life """
        # Define parameters
        self.NUM_ROWS = 10
        self.NUM_COLS = 10

        self.lastRow = -1
        self.lastColumn = -1

        self.lastRow2 = -1
        self.lastColumn2 = -1

        self.player1 = humanPlayer(1, 0, True)

        self.curr_player = self.player1
        self.other_player = 0
        
        # Create view
        self.board1 = GameIntro()
        self.last_cell_clicked = [-1, -1]

        


        self.ship = ship(0, False)
        self.ship_to_place = False
        self.ready_to_hit = False
        self.ships_placed = 0
        #Deleted parameters
        self.ship_types = [battleship(), carrier(), cruiser(), submarine(), destroyer()]
       
        #AIDAN START copied and pasted code down
        self.board1.set_human_handler(self.human_handler)
        self.board1.set_ai_handler(self.ai_handler)
        #AIDAN FINISH copied and pasted code down

        self.ship_types_placed = []
        self.last_ship = ship(0, False)
        self.change_orientation = False
        self.delete_mode = False
        self.mod_color = "gray"
        #AIDANS ADDED CODE
        self.player1.setHits(self.ship_types)
        
        # Start the simulation
        self.board1.window.mainloop()
   
    #New Code written by AIDAN

     

    def cell_click_handler1(self, row, column):
        """ Cell click """
        print("Cell click: row = %d col = %d and is in top frame" % (row, column))

        if (self.lastRow != -1):
            self.board.cells[self.lastRow][self.lastColumn].configure(bg='blue')
        
        #print(self.other_player.shipCells[row][column].hit)
        if (self.ships_placed == 5 and self.other_player.shipCells[row][column].hit == False): 
        #self.other_player.shipCells[row][column].ship == True):

            #AIDANS added code
           # print(self.curr_player.hit)
            #print(self.other_player.shipCells[row][column].id)
            #self.curr_player.hit[self.other_player.shipCells[row][column].id] += 1
            #self.other_player.shipCells[row][column].hit = True

            #We need find equivalent size to this cell
            #if (self.curr_player.hit[self.other_player.shipCells[row][column].id] == self.curr_player.ship_size[self.other_player.shipCells[row][column].id]):
               # print(self.curr_player.shipCells[row][column].id)
               # print("ship sunk")
            
            ##Aidans Code 
            self.board.cells[row][column].configure(bg='yellow')
            self.lastRow = row
            self.lastColumn = column
    
    def shipSunk(self, row, column):
        print(self.other_player.shipCells[row][column].hit)
        if (self.ships_placed == 5 and  self.other_player.shipCells[row][column].ship == True):

            #AIDANS added code
            print(self.curr_player.hit)
            print(self.other_player.shipCells[row][column].id)
            self.curr_player.hit[self.other_player.shipCells[row][column].id] += 1
            #self.other_player.shipCells[row][column].hit = True

            #We need find equivalent size to this cell
            if (self.curr_player.hit[self.other_player.shipCells[row][column].id] == self.curr_player.ship_size[self.other_player.shipCells[row][column].id]):
                print(self.curr_player.shipCells[row][column].id)
                print("ship sunk")

    
    def cell_click_handler2(self, row, column) -> bool:
        """ Cell click """
        print("Cell click: row = %d col = %d" % (row, column))
        if self.delete_mode == True:
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
                    # switching to vertical
                    switch_point = column-self.ship_start
                    if (row-switch_point >= 0 ) and (row-switch_point+self.ship.length <= self.NUM_ROWS): # if new ship won't go out of bounds, continue on
                            self.clear_ship(row, column-switch_point, 0, self.ship.length, not self.ship.horizontal, self.ship.name) # clear original ship
                            for first_half in range(0, self.ship.length):
                                if self.curr_player.shipCells[row-switch_point+first_half][column].ship == True and self.curr_player.shipCells[row-switch_point +first_half][column].id != self.ship.name:
                                    self.ship.change_orientation()
                                    self.clear_ship(row-switch_point, column, 0, self.ship.length, not self.ship.horizontal, self.ship.name)
                                    self.place_ship(row, self.ship_start, 0, self.ship.length, self.ship.horizontal, self.ship.name)
                                    break
                
                                else:
                                    self.board.cells2[row-switch_point+first_half][column].configure(bg = "gray")
                                    self.curr_player.shipCells[row-switch_point+first_half][column].ship = True
                                    self.curr_player.shipCells[row-switch_point+first_half][column].id = self.ship.name
                    else:
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
                                if self.curr_player.shipCells[row][column-switch_point+first_half].ship == True and self.curr_player.shipCells[row][column-switch_point+first_half].id != self.ship.name:
                                    self.ship.change_orientation()
                                    self.clear_ship(row, column-switch_point, 0, self.ship.length, not self.ship.horizontal, self.ship.name)
                                    self.place_ship(self.ship_start, column, 0, self.ship.length, self.ship.horizontal, self.ship.name)
                                    break
                                else:
                                    self.board.cells2[row][column-switch_point+first_half].configure(bg = "gray")
                                    self.curr_player.shipCells[row][column-switch_point+first_half].ship = True
                                    self.curr_player.shipCells[row][column-switch_point+first_half].id = self.ship.name
                    else:
                        self.ship.change_orientation()

            elif (self.ship_to_place == True and self.ship not in self.ship_types_placed) and self.curr_player.shipCells[row][column].ship == False:
                illegal_ship = False
                illegal_index = 0
                if self.ship.horizontal == True:
                    if self.ship.length + column <= self.NUM_COLS:
                        for c in range(self.ship.length):
                            if self.curr_player.shipCells[row][c+column].ship == True and self.curr_player.shipCells[row][c+column].id != self.ship.name:
                                illegal_ship = True
                                illegal_index = c
                                break
                            else:
                                self.board.cells2[row][c+column].configure(bg = "gray")
                                self.curr_player.shipCells[row][c+column].ship = True
                                self.curr_player.shipCells[row][c+column].id = self.ship.name

   
                if illegal_ship == False:
                    self.ship_to_place = False
                    self.ship_types_placed.append(self.ship.name)
                    self.ships_placed += 1
                    self.last_ship = self.ship
                else: # illegal ship is true
                    self.clear_ship(row, column, 0, illegal_index, self.ship.horizontal, self.ship.name)
        

    def place_ship(self, row, column, start_range, end_range, horizontal, ship_name):
        if horizontal == True:
            for c in range(start_range, end_range):
                self.board.cells2[row][c+column].configure(bg = "gray")
                self.curr_player.shipCells[row][c+column].ship = True
                self.curr_player.shipCells[row][c+column].id = ship_name
        else:
            for r in range(start_range, end_range):
                self.board.cells2[row+r][column].configure(bg = "gray")
                self.curr_player.shipCells[row+r][column].ship = True
                self.curr_player.shipCells[row+r][column].id = ship_name

    def clear_ship(self, row, column, start_range, end_range, horizontal, ship_name):
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

    def confirm_hit_handler(self):
        if (self.lastRow != -1):
            print("Confirmed hit on row = %d col = %d" % (self.lastRow, self.lastColumn))
        else:
            return

        
        print(self.lastRow, self.lastColumn)
        if self.other_player.shipCells[self.lastRow][self.lastColumn].ship == True:
            if (self.other_player.shipCells[self.lastRow][self.lastColumn].hit == False):
                self.board.cells[self.lastRow][self.lastColumn].configure(bg='red')
                self.other_player.shipCells[self.lastRow][self.lastColumn].hit = True
                self.curr_player.attackingCells[self.lastRow][self.lastColumn].hit = True
                self.curr_player.incrementHits()
                self.lastRow = -1
        else:
            self.board.cells[self.lastRow][self.lastColumn].configure(bg='grey')
            self.other_player.shipCells[self.lastRow][self.lastColumn].hit = True
            self.curr_player.attackingCells[self.lastRow][self.lastColumn].hit = True
            self.lastRow = -1
        #THIS IS OUR ENDGAME CHECKER!! CURRENTLY ONLY QUITS WINDOW, NEED TO CHANGE TO SPEPERATE WINDOW WITH GAME WINNER INSTEAD
        if (self.curr_player.numOfHits == 17):
            self.board.window.destroy()
            self.end_game_setup()
        else:
            self.board.window.update()
            self.board.window.after(1000, self.update_player())

        
    def update_player(self):   
        if (self.curr_player.playerNum == 1):
            self.curr_player = self.player2
            self.other_player = self.player1
            self.player1.is_turn = False
            self.player2.is_turn = True
        else:
            self.curr_player = self.player1
            self.other_player = self.player2
            self.player1.is_turn = False
            self.player2.is_turn = True

            self.player2.is_turn = False
            self.player1.is_turn = True

        # updating the game board
        self.board.your_hits['text'] = "Your Hits: " + str(self.player1.numOfHits)
        self.board.opponent['text'] = "Opponent: " + str(self.player2.numOfHits)
        if (self.curr_player.playerNum == 1):
            self.board.player['text'] = "PLAYER 2S TURN"
        else:
            self.board.player['text'] = "PLAYER 1S TURN"

        print("it is player " + str(self.curr_player.playerNum) + "s turn")
        self.update_cells()

    def end_game_setup(self):
        self.end_board = EndGame()
        self.end_board.who_won['text'] = "PLAYER " + str(self.curr_player.playerNum) + " WON"
        self.end_board.set_quit_handler(self.quit_handler)
        self.end_board.set_repeat_handler(self.repeat_handler)
        self.end_board.window.mainloop()

    def board_setup(self):
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
        self.board.window.mainloop()

    def initializing_board_handlers(self): 
        self.board.set_battleship_handler(self.battleship_handler)
        self.board.set_carrier_handler(self.carrier_handler)
        self.board.set_submarine_handler(self.submarine_handler)
        self.board.set_cruiser_handler(self.cruiser_handler)
        self.board.set_destroyer_handler(self.destroyer_handler)
        self.board.set_done_placing_ships_handler(self.done_placing_ships_handler)
        self.board.set_delete_ship_handler(self.delete_ship_handler)

    def delete_mode_func(self, ship_name):
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                if (self.curr_player.shipCells[r][c].id == ship_name):
                    self.board.cells2[r][c].configure(bg="blue")  
                    self.curr_player.shipCells[r][c].id = ""
                    self.curr_player.shipCells[r][c].ship = False
        
        self.ships_placed -= 1
        self.ship_types_placed.remove(ship_name)
        self.update_ship_labels(ship_name)

    def update_ship_labels(self, ship_name):
        if ship_name == "carrier":
            self.board.carrier.configure(fg = "black")
        elif ship_name == "destroyer":
            self.board.destroyer.configure(fg = "black")
        elif ship_name == "battleship":
            self.board.battleship.configure(fg = "black")
        elif ship_name == "submarine":
            self.board.submarine.configure(fg = "black")
        elif ship_name == "cruiser":
            self.board.cruiser.configure(fg = "black")
        else:
            print("invalid ship name")

    def delete_ship_handler(self):
        print("delete mode on")
        if self.delete_mode == False:
            self.board.delete_ship['text'] = "Delete Mode: ON"
            self.delete_mode = True
        else:
            self.board.delete_ship['text'] = "Delete Mode: OFF"
            self.delete_mode = False

    def done_placing_ships_handler(self):
        print("done placing ships button was pushed")
        if self.ships_placed == 5 and self.curr_player == self.player1:
            self.curr_player = self.player2
            self.ships_placed = 0
            self.reset_cells2()
            for s in self.ship_types_placed:
                self.update_ship_labels(s)
            self.ship_types_placed = []
            self.board.player['text'] = "PLAYER 2: Place your ships"

            if self.player2.is_human == False:
                # randomly placing ships
                for i in range(5):
                    self.ship = self.ship_types[i]
                    self.ship.set_orientation(bool(random.randint(0,1)))    
                    
                    self.cell_click_handler2(random.randint(0,9), random.randint(0, 9))

                self.curr_player = self.player1
                self.update_cells()
                self.board.ship_frame.destroy()
                self.board.player['text'] = "PLAYER 1S TURN"

            
        elif self.ships_placed == 5 and self.curr_player == self.player2:
            self.curr_player = self.player1
            self.update_cells()
            self.board.ship_frame.destroy()
            self.board.player['text'] = "PLAYER 1S TURN"

    def carrier_handler(self):
        print("carrier button was pushed")
        if "carrier" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = carrier()
            self.board.carrier.configure(fg = self.mod_color)
            
    def battleship_handler(self):
        print("battleship button was pushed")
        if "battleship" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = battleship()
            self.board.battleship.configure(fg = self.mod_color)

    def submarine_handler(self):
        print("submarine button was pushed")
        if "submarine" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = submarine()
            self.board.submarine.configure(fg = self.mod_color)
        
    def cruiser_handler(self):
        print("cruiser button was pushed")
        if "cruiser" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = cruiser()
            self.board.cruiser.configure(fg = self.mod_color)
        
    def destroyer_handler(self):
        print("destroyer button was pushed")
        if "destroyer" not in self.ship_types_placed and self.delete_mode == False:
            self.ship_to_place = True
            self.ship = destroyer()
            self.board.destroyer.configure(fg = self.mod_color)

    def reset_cells2(self):
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                self.board.cells2[r][c].configure(bg="blue")   

    def update_cells(self):
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                
                if (self.other_player.shipCells[r][c].ship == True and self.curr_player.attackingCells[r][c].hit == True):
                    self.board.cells[r][c].configure(bg="red")
                elif (self.curr_player.attackingCells[r][c].hit == True):
                    self.board.cells[r][c].configure(bg="grey")
                else:
                    self.board.cells[r][c].configure(bg="blue")

                if (self.curr_player.shipCells[r][c].ship == True and self.other_player.attackingCells[r][c].hit == True):
                    self.board.cells2[r][c].configure(bg="orange")
                elif(self.curr_player.shipCells[r][c].ship == True):
                    self.board.cells2[r][c].configure(bg="grey")
                elif(self.other_player.attackingCells[r][c].hit == True):
                    self.board.cells2[r][c].configure(bg="black")
                else:
                    self.board.cells2[r][c].configure(bg="blue")         


    def human_handler(self):
        """ Start (or restart) simulation by scheduling the next step. """
        self.player2 = humanPlayer(2, 0, False)
        self.player2.setHits(ship_types) #AIDANS CODE

        self.other_player = self.player2
        print("human button pressed")
        self.board1.window.destroy()
        self.board_setup()
            
    def ai_handler(self):
        """ Pause simulation """
        self.player2 = computerPlayer(2, 0, False)
        self.other_player = self.player2
        #Aidans Code START
        self.player2.setHits(ship_types)
        #Aidans Code FINISH
        print("ai button pressed")
        self.board1.window.destroy()
        self.board_setup()
    
    def quit_handler(self):
        self.end_board.window.destroy()
    def repeat_handler(self):
        self.end_board.window.destroy()
        self.__init__()
        

class EndGame:
    def __init__(self):
        """ Initialize view of the game """
        # Constants
        self.CONTROL_FRAME_HEIGHT = 700

        # Create window
        self.window = tk.Tk()
        self.window.title("Battleship")

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = self.CONTROL_FRAME_HEIGHT, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 1, column = 2, padx=40, pady=40)
        (self.repeat_button, self.quit_button, self.who_won) = self.add_control()

    def add_control(self):
        """ 
        Create control buttons and welcome message, and add them to the control frame 
        """
        welcome = tk.Label(self.control_frame, text="Game has ended", font=("Helvetica", 20))
        welcome.grid(row=1, column = 1)

        who_won = tk.Label(self.control_frame, text="", font=("Helvetica", 20))
        who_won.grid(row=2, column = 1)

        repeat_button = tk.Button(self.control_frame, text="Repeat Game?", font=("Helvetica", 10))
        repeat_button.grid(row=3, column=1)

        quit_button = tk.Button(self.control_frame, text="Quit", font=("Helvetica", 10))
        quit_button.grid(row=4, column=1)

        return (repeat_button, quit_button, who_won)

    def set_repeat_handler(self, handler):
        """ set handler for clicking on start button to the function handler """
        self.repeat_button.configure(command = handler)

    def set_quit_handler(self, handler):
        """ set handler for clicking on pause button to the function handler """
        self.quit_button.configure(command = handler)

class GameIntro:
    def __init__(self):
        """ Initialize view of the game """
        # Constants
        self.CONTROL_FRAME_HEIGHT = 500

        # Create window
        self.window = tk.Tk()
        self.window.title("Battleship")

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = self.CONTROL_FRAME_HEIGHT, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 1, column = 2, padx=40, pady=40)
        (self.human_button, self.ai_button) = self.add_control()

    def add_control(self):
        """ 
        Create control buttons and welcome message, and add them to the control frame 
        """
        welcome = tk.Label(self.control_frame, text="Welcome to Battleship", font=("Helvetica", 20))
        welcome.grid(row=1, column = 1)

        human_button = tk.Button(self.control_frame, text="Human vs Human", font=("Helvetica", 10))
        human_button.grid(row=2, column=1)

        ai_button = tk.Button(self.control_frame, text="Human vs Computer", font=("Helvetica", 10))
        ai_button.grid(row=3, column=1)

        return (human_button, ai_button)

    def set_human_handler(self, handler):
        """ set handler for clicking on start button to the function handler """
        self.human_button.configure(command = handler)

    def set_ai_handler(self, handler):
        """ set handler for clicking on pause button to the function handler """
        self.ai_button.configure(command = handler)

class Gameboard:
    """ The view """

    def __init__(self, num_rows, num_cols):
        """ Initialize view of the game """
        # Constants
        self.CELL_SIZE = 30
        self.CONTROL_FRAME_HEIGHT = 500

        # Size of grid
        self.num_rows = num_rows
        self.num_cols = num_cols

        # Create window
        self.window = tk.Tk()
        self.window.title("Battleship")


        # GRID ONE: Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(self.window, height = num_rows * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.grid_frame.grid(row = 1, column = 1, padx=40, pady=20)
        self.cells = self.add_cells()

        # GRID 2: Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(self.window, height = num_rows * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.grid_frame.grid(row = 2, column = 1, padx=40, pady=20)
        self.cells2 = self.add_cells()

        # GRID 2: Create frame for grid of cells, and put cells in the frame
        self.ship_frame = tk.Frame(self.window, height = num_cols * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.ship_frame.grid(row = 2, column = 2, padx=40, pady=40)
        (self.delete_ship, self.done_placing_ships, self.carrier, self.battleship, self.submarine, self.cruiser, self.destroyer) = self.ship_buttons()

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = num_cols * self.CELL_SIZE, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 1, column = 2, padx=40, pady=40)
        ( self.start_button, self.quit_button, self.label1,
            self.confirm_button, self.your_hits, self.opponent, self.player) = self.add_control()

    
    def ship_buttons(self):
        """ 
        Create buttons to choose ship
        """
        done_placing_ships = tk.Button(self.ship_frame, text="Done Placing Ships", font=("Helvetica", 20))
        done_placing_ships.grid(row=1, column = 1)

        delete_ship = tk.Button(self.ship_frame, text="Delete Mode: OFF", font=("Helvetica", 15))
        delete_ship.grid(row=2, column = 1)

        carrier = tk.Button(self.ship_frame, text="Carrier (5 cells)", font=("Helvetica", 10))
        carrier.grid(row=3, column=1)

        battleship = tk.Button(self.ship_frame, text="Battleship (4 cells)", font=("Helvetica", 10))
        battleship.grid(row=4, column=1)

        submarine = tk.Button(self.ship_frame, text="Submarine (3 cells)", font=("Helvetica", 10))
        submarine.grid(row=5, column = 1)

        cruiser = tk.Button(self.ship_frame, text="Cruiser (3 cells)", font=("Helvetica", 10))
        cruiser.grid(row=6, column = 1)

        destroyer = tk.Button(self.ship_frame, text="Destroyer (2 cells)", font=("Helvetica", 10))
        destroyer.grid(row=7, column = 1)

        return (delete_ship, done_placing_ships, carrier, battleship, submarine, cruiser, destroyer)

    def set_done_placing_ships_handler(self, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.done_placing_ships.configure(command = handler)
    
    def set_delete_ship_handler(self, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.delete_ship.configure(command = handler)

    def set_carrier_handler(self, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.carrier.configure(command = handler)

    def set_battleship_handler(self, handler):
        """ set handler for clicking on start button to the function handler """
        self.battleship.configure(command = handler)

    def set_submarine_handler(self, handler):
        """ set handler for clicking on pause button to the function handler """
        self.submarine.configure(command = handler)

    def set_cruiser_handler(self, handler):
        """ set handler for clicking on step button to the function handler """
        self.cruiser.configure(command = handler)

    def set_destroyer_handler(self, handler):
        """ set handler for clicking on reset button to the function handler """
        self.destroyer.configure(command = handler)

    def add_control(self):
        """ 
        Create control buttons and welcome message, and add them to the control frame 
        """
        start_button = tk.Button(self.control_frame, text="Start", font=("Helvetica", 10))
        start_button.grid(row=1, column=1)

        quit_button = tk.Button(self.control_frame, text="Quit", font=("Helvetica", 10), command=quit)
        quit_button.grid(row=1, column=2)

        label1 = tk.Label(self.control_frame, text="Welcome to Battleship", font=("Helvetica", 20))
        label1.grid(row=2)

        confirm_button = tk.Button(self.control_frame, text="Confirm Hit", font=("Helvetica", 20))
        confirm_button.grid(row=3)

        your_hits = tk.Label(self.control_frame, text="Your Hits: 0", font=("Helvetica", 10))
        your_hits.grid(row=4)

        opponent = tk.Label(self.control_frame, text="Opponent: 0", font=("Helvetica", 10))
        opponent.grid(row=5)

        player = tk.Label(self.control_frame, text="PLAYER 1: Place your ships", font=("Helvetica", 20))
        player.grid(row=7)

        return (start_button, quit_button, label1, confirm_button, your_hits, opponent, player)

    def add_cells(self):
        """ Add cells to the view """
        cells = []
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                frame = tk.Frame(self.grid_frame, width = self.CELL_SIZE, 
                        height = self.CELL_SIZE, borderwidth = 1, 
                        relief = "solid", background="blue")
                frame.grid(row = r, column = c)
                row.append(frame)
            cells.append(row)
        return cells

    def set_cell_click_handler_top(self, row, column, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.cells[row][column].bind('<Button-1>', handler)

    def set_cell_click_handler_bottom(self, row, column, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.cells2[row][column].bind('<Button-1>', handler)

    def set_confirm_hit_handler(self, handler):
        self.confirm_button.bind('<Button-1>', handler)

    def quit(self):
        """ Functionality for quit button """
        self.window.destroy()

if __name__ == "__main__":
    game_of_life = Control()