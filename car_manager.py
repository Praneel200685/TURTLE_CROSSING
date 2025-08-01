from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance==1 or random_chance==5 or random_chance==3:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def levelup(self):
        self.car_speed += MOVE_INCREMENT
