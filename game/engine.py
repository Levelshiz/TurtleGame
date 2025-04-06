import time
from turtle import *
from turtledemo.penrose import start

from .player import Player
from .config import *
from time import sleep
from .food import Food
from .enemy import Enemy
from .ui import *
class Engine ():



    def __init__(self):
        self.screen = Screen()
        self.screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen.title ("turtle.game")

        self.player = Player()
        self.player.setup_keyboard_bindings(self.screen)

        self.food = Food()
        self.player.food = self.food     #Передаем переменную еды игроку

        self.enemies = []
        self.last_spawn_time = time.time()

        self.ui = Ui(self.player)
        self.player.ui = self.ui          #Передаем интерфейс игроку


        self.game_over = False
        self.screen.onkeypress(self.restart_game,'r')
        self.screen.listen()









    def spawn_enemy(self):
        '''Спавнит врага'''
        enemy = Enemy()
        self.enemies.append(enemy)

    def update_enemies(self):
       for enemy in self.enemies:
           enemy.move()
           if enemy.check_player(self.player):
               self.player.take_damage(DAMAGE)
               enemy.hideturtle()
               self.enemies.remove(enemy)
               self.ui.update_hp_display()


    def restart_game(self):
        '''Рестарт игры'''
        self.screen.clear()
        self.__init__()
        self.start()
    def check_gameover(self):
        '''Проверка конца игры'''
        if self.player._HP <= 0:
            self.game_over = True
            self.ui.show_gameover()








    #Игровой цикл
    def start(self):
        while self.game_over == False:
            self.player.move()
            self.screen.update ()
            sleep(1 / 240)
            if time.time() - self.last_spawn_time > SPAWN_INTERVAL:
                self.spawn_enemy()
                self.last_spawn_time = time.time()
            self.update_enemies()
            self.check_gameover()

        self.screen.mainloop()
