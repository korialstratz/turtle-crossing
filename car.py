from turtle import Turtle
import random

COLOR_LIST = ["midnight blue", "chocolate", "DarkSlateGray4", "aquamarine2", "goldenrod1", "orange",
              "green", "OrangeRed2", "maroon2", "orchid2", "red2", "tan1", "yellow", "purple"]

POWER_X = 26
POWER_Y = 25


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLOR_LIST))
        self.shapesize(stretch_len=1.5)
        self.shape("square")
        self.x = -260 + (20 * random.randint(0, POWER_X))
        self.y = -250 + (20 * random.randint(0, POWER_Y))
        self.goto(self.x, self.y)

    def move(self):
        move_distance = random.randint(1, 10)
        new_x = self.xcor() - move_distance
        y = self.ycor()
        self.goto(new_x, y)

    def to_start(self):
        new_y = -250 + (20 * random.randint(0, POWER_Y))
        self.goto(310, new_y)
