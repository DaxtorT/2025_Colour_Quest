from tkinter import*

class StartGame():
    """
    Colour Quest Game Start Screen
    """

    def __init__(self):
        """
        Start Game GUI
        """

        background = "#f5cba7"
        instructions = ("In each round you will be invited to choose a "
                        "colour. Your goal is to beat the target score and "
                        "win the round (and keep your points)")
        question = "How Many Rounds Do You Want To Play?"

        self.start_frame = Frame(padx=10, pady=10, bg="#f5cba7")
        self.start_frame.grid()

        self.start_heading = Label(self.start_frame,
                                   text="Welcome To Colour Quest!",
                                   font=("Arial", "16", "bold"))
        self.start_heading.grid(row=0, padx=10, pady=10)

        self.start_instruct = Label(self.start_frame,
                                    text=instructions,
                                    wraplength=350, width=40,
                                    font=("Arial", "12"))
        self.start_instruct.grid(row=1, padx=10, pady=10)

        self.start_question = Label(self.start_frame,
                                    text=question,
                                    wraplength=350, width=40,
                                    font=("Arial", "12", "bold"), fg="#009900")
        self.start_question.grid(row=2, padx=5, pady=5)

        self.start_but_frame = Frame(self.start_frame)
        self.start_but_frame.grid(row=3, padx=5, pady=5)

        self.start_round_entry = Entry(self.start_but_frame,
                                       font=("Arial", "20"), width=10)
        self.start_round_entry.grid(row=0, column=0, padx=5, pady=5)

        self.start_round_button = Button(self.start_but_frame,
                                        text="Play", command=self.check_rounds,
                                        bg="#0000cc", fg="#ffffff",
                                        font=("Arial", "14", "bold"), width=10)
        self.start_round_button.grid(row=0, column=1, padx=5, pady=5)

        # List and loop to set the background colour on everything except the buttons
        recolour_list = [self.start_frame, self.start_but_frame, self.start_heading, self.start_instruct, self.start_question]

        for item in recolour_list:
            item.config(bg=background)

    def check_rounds(self):
        """
        Checks whether users input for rounds is valid
        """
        # Retrieve temperature to be converted
        rounds_wanted = self.start_round_entry.get()

        # Reset label and entry box (for when users come back to home screen)
        self.start_question.config(fg="#009900", font=("Arial", "12", "bold"), wraplength=350)
        self.start_round_entry.config(bg="#ffffff")

        error = "Oops - Please choose a whole number more than zero."
        has_errors = "no"

        # Checks that amount to be converted is a number above absolute zero
        try:
            rounds_wanted = int(rounds_wanted)
            if rounds_wanted > 0:
                # Invoke Play Class (and take across number of rounds)
                Play(rounds_wanted)
                # Hide Root Window (ie: hide rounds choice window)
                root.withdraw()
            else:
                has_errors == "yes"

        except ValueError:
            has_errors = "yes"

        # Display the error if necessary
        if has_errors == "yes":
            self.start_question.config(text=error, fg="#990000",
                                       font=("Arial", "10", "bold"), wraplength=200)
            self.start_round_entry.config(bg="#f4cccc")
            self.start_round_entry.delete(0, END)


class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self, how_many):
        # Preset some values temporarily
        colour_name = "Blue"
        score_to_beat = 20
        score = 20

        # Constants for the play class
        small_font = ("Arial", "11")
        med_font = ("Arial", "12", "bold")
        large_font = ("Arial", "14", "bold")
        choice_text = f"You chose {colour_name} - your score is {score}\n" \
                      f"Well Done, you have won this round."
        white = "#ffffff"
        gray = "#cccccc"

        # Start of GUI Creation
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        # Row 3 - Colour Buttons Frame
        self.colour_frame = Frame(self.game_frame)
        self.colour_frame.grid(row=3, padx=10, pady=5)

        # Row 6 - Hint & Stats Button Frame
        self.hints_stats_frame = Frame(self.game_frame)
        self.hints_stats_frame.grid(row=6, padx=10, pady=5)

        # List for holding label details (Text | Font | BG Colour | Row | Width | Border Size | Border | Wrap Length)
        play_labels_list = [
            [f"Round 0 of {how_many}", ("Arial", "16", "bold"), None, 0, 30, 0, None, None],
            [f"Score to Beat: {score_to_beat}", small_font, "#fff2cc", 1, 30, 1, "solid", None],
            ["Choose a Colour below. Good Luck", small_font, "#d5e8d4", 2, 30, 1, "solid", 175],
            [choice_text, small_font, "#d5e8d4", 4, 30, 1, "solid", 350, 5, None]
        ]

        # List to hold labels once they have been made
        self.labels_ref_list = []

        # Loop through every item in label list to make label
        for item in play_labels_list:
            self.make_label = Label(self.game_frame, text=item[0], font=item[1], bg=item[2], 
                                      width=item[4], border=item[5], relief=item[6], wraplength=item[7])
            self.make_label.grid(row=item[3], padx=5, pady=5)
            self.labels_ref_list.append(self.make_label)

        # Make variables for labels that need editing later
        self.game_heading = self.labels_ref_list[0]

        self.score_to_beat = self.labels_ref_list[1]

        # List for holding button details (Text | Frame Location | Command | Font | FG Colour | BG Colour | Row | Column | Width)
        play_buttons_list = [
            ["Colour A", self.colour_frame, "", med_font, None, gray, 0, 0, 12],
            ["Colour B", self.colour_frame, "", med_font, None, gray, 0, 1, 12],
            ["Colour C", self.colour_frame, "", med_font, None, gray, 1, 0, 12],
            ["Colour D", self.colour_frame, "", med_font, None, gray, 1, 1, 12],
            ["Next Round", self.game_frame, "", large_font, white, "#0057d8", 5, None, 22],
            ["Hints", self.hints_stats_frame, "", large_font, white, "#ff8000", 0, 0, 10],
            ["Stats", self.hints_stats_frame, "", large_font, white, "#333333", 0, 1, 10],
            ["End Game", self.game_frame, self.close_play, large_font, white, "#990000", 7, None, 22]
        ]
        disabled_list = [0, 1, 2, 3, 6]

        # List to hold buttons once they have been made
        self.buttons_ref_list = []

        # Loop through every item in button list to make button
        for item in play_buttons_list:
            self.make_button = Button(item[1], command=item[2], text=item[0], font=item[3],
                                      fg=item[4], bg=item[5], width=item[8])
            self.make_button.grid(row=item[6], column=item[7], padx=5, pady=5)
            if item in disabled_list:
                self.make_button.config(state=DISABLED)
            self.buttons_ref_list.append(self.make_button)

        # Make variables for buttons that need editing later
        self.colour_button_a = self.buttons_ref_list[0]
        self.colour_button_b = self.buttons_ref_list[1]
        self.colour_button_c = self.buttons_ref_list[2]
        self.colour_button_d = self.buttons_ref_list[3]

        self.hints_button = self.buttons_ref_list[5]
        self.stats_button = self.buttons_ref_list[6]

    def close_play(self):
        # Reshow root (Choose Rounds window) and end current game / allow new game to start
        root.deiconify()
        self.play_box.destroy()

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()