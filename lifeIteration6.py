"""
Module: lifeIteration6

Author:
John Glick
Department of Computer Science
University of San Diego

Description:
A Python implementation of Conway's game of life, using Tkinter, and implemented
using the model-view-controller design pattern.

Iteration 6: 

Final iteration of the life program.  This last iteration implements the event
handler functions in the controller (the Life class) that were created
as stub functions in iteration 4.
"""

import tkinter as tk
from enum import IntEnum
import unittest

class Life:
    """ The controller. """
    def __init__(self):
        """ Initializes the game of life """
        # Define parameters
        self.NUM_ROWS = 30
        self.NUM_COLS = 30
        self.DEFAULT_STEP_TIME_MILLIS = 1000

        # Create model
        self.model = LifeModel(self.NUM_ROWS, self.NUM_COLS)

        # Create view
        self.view = LifeView(self.NUM_ROWS, self.NUM_COLS)

        # Set up step time
        self.step_time_millis = self.DEFAULT_STEP_TIME_MILLIS

        # Set up the control
        
        # Start
        self.view.set_start_handler(self.start_handler)
        self.is_running = False
        
        # Pause
        self.view.set_pause_handler(self.pause_handler)

        # Step
        self.view.set_step_handler(self.step_handler)

        # Reset 
        self.view.set_reset_handler(self.reset_handler)

        # Quit
        self.view.set_quit_handler(self.quit_handler)

        # Step speed
        self.view.set_step_speed_handler(self.step_speed_handler)

        # Cell clicks.  (Note that a separate handler function is defined for 
        # each cell.)
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                def handler(event, row = r, column = c):
                    self.cell_click_handler(row, column)
                self.view.set_cell_click_handler(r, c, handler)

        # Start the simulation
        self.view.window.mainloop()

    def start_handler(self):
        """ Start (or restart) simulation by scheduling the next step. """
        if not self.is_running:
            self.is_running = True
            self.view.schedule_next_step(self.step_time_millis, 
                                        self.continue_simulation)
        
    def pause_handler(self):
        """ Pause simulation """
        if self.is_running:
            self.view.cancel_next_step()
            self.is_running = False
        
    def step_handler(self):
        """ Perform one step of simulation """
        if not self.is_running:
            self.one_step()

    def reset_handler(self):
        """ Reset simulation """
        self.pause_handler()
        self.reset()

    def quit_handler(self):
        """ Quit life program """
        self.view.window.destroy()

    def step_speed_handler(self, value):
        """ Adjust simulation speed"""
        self.step_time_millis = self.DEFAULT_STEP_TIME_MILLIS // int(value)
                
    def cell_click_handler(self, row, column):
        """ Cell click """
        if self.model.is_alive(row, column):
            self.model.make_dead(row, column)
            self.view.make_dead(row, column)
        else:
            self.model.make_alive(row, column)
            self.view.make_alive(row, column)

    def reset(self):
        """ Reset the game (all cells dead) """
        self.model.reset()
        self.view.reset()

    def continue_simulation(self):
        """ Perform another step of the simulation, and schedule
            the next step.
        """
        self.one_step()
        self.view.schedule_next_step(self.step_time_millis, self.continue_simulation)

    def one_step(self):
        """ Simulate one step """
        # Update the model
        self.model.one_step()

        # Update the view
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if self.model.is_alive(row, col):
                    self.view.make_alive(row, col)
                else:
                    self.view.make_dead(row, col)
        
