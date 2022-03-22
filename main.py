from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong")
screen.tracer(0)

# Initial objects and variables
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()
r_angles = [40, 320]
l_angles = [140, 220]

# Handling controls
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# The main game loop
game_is_on = True

while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(0.01)

    # Detect a collision with walls, and bounce in the needed, and a bit random direction
    if ball.ycor() >= 290 and ball.direction == "right":
        ball.setheading(random.randint(310, 330))
    if ball.ycor() >= 290 and ball.direction == "left":
        ball.setheading(random.randint(210, 230))
    if ball.ycor() <= -280 and ball.direction == "right":
        ball.setheading(random.randint(30, 50))
    if ball.ycor() <= -280 and ball.direction == "left":
        ball.setheading(random.randint(130, 150))

    # Detect a collision with a paddle, increase a speed of the ball after a contact
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.direction = "left"
        ball.setheading(random.choice(l_angles))
        ball.speed += 1
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.direction = "right"
        ball.setheading(random.choice(r_angles))
        ball.speed += 1

    # Detect the right paddle misses
    if ball.xcor() >= 400:
        ball.setpos(0, 0)
        ball.direction = "left"
        ball.setheading(random.choice(l_angles))
        ball.speed = 2
        scoreboard.l_score += 1
        scoreboard.display_score()
    # Detect the left paddle misses
    if ball.xcor() <= -400:
        ball.setpos(0, 0)
        ball.direction = "right"
        ball.setheading(random.choice(r_angles))
        ball.speed = 2
        scoreboard.r_score += 1
        scoreboard.display_score()
    
    # Check score and stope the game if it's over
    if scoreboard.if_gameover():
        game_is_on = False


screen.exitonclick()