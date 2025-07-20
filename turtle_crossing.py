import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard  # Optional unless you're planning to use it

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#141414")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Reduce car generation frequency
    if random.randint(1, 6) == 1:
        car_manager.create_car()

    # Move cars
    for car in car_manager.all_cars:
        car.backward(5)

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
    # Detect successful walk
    if player.ycor()>280:
        player.goto(0,-280)
        car_manager.levelup()
        scoreboard.increase_level()

screen.mainloop()