from turtle import Screen, Turtle

tim = Turtle()
tim.color("white")
tim.shape("square")
tim.penup()
tim.shapesize(stretch_wid=5, stretch_len=5)
tim.setpos(350, 0)


# def g():
#     tim.setheading(90)
#     tim.forward(50)
#
#
# def go():
#     tim.setheading(270)
#     tim.forward(50)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
# screen.onkey(g, "Up")
# screen.onkey(go, "Down")
screen.exitonclick()
