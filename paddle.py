from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.








    # def __init__(self):
    #     self.segments = []
    #     self.create_snake()
    #     self.head = self.segments[0]

    # def create_snake(self):
    #     for position in STARTING_POSITION:  # for position in pos:
    #         self.add_segment(position)

    # def add_segment(self, position):
    #     new_segment = Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.goto(position)  # segment_1.goto(pos)
    #     self.segments.append(new_segment)

    # def extend(self):
    #     self.add_segment(self.segments[-1].position())



























# # Create Paddle
# paddle = Turtle()

# # set color and shape
# paddle.color("white")
# paddle.shape("square")

# # Remove paddle trail
# paddle.penup()

# # set paddle size. the default size os 20px by 20px/ We are setting this to 100px by 20px
# paddle.shapesize(stretch_wid=5, stretch_len=1)

# # declare where the paddle should goto on the screen
# paddle.goto(350, 0)

# # create screen, its title, size and background colour
# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Pong")

# # screen animator removal
# screen.tracer(0)

# # define the go up and down function


# def go_up():
#     new_y = paddle.ycor()+20
#     paddle.goto(paddle.xcor(), new_y)


# def go_down():
#     new_y = paddle.ycor()-20
#     paddle.goto(paddle.xcor(), new_y)