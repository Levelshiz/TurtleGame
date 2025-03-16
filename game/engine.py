from turtle import *
from .player import Player
from .config import WINDOW_WIDTH, WINDOW_HEIGHT
from time import sleep
from .food import Food
class Engine ():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen.title ("turtle.game")
        self.player = Player()
        self.player.setup_keyboard_bindings(self.screen)
        self.food = Food()
        self.player.food = self.food




    #Игровой цикл
    def start(self):
        while True:
            self.player.move()
            self.screen.update ()
            sleep(1 / 240)

