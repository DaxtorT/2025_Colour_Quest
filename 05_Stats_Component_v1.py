from tkinter import*
from functools import partial

# 3:33 On Video 24

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
        self.rounds_won = IntVar()

        # Lists for stats component

        # Highest Score Test Data...
        # self.all_scores_list = [20, 20, 20, 16, 19]
        # self.all_high_score_list = [20, 20, 20, 16, 19]
        # self.rounds_won.set(5)

        # Lowest Score Test Data
        # self.all_scores_list = [0, 0, 0, 0, 0]
        # self.all_high_score_list = [20, 20, 20, 16, 19]
        # self.rounds_won.set(0)

        # Random Score Test Data
        self.all_scores_list = [16, 16, 0, 0, 20]
        self.all_high_score_list = [16, 16, 19, 19, 20]
        self.rounds_won.set(3)

        # GUI Code
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.game_heading = Label(self.game_frame, text=f"Round 0 of {how_many}",
                                  font=("Arial", "16", "bold"))
        self.game_heading.grid(row=0) 

        self.stats_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                   text="Stats", width=15, fg="#ffffff",
                                   bg="#0080ff", padx=10, pady=10, command=self.to_stats)
        self.stats_button.grid(row=1)

    def to_stats(self):
        """
        Retrieves everything we need to display the game / round statistics
        """
        # IMPORTANT: Retrieve # of rounds won as a number
        rounds_won = self.rounds_won.get()
        stats_bundle = [rounds_won, self.all_scores_list, self.all_high_score_list]

        DisplayStats(self, stats_bundle)


class DisplayStats():
    """
    Displays stats for Colour Quest Game
    """

    def __init__(self, partner, all_stats_info):
        # Extract information from master list...
        rounds_won = all_stats_info[0]
        user_scores = all_stats_info[1]
        high_scores = all_stats_info[2]

        # Sort user scores to find high score...
        user_scores.sort()

        background = "#cce6ff"

        # Makes new window seperate to main converter window
        self.stats_box = Toplevel()

        # Disable stats button when already open
        partner.stats_button.config(state=DISABLED)

        # If users press cross at top, closes stats and 'releases' stats button
        self.stats_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_stats, partner))

        self.stats_frame = Frame(self.stats_box, width=300, bg=background)
        self.stats_frame.grid()

        # Maths to populate Stats dialogue...
        rounds_played = len(user_scores)

        success_rate = rounds_won / rounds_played * 100
        total_score = sum(user_scores)
        max_possible = sum(high_scores)

        best_score = user_scores[-1]
        average_score = total_score / rounds_played

        # All label Strings
        success_string = f"Success Rate: {rounds_won} / {rounds_played} ({success_rate:.2f}%)"

        total_score_string = f"Total Score: {total_score}"
        max_possible_string = f"Maximum Possible Score: {max_possible}"
        best_score_string = f"Best Score: {best_score}"

        # Custom Comment text and formatting
        if total_score == max_possible:
            comment_string = "Amazing! You got the Highest Possible Score!"
            comment_colour = "#d5e8d4"
        elif total_score == 0:
            comment_string = "Oops - You've lost every round! You might want to look at the hints!"
            comment_colour = "#f8cecc"
            best_score_string = f"Best Score: n/a"
        else:
            comment_string = ""
            comment_colour = background

        average_score_string = f"Average Score: {average_score:.0f}"

        heading_font = ("Arial", "16", "bold")
        normal_font = ("Arial", "14")
        comment_font = ("Arial", "13")

        # Label List (text | font | 'Sticky')
        all_stats_strings = [
            ["Statistics", heading_font, ""],
            [success_string, normal_font, "W"],
            [total_score_string, normal_font, "W"],
            [max_possible_string, normal_font, "W"],
            [comment_string, comment_font, "W"],
            ["\nRounds Stats", heading_font, ""],
            [best_score_string, normal_font, "W"],
            [average_score_string, normal_font, "W"],
        ]

        # List to hold labels once they have been made
        stats_labels_ref_list = []

        # Loop through every item in label list to make label
        for count, item in enumerate(all_stats_strings):
            self.make_stats_label = Label(self.stats_frame, text=item[0], font=item[1],
                                     anchor="w", justify="left", padx=30, pady=5, bg=background)
            self.make_stats_label.grid(row=count, sticky=item[2], padx=10)
            stats_labels_ref_list.append(self.make_stats_label)

        # Configure comment label backgropund (for all won / all lost)
        self.stats_comment_label = stats_labels_ref_list[4]
        self.stats_comment_label.config(fg=comment_colour)

        self.dismiss_button = Button(self.stats_frame,
                                     font=("Arial", "16", "bold"),
                                     text="Dismiss", bg="#cc6600",
                                     fg="#ffffff", width=20,
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=8, padx=10, pady=10)

    def close_stats(self, partner):
        """
        Closes stats dialogue box (and enables stats button)
        """
        # Put stats button back to normal
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()