"""
Authors:
Aidan Rooney
Alizea Hinz
Gabe Krishnadasan
Marissa Esteban

Description:
Gameboard

"""

import tkinter as tk
from enum import IntEnum

class Control:
    """ The controller. """
    def __init__(self):
        """ Initializes the game of life """
        # Define parameters
        self.NUM_ROWS = 10
        self.NUM_COLS = 10

        # Create view
        self.board = Gameboard(self.NUM_ROWS, self.NUM_COLS)

        self.board.set_battleship_handler(self.battleship_handler)
        self.board.set_carrier_handler(self.carrier_handler)
        self.board.set_submarine_handler(self.submarine_handler)
        self.board.set_cruiser_handler(self.cruiser_handler)
        self.board.set_destroyer_handler(self.destroyer_handler)
        
        # Start the simulation
        self.board.window.mainloop()

        

    def carrier_handler(self):
        print("carrier button was pushed")
    def battleship_handler(self):
        print("battleship button was pushed")
    def submarine_handler(self):
        print("submarine button was pushed")
    def cruiser_handler(self):
        print("cruiser button was pushed")
    def destroyer_handler(self):
        print("destroyer button was pushed")

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
        self.grid_frame.grid(row = 1, column = 1, padx=40, pady=40)
        self.cells = self.add_cells()

        # GRID 2: Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(self.window, height = num_rows * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.grid_frame.grid(row = 2, column = 1, padx=40, pady=40)
        self.cells = self.add_cells()

        # GRID 2: Create frame for grid of cells, and put cells in the frame
        self.ship_frame = tk.Frame(self.window, height = num_cols * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.ship_frame.grid(row = 2, column = 2, padx=40, pady=40)
        (self.carrier, self.battleship, self.submarine, self.cruiser, self.destroyer) = self.ship_buttons()

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = num_cols * self.CELL_SIZE, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 1, column = 2, padx=40, pady=40)
        (self.start_button, self.quit_button, self.label1,
            self.confirm_button, self.your_hits, self.opponent) = self.add_control()

    
    def ship_buttons(self):
        """ 
        Create buttons to choose ship
        """
        carrier = tk.Button(self.ship_frame, text="Carrier (5 cells)", font=("Helvetica", 10))
        carrier.grid(row=1, column=1)

        battleship = tk.Button(self.ship_frame, text="Battleship (4 cells)", font=("Helvetica", 10))
        battleship.grid(row=2, column=1)

        submarine = tk.Button(self.ship_frame, text="Submarine (3 cells)", font=("Helvetica", 10))
        submarine.grid(row=3, column = 1)

        cruiser = tk.Button(self.ship_frame, text="Cruiser (3 cells)", font=("Helvetica", 10))
        cruiser.grid(row=4, column = 1)

        destroyer = tk.Button(self.ship_frame, text="Destroyer (2 cells)", font=("Helvetica", 10))
        destroyer.grid(row=5, column = 1)

        return (carrier, battleship, submarine, cruiser, destroyer)

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

        quit_button = tk.Button(self.control_frame, text="Quit", font=("Helvetica", 10))
        quit_button.grid(row=1, column=2)

        label1 = tk.Label(self.control_frame, text="Welcome to Battleship", font=("Helvetica", 20))
        label1.grid(row=2)

        confirm_button = tk.Button(self.control_frame, text="Confirm Hit", font=("Helvetica", 20))
        confirm_button.grid(row=3)

        your_hits = tk.Label(self.control_frame, text="Your Hits: ", font=("Helvetica", 10))
        your_hits.grid(row=4)

        opponent = tk.Label(self.control_frame, text="Opponent: ", font=("Helvetica", 10))
        opponent.grid(row=5)

        return (start_button, quit_button, label1, confirm_button, your_hits, opponent)


    def add_cells(self):
        """ Add cells to the view """
        cells = []
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                frame = tk.Frame(self.grid_frame, width = self.CELL_SIZE, 
                        height = self.CELL_SIZE, borderwidth = 1, 
                        relief = "solid")
                frame.grid(row = r, column = c)
                row.append(frame)
            cells.append(row)
        return cells


if __name__ == "__main__":
    game_of_life = Control()

