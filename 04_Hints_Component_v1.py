from tkinter import*
from functools import partial

class StartGame():
    """
    Colour Quest Game Start Screen
    """

    def __init__(self):
        """
        Start Game GUI
        """

        background = "#f5cba7"

        self.start_frame = Frame(padx=10, pady=10, bg="#f5cba7")
        self.start_frame.grid()

        self.start_heading = Label(self.start_frame,
                                   text="Welcome To Colour Quest!",
                                   font=("Arial", "16", "bold"))
        self.start_heading.grid(row=0, padx=10, pady=10)

        self.start_round_button = Button(self.start_frame,
                                        text="Play", command=self.check_rounds,
                                        bg="#ff8000", fg="#ffffff",
                                        font=("Arial", "14", "bold"), width=10)
        self.start_round_button.grid(row=1, padx=5, pady=5)

        # List and loop to set the background colour on everything except the buttons
        recolour_list = [self.start_frame, self.start_heading]

        for item in recolour_list:
            item.config(bg=background)

    def check_rounds(self):
        """
        Checks whether users input for rounds is vali           d
        """
        
        rounds_wanted = 5
        # Invoke Play Class (and take across number of rounds)
        Play(rounds_wanted)
        # Hide Root Window (ie: hide rounds choice window)
        root.withdraw()


class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.game_heading = Label(self.game_frame, text=f"Round 0 of {how_many}",
                                  font=("Arial", "16", "bold"))
        self.game_heading.grid(row=0) 

        self.hints_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                   text="Hints", width=15, fg="#ffffff",
                                   bg="#ff8000", padx=10, pady=10, command=self.to_hints)
        self.hints_button.grid(row=1)

    def to_hints(self):
        """
        Displays hints for playing game
        """
        DisplayHints(self)


class DisplayHints():

    def __init__(self, partner):
        # Setup dialogue box and background colour
        background = "#ffe6cc"
        hints_text = "The score for each colour relates to it's hexadecimal code. \n\n" \
                    "Remember, the hex code for white is #FFFFFF - which is the best " \
                    "possible score \n\n" \
                    "The hex code for black is #000000 which is the worst possible " \
                    "score. \n\n" \
                    "The first colour in the code is red, so if you had to choose " \
                    "between red (#FF0000), green (#00FF00) and blue (#0000FF), then " \
                    "red would be the best choice. \n\n" \
                    "Good Luck!"

        # Makes new window seperate to main converter window
        self.hints_box = Toplevel()

        # Disable hints button when already open
        partner.hints_button.config(state=DISABLED)

        # If users press cross at top, closes hints and 'releases' hints button
        self.hints_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_hints, partner))

        self.hints_frame = Frame(self.hints_box,
                                width=300, height=200)
        self.hints_frame.grid()

        self.hints_heading_label = Label(self.hints_frame,
                                        text="Hints",
                                        font=( "Arial", "14", "bold"))
        self.hints_heading_label.grid(row=0)

        self.hints_text_label = Label(self.hints_frame,
                                     text=hints_text, wraplength=350,
                                     justify="left")
        self.hints_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.hints_frame,
                                     font=("Arial", "14", "bold"),
                                     text="Dismiss", 
                                     bg="#cc6600", fg="#ffffff", 
                                     command=partial(self.close_hints, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)


        # List and loop to set the background colour on everything except the buttons
        recolour_list = [self.hints_frame, self.hints_heading_label, self.hints_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_hints(self, partner):
        """
        Closes hints dialogue box (and enables hints button)
        """
        # Put hints button back to normal
        partner.hints_button.config(state=NORMAL)
        self.hints_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()