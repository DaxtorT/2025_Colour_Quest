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

        self.start_frame = Frame(padx=10, pady=10, bg="#f5cba7")
        self.start_frame.grid()

        self.start_heading = Label(self.start_frame,
                                   text="Welcome To Colour Quest!",
                                   font=("Arial", "16", "bold"))
        self.start_heading.grid(row=0, padx=10, pady=10)

        instructions = ("In each round you will be invited to choose a "
                        "colour. Your goal is to beat the target score and "
                        "win the round (and keep your points)")

        self.start_instruct = Label(self.start_frame,
                                    text=instructions,
                                    wraplength=350, width=40,
                                    font=("Arial", "12"))
        self.start_instruct.grid(row=1, padx=10, pady=10)

        question = "How Many Rounds Do You Want To Play?"

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
        score = 20

        # Start of GUI Creation
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        # Row 0 - Round Number Label
        self.game_heading = Label(self.game_frame, text=f"Round 0 of {how_many}",
                                  font=("Arial", "16", "bold"))
        self.game_heading.grid(row=0)

        # Row 1 - Score to Beat Label
        self.score_to_beat = Label(self.game_frame, text=f"Score to Beat: #",
                                   font=("Arial", "11"), bg="#fff2cc",
                                   width=30, border=1, relief="solid")
        self.score_to_beat.grid(row=1, pady=1)

        # Row 2 - Choose Colour Instruction Label
        self.choose_label = Label(self.game_frame, text="Choose a colour below. Good Luck",
                                  font=("Arial", "11"), bg="#d5e8d4",
                                  width=30, wraplength=175,
                                  border=1, relief="solid")
        self.choose_label.grid(row=2, pady=1)

        # Row 3 - Colour Buttons Frame
        self.colour_frame = Frame(self.game_frame)
        self.colour_frame.grid(row=3, padx=10, pady=5)

        # Colours List (Colour Text | BG Colour | Command | Row | Column)
        colours_detail_list = [
            ["Colour A", "#cccccc", "", 0, 0],
            ["Colour B", "#cccccc", "", 0, 1],
            ["Colour C", "#cccccc", "", 1, 0],
            ["Colour D", "#cccccc", "", 1, 1]
        ]

        # List to hold buttons once they have been made
        self.colours_ref_list = []

        for item in colours_detail_list:
            self.make_button = Button(self.colour_frame,
                                      text=item[0], bg=item[1],
                                      fg="#ffffff", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.make_button.config(state=DISABLED)
            self.colours_ref_list.append(self.make_button)

        choice_text = f"You chose {colour_name} - your score is {score}\n" \
                      f"Well Done, you have won this round."

        # Row 4 - Colour Choice Label
        self.choice_label = Label(self.game_frame, text=choice_text,
                                  font=("Arial", "11"), bg="#d5e8d4",
                                  width=30, wraplength=350,
                                  border=1, relief="solid")
        self.choice_label.grid(row=4, pady=5)

        # Row 5 - Next Round Button
        self.round_button = Button(self.game_frame, text="Next Round",
                                  font=("Arial", "14", "bold"), width=22,
                                  fg="#ffffff", bg="#0057d8", command="")
        self.round_button.grid(row=5, pady=1)

        # Row 6 - Hint & Stats Button Frame
        self.hints_stats_frame = Frame(self.game_frame)
        self.hints_stats_frame.grid(row=6, padx=10, pady=5)

        # Hints and Stats Buttons
        self.hints_button = Button(self.hints_stats_frame, text="Hints",
                                  font=("Arial", "14", "bold"), width=10,
                                  fg="#ffffff", bg="#ff8000", command="")
        self.hints_button.grid(row=0, column=0, padx=7)
        self.hints_button.config(state=DISABLED)

        self.stats_button = Button(self.hints_stats_frame, text="Stats",
                                  font=("Arial", "14", "bold"), width=10,
                                  fg="#ffffff", bg="#333333", command="")
        self.stats_button.grid(row=0, column=1, padx=7)
        self.stats_button.config(state=DISABLED)

        # Row 7 - End Game Button
        self.end_game_button = Button(self.game_frame, text="End Game",
                                      font=("Arial", "14", "bold"),
                                      fg="#ffffff", bg="#990000", width=22,
                                      command=self.close_play)
        self.end_game_button.grid(row=7)

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