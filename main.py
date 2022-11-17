from turtle import Screen, Turtle
from paddle import Paddle,Ball
import time


# create screen, its title, size and background colour
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# screen animator removal
screen.tracer(0)

# Create new paddle object from the paddle class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


    




# # listen to key press to control the movement of the paddle using the system button
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# to make things show on the screen
game_is_on = True;

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    # Detect Collision 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()
