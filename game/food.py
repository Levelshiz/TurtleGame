from turtle import *
from .config import *
import random



class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.change_position()
        self.shapesize(0.5,0.5)
    def change_position (self):
        x = random.randint(-WINDOW_WIDTH // 2 + 50, WINDOW_WIDTH // 2 - 50)
        y = random.randint(-WINDOW_HEIGHT // 2 + 50, WINDOW_HEIGHT // 2 - 50)
        self.teleport(x,y)