class LifeView:
    """ The view """

    def __init__(self, num_rows, num_cols):
        """ Initialize view of the game """
        # Constants
        self.CELL_SIZE = 20
        self.CONTROL_FRAME_HEIGHT = 100

        # Size of grid
        self.num_rows = num_rows
        self.num_cols = num_cols

        # Create window
        self.window = tk.Tk()
        self.window.title("Game of Life")

        # Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(self.window, height = num_rows * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.grid_frame.grid(row = 1, column = 1)
        self.cells = self.add_cells()

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = num_cols * self.CELL_SIZE, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 2, column = 1)
        self.control_frame.grid_propagate(False)
        (self.start_button, self.pause_button, 
         self.step_button, self.step_speed_slider, 
         self.reset_button, self.quit_button) = self.add_control()            

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

    def add_control(self):
        """ 
        Create control buttons and slider, and add them to the control frame 
        """
        start_button = tk.Button(self.control_frame, text="Start")
        start_button.grid(row=1, column=1)
        pause_button = tk.Button(self.control_frame, text="Pause")
        pause_button.grid(row=1, column=2)
        step_button = tk.Button(self.control_frame, text="Step")
        step_button.grid(row=1, column=3)
        step_speed_slider = tk.Scale(self.control_frame, from_=1, to=10, 
                    label="Step Speed", showvalue=0, orient=tk.HORIZONTAL)
        step_speed_slider.grid(row=1, column=4)
        reset_button = tk.Button(self.control_frame, text="Reset")
        reset_button.grid(row=1, column=5)
        quit_button = tk.Button(self.control_frame, text="Quit")
        quit_button.grid(row=1, column=6)

        # Vertically center the controls in the control frame
        self.control_frame.grid_rowconfigure(1, weight = 1) 

        # Horizontally center the controls in the control frame
        self.control_frame.grid_columnconfigure(0, weight = 1) 
        self.control_frame.grid_columnconfigure(7, weight = 1) 
                                                            
        return (start_button, pause_button, step_button, step_speed_slider, 
                reset_button, quit_button)

    def set_cell_click_handler(self, row, column, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.cells[row][column].bind('<Button-1>', handler)

    def set_start_handler(self, handler):
        """ set handler for clicking on start button to the function handler """
        self.start_button.configure(command = handler)

    def set_pause_handler(self, handler):
        """ set handler for clicking on pause button to the function handler """
        self.pause_button.configure(command = handler)

    def set_step_handler(self, handler):
        """ set handler for clicking on step button to the function handler """
        self.step_button.configure(command = handler)

    def set_reset_handler(self, handler):
        """ set handler for clicking on reset button to the function handler """
        self.reset_button.configure(command = handler)

    def set_quit_handler(self, handler):
        """ set handler for clicking on quit button to the function handler """
        self.quit_button.configure(command = handler)

    def set_step_speed_handler(self, handler):
        """ set handler for dragging the step speed slider to the function handler """
        self.step_speed_slider.configure(command = handler)

    def make_alive(self, row, column):
        """ Make cell in row, column alive """
        self.cells[row][column]['bg'] = 'black'

    def make_dead(self, row, column):
        """ Make cell in row, column dead """
        self.cells[row][column]['bg'] = 'white'

    def reset(self):
        """ reset all cells to dead """
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.make_dead(r, c)

    def schedule_next_step(self, step_time_millis, step_handler):
        """ schedule next step of the simulation """
        self.start_timer_object = self.window.after(step_time_millis, step_handler)

    def cancel_next_step(self):
        """ cancel the scheduled next step of simulation """
        self.window.after_cancel(self.start_timer_object)

class LifeModel:
    """ The model """

    def __init__(self, num_rows, num_cols):
        """ initialize the life model """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.state = [[CellState.DEAD for c in range(self.num_cols)] 
                        for r in range(self.num_rows)]
        # SAME AS
        #self.state = []
        #for _ in range(num_rows):
        #    row = []
        #    for _ in range(num_cols):
        #        row.append(CellState.DEAD)
        #    self.state.append(row)
    
    def make_alive(self, row, col):
        """ Make the cell in row, col alive. """
        self.state[row][col] = CellState.ALIVE

    def make_dead(self, row, col):
        """ Make the cell in row, col dead. """
        self.state[row][col] = CellState.DEAD

    def is_alive(self, row, col):
        """ returns true if the cell in row, col is alive, false otherwise """
        return self.state[row][col] == CellState.ALIVE

    def reset(self):
        """ Resets all cells to dead """
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.make_dead(r, c)

    def one_step(self):
        """ Simulates one time step of simulation """
        # Make array for state in next timestep
        next_state = [[CellState.DEAD for c in range(self.num_cols)] 
                        for r in range(self.num_rows)]
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                num_neighbors = self.neighbor_count(r, c)
                if self.is_alive(r, c):
                    if num_neighbors < 2 or num_neighbors > 3:
                        next_state[r][c] = CellState.DEAD
                    else:
                        next_state[r][c] = CellState.ALIVE
                else:
                    if num_neighbors == 3:
                        next_state[r][c] = CellState.ALIVE
                    else:
                        next_state[r][c] = CellState.DEAD
        self.state = next_state

    def neighbor_count(self, row, col):
        """ Returns count of number of alive neighbors to the cell in row, col """
        num_neighbors = 0
        for del_r in range(-1, 2):
            for del_c in range(-1, 2):
                r = row + del_r
                c = col + del_c
                if ((r >= 0 and r < self.num_rows) and 
                    (c >= 0 and c < self.num_cols) and 
                    (del_r != 0 or del_c != 0)):
                    if self.is_alive(r, c):
                        num_neighbors += 1
        return num_neighbors

class CellState(IntEnum):
    """ 
    Use IntEnum so that the test code below can
    set cell states using 0's and 1's
    """
    DEAD = 0
    ALIVE = 1

class LifeModelTest(unittest.TestCase):
    """ 
    For testing the neighbor_count and one_step methods of the LifeModel class.
    Run test_neighbor_count and test_one_step by typing
    python3 -m unittest lifeIteration5.py 
    from the command line.
    """
    def setUp(self):
        self.model = LifeModel(10, 9)
        self.model.state = [[1, 0, 0, 0, 1, 0, 0, 0, 1],
                            [0, 0, 1, 0, 0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 1, 0],
                            [0, 0, 1, 0, 0, 1, 1, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 1, 1, 1, 0, 0, 1],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 1, 0, 0, 0, 1]]
        self.correct_num_neighbors =  [[0, 2, 1, 2, 0, 2, 1, 2, 0], 
                            [1, 3, 1, 3, 1, 2, 1, 3, 2], 
                            [0, 3, 2, 3, 1, 3, 5, 3, 2], 
                            [0, 2, 1, 2, 1, 1, 3, 2, 2], 
                            [1, 2, 2, 3, 4, 4, 4, 3, 2], 
                            [0, 1, 2, 3, 5, 3, 2, 1, 0], 
                            [1, 1, 3, 5, 8, 5, 3, 1, 1], 
                            [0, 0, 2, 3, 5, 3, 2, 0, 0], 
                            [1, 1, 1, 3, 4, 3, 1, 1, 1], 
                            [0, 1, 0, 1, 0, 1, 0, 1, 0]]   
        self.correct_next_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 1, 0, 0, 0, 1, 0],
                            [0, 1, 1, 1, 0, 1, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 1, 1, 0],
                            [0, 0, 0, 1, 0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 1, 0, 1, 0, 0, 0],
                            [0, 0, 0, 1, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                      

    def test_neighbor_count(self):
        # Test neighbor_count on all cells of the test grid
        for row in range(self.model.num_rows):
            for col in range(self.model.num_cols):
                self.assertEqual(self.model.neighbor_count(row, col), 
                                self.correct_num_neighbors[row][col])

    def test_one_step(self):
        # Test just one step of the life simuation
        self.model.one_step()
        self.assertEqual(self.model.state, self.correct_next_state)

if __name__ == "__main__":
    game_of_life = Life()