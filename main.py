from turtle import Screen
from timmy import Timmy
from score import Score
from car import Car
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(False)
screen.listen()
score = Score()
timmy = Timmy()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")

car_count = 30
car_list = []


for cars in range(car_count):
    car = Car()
    car_list.append(car)


game_on = True
while game_on:
    time.sleep(score.move_time)
    screen.update()
    for c in car_list:
        c.move()
        if c.xcor() < -320:
            c.to_start()
        if timmy.distance(c) < 20:
            game_on = False
            score.game_over()

    if timmy.ycor() > 260:
        score.level_up()
        timmy.start_line()

screen.exitonclick()
