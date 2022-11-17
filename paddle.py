from turtle import Turtle
import random
import sys


class Paddle(Turtle):  # paddle class is now the same as turtle
    def __init__(self, position):
        super().__init__()  # allows paddle to inherit functionalities of turtle class
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)



class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce(self):
         self.y_move *= -1