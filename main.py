from turtle import Screen, Turtle


# Create Paddle
paddle = Turtle()

# set color and shape
paddle.color("white")
paddle.shape("square")

# Remove paddle trail
paddle.penup()

# set paddle size. the default size os 20px by 20px/ We are setting this to 100px by 20px
paddle.shapesize(stretch_wid=5, stretch_len=1)

# declare where the paddle should goto on the screen
paddle.goto(350, 0)

# create screen, its title, size and background colour
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# screen animator removal
screen.tracer(0)

# define the go up and down function


def go_up():
    new_y = paddle.ycor()+20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor()-20
    paddle.goto(paddle.xcor(), new_y)


# listen to key press to control the movement of the paddle using the system button
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

# to make things show on the screen
game_is_on = True;

while game_is_on:
    screen.update()


screen.exitonclick()
