from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("White")


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.speed(0)

    def down_up(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.speed(0)

