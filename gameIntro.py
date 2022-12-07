import tkinter as tk

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