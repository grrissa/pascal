"""
Description: Class to create GUI gameboard
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

import tkinter as tk
class Gameboard:
    def __init__(self, num_rows:int, num_cols:int)->None:
        """ 
        Initialize the GUI gameboard
        """
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

        # GRID 3: Create frame for grid of cells, and put cells in the frame
        self.ship_frame = tk.Frame(self.window, height = num_cols * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.ship_frame.grid(row = 2, column = 2, padx=40, pady=40)
        (self.delete_ship, self.done_placing_ships, self.carrier, self.battleship, self.submarine, self.cruiser, self.destroyer, self.place_random_ships) = self.ship_buttons()

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = num_cols * self.CELL_SIZE, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 1, column = 2, padx=40, pady=40)
        (self.quit_button, self.label1,
            self.confirm_button, self.your_hits, self.opponent, self.player, self.shipSinkNotification) = self.add_control()

        self.switch_frame = tk.Frame(self.window, relief = "solid", background = "black")
        self.switch_frame.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, sticky = "news")
        self.window.grid_columnconfigure(0, weight=1)
        self.switch_players = self.player_switch()

    def player_switch(self)->object:
        """
        Function that handles the switch between players
        """
        switch_players = tk.Button(self.switch_frame, text = "Ready to Switch Players", font=("Helvetica", 20), bg= "blue" , fg = "blue")
        switch_players.pack()
        return switch_players

    def set_switch_players_handler(self, handler)->None:
        """ 
        Set handler for clicking on reset button to the function handler 
        """
        self.switch_players.configure(command = handler)
    
    def ship_buttons(self)->tuple:
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

        random_ships = tk.Button(self.ship_frame, text="Place Random Ships", font=("Helvetica", 15))
        random_ships.grid(row=8, column = 1)

        return (delete_ship, done_placing_ships, carrier, battleship, submarine, cruiser, destroyer, random_ships)

    def set_done_placing_ships_handler(self, handler)->None:
        """ 
        Set handler for clicking on cell in row, column to the function handler
        """
        self.done_placing_ships.configure(command = handler)
    
    def set_random_ships_handler(self, handler)->None:
        """
        Set handler for clicking on cell in row, column to the function handler 
        """
        self.place_random_ships.configure(command = handler)

    def set_delete_ship_handler(self, handler)->None:
        """ 
        Set handler for clicking on cell in row, column to the function handler 
        """
        self.delete_ship.configure(command = handler)

    def set_carrier_handler(self, handler)->None:
        """ 
        Set handler for clicking on cell in row, column to the function handler 
        """
        self.carrier.configure(command = handler)

    def set_battleship_handler(self, handler)->None:
        """ 
        Set handler for clicking on start button to the function handler 
        """
        self.battleship.configure(command = handler)

    def set_submarine_handler(self, handler)->None:
        """ 
        Set handler for clicking on pause button to the function handler 
        """
        self.submarine.configure(command = handler)

    def set_cruiser_handler(self, handler)->None:
        """ 
        Set handler for clicking on step button to the function handler 
        """
        self.cruiser.configure(command = handler)

    def set_destroyer_handler(self, handler)->None:
        """ 
        Set handler for clicking on reset button to the function handler 
        """
        self.destroyer.configure(command = handler)

    def add_control(self)->tuple:
        """ 
        Create control buttons and welcome message, and add them to the control frame 
        """
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

        shipSinkNotification = tk.Label(self.control_frame, text="", font=("Helvetica", 20))
        shipSinkNotification.grid(row=8)

        return (quit_button, label1, confirm_button, your_hits, opponent, player, shipSinkNotification)

    def add_cells(self)->list:
        """ 
        Add cells to the view 
        """
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

    def set_cell_click_handler_top(self, row:int, column:int, handler)->None:
        """ 
        Set handler for clicking on cell in row, column to the function handler 
        """
        self.cells[row][column].bind('<Button-1>', handler)

    def set_cell_click_handler_bottom(self, row:int, column:int, handler)->None:
        """ 
        Set handler for clicking on cell in row, column to the function handler 
        """
        self.cells2[row][column].bind('<Button-1>', handler)

    def set_confirm_hit_handler(self, handler)->None:
        """
        Set handler for clicking the confirm hit button on the gameboard
        """
        self.confirm_button.bind('<Button-1>', handler)

    def quit(self)->None:
        """ 
        Functionality for quit button 
        """
        self.window.destroy()