from turtle import Screen, Turtle
from paddle import Paddle


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



# # listen to key press to control the movement of the paddle using the system button
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# to make things show on the screen
game_is_on = True;

while game_is_on:
    screen.update()


screen.exitonclick()
