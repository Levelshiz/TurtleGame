from turtle import *
import random
from .config import *
import time

class Enemy(Turtle):



    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.color("black")
        self.penup()
        self.speed(0)
        self.interval_angle = random.randint(1, 3)
        self.last_change_direction = time.time ()
        self.set_random_direction()
        self.spawn()



    def spawn(self):
        """Появление enemies"""
        x = random.randint(-WINDOW_WIDTH // 2 + 50, WINDOW_WIDTH // 2 - 50)
        y = random.randint(-WINDOW_HEIGHT // 2 + 50, WINDOW_HEIGHT // 2 - 50)
        self.teleport(x, y)



    def set_random_direction(self):
        """Задает случайное направление"""
        angle = random.randint (0,360)
        self.setheading(angle)

    def move(self):
        """Создаёт границы экрана"""


        self.forward(PLAYER_SPEED * 0.75)
        if self.xcor() > WINDOW_WIDTH / 2:
            self.goto(-WINDOW_WIDTH / 2, self.ycor())
        if self.xcor() < -WINDOW_WIDTH / 2:
            self.goto(WINDOW_WIDTH / 2, self.ycor())
        if self.ycor() > WINDOW_WIDTH / 2:
            self.goto(self.xcor(), -WINDOW_HEIGHT / 2)
        if self.ycor() < -WINDOW_HEIGHT / 2:
            self.goto(self.xcor(), WINDOW_HEIGHT / 2)


        if time.time() - self.last_change_direction > self.interval_angle:
            self.set_random_direction()
            self.interval_angle = random.randint(1, 3)
            self.last_change_direction = time.time()
    def check_player(self,player):
        """Проверяет дистанцию и меняет ее спустя время"""
        return self.distance(player) < 20