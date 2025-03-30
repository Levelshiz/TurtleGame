import time
from turtle import *
from .player import Player
from .config import *
from time import sleep
from .food import Food
from .enemy import Enemy
class Engine ():



    def __init__(self):
        self.screen = Screen()
        self.screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen.title ("turtle.game")

        self.player = Player()
        self.player.setup_keyboard_bindings(self.screen)

        self.food = Food()
        self.player.food = self.food

        self.enemies = []
        self.last_spawn_time = time.time()



    def spawn_enemy(self):
        enemy = Enemy()
        self.enemies.append(enemy)

    def update_enemies(self):
       for enemy in self.enemies:
           enemy.move()
           if enemy.check_player(self.player):
               self.player.take_damage(DAMAGE)
               enemy.hideturtle()
               self.enemies.remove(enemy)







    #Игровой цикл
    def start(self):
        while True:
            self.player.move()
            self.screen.update ()
            sleep(1 / 240)
            if time.time() - self.last_spawn_time > SPAWN_INTERVAL:
                self.spawn_enemy()
                self.last_spawn_time = time.time()
            self.update_enemies()