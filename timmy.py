from turtle import Turtle


class Timmy(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("ForestGreen")
        self.shape("turtle")
        self.goto(0, -280)

    def up(self):
        new_y = self.ycor() + 20
        x = self.xcor()
        self.goto(x, new_y)

    def down(self):
        new_y = self.ycor() - 10
        x = self.xcor()
        self.goto(x, new_y)

    def start_line(self):
        self.goto(0, -280)
