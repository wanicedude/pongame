from turtle import Turtle

class Paddle(Turtle): #paddle class is now the same as turtle
    def __init__(self, position):
        super().__init__() # allows paddle to inherit functionalities of turtle class
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



        
    
    
        
        
        


















