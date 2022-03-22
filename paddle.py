from turtle import Turtle

class Paddle(Turtle):
    # Initial parameters
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.pu()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setpos(x=pos[0], y=pos[1])
        self.setheading(90)

    # Move a paddle up ro down
    def go_up(self):
        self.forward(20)
    def go_down(self):
        self.backward(20)
