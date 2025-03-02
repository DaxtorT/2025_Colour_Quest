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
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.game_heading = Label(self.game_frame, text=f"Round 0 of {how_many}",
                                  font=("Arial", "16", "bold"))
        self.game_heading.grid(row=0)

        

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()