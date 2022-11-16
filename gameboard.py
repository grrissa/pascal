"""
Description: Class to create GUI gameboard
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

import tkinter as tk
#import humanPlayer, player
from enum import IntEnum

class Control:
    """ The controller. """
    def __init__(self):
        """ Initializes the game of life """
        # Define parameters
        self.NUM_ROWS = 10
        self.NUM_COLS = 10

        # Create view
        self.board1 = GameIntro()

        self.board1.set_human_handler(self.human_handler)
        self.board1.set_ai_handler(self.ai_handler)

        #self.player1 = humanPlayer(0, True)

        # Start the simulation
        self.board1.window.mainloop()

    def cell_click_handler(self, row, column):
        """ Cell click """
        print("Cell click: row = %d col = %d" % (row, column))

    def board_setup(self):
        # Cell clicks.  (Note that a separate handler function is defined for 
        # each cell.)
        self.board = Gameboard(self.NUM_ROWS, self.NUM_COLS)
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                def handler(event, row = r, column = c):
                    self.cell_click_handler(row, column)
                self.board.set_cell_click_handler(r, c, handler)

        self.board.window.mainloop()

    def human_handler(self):
        """ Start (or restart) simulation by scheduling the next step. """
        #self.player2 = humanPlayer(0, False)
        print("human button pressed")
        self.board1.window.destroy()
        self.board_setup()
            
    def ai_handler(self):
        """ Pause simulation """
        #self.player2 = computerPlayer(0, False)
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

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = num_cols * self.CELL_SIZE, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 1, column = 2, padx=40, pady=40)
        (self.start_button, self.quit_button, self.label1,
            self.confirm_button, self.your_hits, self.opponent) = self.add_control()

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

    def set_cell_click_handler(self, row, column, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.cells[row][column].bind('<Button-1>', handler)
        self.cells2[row][column].bind('<Button-1>', handler)

    def quit(self):
        """ Functionality for quit button """
        self.window.destroy()

if __name__ == "__main__":
    game_of_life = Control()

