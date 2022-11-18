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

        self.player1_hits = 0
        self.player2_hits = 0
        
        # Create view
        self.board1 = GameIntro()
        self.last_cell_clicked = [-1, -1]

        self.board1.set_human_handler(self.human_handler)
        self.board1.set_ai_handler(self.ai_handler)


        self.ship = ship(0, False)
        self.ship_to_place = False
        self.ready_to_hit = False
        self.ships_placed = 0
        
        # Start the simulation
        self.board1.window.mainloop()

    def cell_click_handler1(self, row, column):
        """ Cell click """
        print("Cell click: row = %d col = %d and is in top frame" % (row, column))

        if (self.lastRow != -1):
            self.board.cells[self.lastRow][self.lastColumn].configure(bg='blue')
        
        if self.ships_placed == 5:
            self.board.cells[row][column].configure(bg='red')
            self.lastRow = row
            self.lastColumn = column

    
    def cell_click_handler2(self, row, column):
        """ Cell click """
        print("Cell click: row = %d col = %d" % (row, column))
        
        if self.ship_to_place == True:
            illegal_ship = False
            if self.ship.horizontal == True:
                if self.ship.length + column > self.NUM_COLS:
                    print("ship will go out of range")
                else:
                    for c in range(self.ship.length):
                        if self.curr_player.shipCells[row][c+column].ship == True:
                            print("attempting to place ship illegally")
                            illegal_ship = True
                        else:
                            self.board.cells2[row][c+column].configure(bg = "gray")
                            self.curr_player.shipCells[row][c+column].ship = True
                            self.curr_player.shipCells[row][c+column].id = self.ship.name
                    if illegal_ship == False:
                        self.ship_to_place = False
                        self.ships_placed += 1
            else:
                if self.ship.length + row > self.NUM_ROWS:
                    print("ship will go out of range")
                else:
                    for r in range(self.ship.length):
                        if self.curr_player.shipCells[row][c+column].ship == True:
                            print("attempting to place ship illegally")
                            illegal_ship = True
                        else:
                            self.board.cells2[r+row][column].configure(bg = "gray")
                            self.curr_player.shipCells[r+row][column].ship = True
                            self.curr_player.shipCells[r+row][column].id = self.ship.name
                    if illegal_ship == False:
                        self.ship_to_place = False
                        self.ships_placed += 1
        else:
            if (self.lastRow2 != -1):
                self.board.cells2[self.lastRow2][self.lastColumn2].configure(bg='blue')
         
        self.lastRow2 = row
        self.lastColumn2 = column

            

    def confirm_hit_handler(self):
        if (self.lastRow != -1):
            print("Confirmed hit on row = %d col = %d" % (self.lastRow, self.lastColumn))
        else:
            return

        if self.curr_player.shipCells[self.lastRow][self.lastColumn].ship == True:
                self.board.cells[self.lastRow][self.lastColumn].configure(bg='red')
                self.curr_player.attackingCells[self.lastRow][self.lastColumn].hit = True
                if (self.curr_player == self.player1):
                    self.player1_hits +=1
                else:
                    self.player2_hits +=1
                self.lastRow = -1
        else:
            self.board.cells[self.lastRow][self.lastColumn].configure(bg='grey')
            self.curr_player.attackingCells[self.lastRow][self.lastColumn].hit = True
            self.lastRow = -1
        
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
        self.board.your_hits['text'] = "Your Hits: " + str(self.player1_hits)
        self.board.opponent['text'] = "Opponent: " + str(self.player2_hits)
        if (self.curr_player.playerNum == 1):
            self.board.player['text'] = "PLAYER 2S TURN"
        else:
            self.board.player['text'] = "PLAYER 1S TURN"



        print("it is player " + str(self.curr_player.playerNum) + "s turn")
        self.update_cells()


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

    def done_placing_ships_handler(self):
        print("done placing ships button was pushed")
        if self.ships_placed == 5 and self.curr_player == self.player1:
            self.curr_player = self.player2
            self.ships_placed = 0
            self.reset_cells2()
            print("player 1 done")
        elif self.ships_placed == 5 and self.curr_player == self.player2:
            self.curr_player = self.player1
            self.reset_cells2()
            self.board.ship_frame.destroy()
            print("player 2 done")
        print("ships placed"+str(self.ships_placed))

    def carrier_handler(self):
        print("carrier button was pushed")
        self.ship_to_place = True
        self.ship = carrier()
    def battleship_handler(self):
        print("battleship button was pushed")
        self.ship_to_place = True
        self.ship = battleship()
    def submarine_handler(self):
        print("submarine button was pushed")
        self.ship_to_place = True
        self.ship = submarine()
    def cruiser_handler(self):
        print("cruiser button was pushed")
        self.ship_to_place = True
        self.ship = cruiser()
    def destroyer_handler(self):
        print("destroyer button was pushed")
        self.ship_to_place = True
        self.ship = destroyer()

    def reset_cells2(self):
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                self.board.cells2[r][c].configure(bg="blue")   

    def update_cells(self):
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                if (self.curr_player.attackingCells[r][c].ship == True and self.curr_player.attackingCells[r][c].hit == True):
                    self.board.cells[r][c].configure(bg="red")
                elif (self.curr_player.attackingCells[r][c].hit == True):
                    self.board.cells[r][c].configure(bg="grey")
                else:
                    self.board.cells[r][c].configure(bg="blue")

                if (self.curr_player.shipCells[r][c].ship == True):
                    self.board.cells2[r][c].configure(bg="black")  
                else:
                    self.board.cells2[r][c].configure(bg="blue")

                if (self.curr_player.shipCells[r][c].ship == True):
                    self.board.cells2[r][c].configure(bg="grey")
                else:
                    self.board.cells2[r][c].configure(bg="blue")         


    def human_handler(self):
        """ Start (or restart) simulation by scheduling the next step. """
        self.player2 = humanPlayer(2, 0, False)
        self.other_player = self.player2
        print("human button pressed")
        self.board1.window.destroy()
        self.board_setup()
            
    def ai_handler(self):
        """ Pause simulation """
        self.player2 = computerPlayer(2, 0, False)
        self.other_player = self.player2
        print("ai button pressed")
        self.board1.window.destroy()
        self.board_setup()

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

        ai_button = tk.Button(self.control_frame, text="Human vs AI", font=("Helvetica", 10))
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

        # players and their hits
        self.player1_hits = 0
        self.player2_hits = 0

        # GRID ONE: Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(self.window, height = num_rows * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.grid_frame.grid(row = 1, column = 1, padx=40, pady=40)
        self.cells = self.add_cells()

        # GRID 2: Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(self.window, height = num_rows * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.grid_frame.grid(row = 2, column = 1, padx=40, pady=40)
        self.cells2 = self.add_cells()

        # GRID 2: Create frame for grid of cells, and put cells in the frame
        self.ship_frame = tk.Frame(self.window, height = num_cols * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.ship_frame.grid(row = 2, column = 2, padx=40, pady=40)
        (self.done_placing_ships, self.carrier, self.battleship, self.submarine, self.cruiser, self.destroyer) = self.ship_buttons()

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

        carrier = tk.Button(self.ship_frame, text="Carrier (5 cells)", font=("Helvetica", 10))
        carrier.grid(row=2, column=1)

        battleship = tk.Button(self.ship_frame, text="Battleship (4 cells)", font=("Helvetica", 10))
        battleship.grid(row=3, column=1)

        submarine = tk.Button(self.ship_frame, text="Submarine (3 cells)", font=("Helvetica", 10))
        submarine.grid(row=4, column = 1)

        cruiser = tk.Button(self.ship_frame, text="Cruiser (3 cells)", font=("Helvetica", 10))
        cruiser.grid(row=5, column = 1)

        destroyer = tk.Button(self.ship_frame, text="Destroyer (2 cells)", font=("Helvetica", 10))
        destroyer.grid(row=6, column = 1)

        return (done_placing_ships, carrier, battleship, submarine, cruiser, destroyer)

    def set_done_placing_ships_handler(self, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.done_placing_ships.configure(command = handler)

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

        your_hits = tk.Label(self.control_frame, text="Your Hits: " + str(self.player1_hits), font=("Helvetica", 10))
        your_hits.grid(row=4)

        opponent = tk.Label(self.control_frame, text="Opponent: " + str(self.player2_hits), font=("Helvetica", 10))
        opponent.grid(row=5)

        player = tk.Label(self.control_frame, text="PLAYER 1S TURN", font=("Helvetica", 20))
        player.grid(row=6)

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

