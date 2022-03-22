import imp
from turtle import Turtle

class Scoreboard(Turtle):

    # Initial parameters
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.setpos(0, 250)
        self.display_score()

    # Clear the screen and display currecnt score
    def display_score(self):
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", False, align="center", font=("Consolas", 25, "normal"))

    # Checking the score of both players, displaying a message when the needed score is achieved
    def if_gameover(self):
        if self.l_score == 10:
            self.clear()
            self.setpos(0, 0)
            self.write(f"Game over. Player Left won", False, align="center", font=("Consolas", 18, "normal"))
            return True
        if self.r_score == 10:
            self.clear()
            self.setpos(0, 0)
            self.write(f"Game over. Player Right won", False, align="center", font=("Consolas", 18, "normal"))
            return True
        return False