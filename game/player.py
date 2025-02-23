from turtle import *
from .config import *


class Player(Turtle):
    _HP = MAX_HP
    _speed = PLAYER_SPEED

    def __init__(self):
        super().__init__()
        self.penup()