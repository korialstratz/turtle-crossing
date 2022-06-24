from turtle import Turtle

FONT = ('Arial', 18, 'normal')
ALIGNMENT = "left"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-260, 260)
        self.level = 0
        self.move_time = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.move_time *= 0.9
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
