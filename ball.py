from turtle import Turtle

class Ball(Turtle):
    # Initial parameters
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.pu()
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.setheading(40)
        self.direction = "right"
        self.speed = 2
    # Moving the ball
    def move_ball(self):
        self.forward(self.speed)