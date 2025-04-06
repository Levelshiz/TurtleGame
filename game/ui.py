from turtle import *
from .player import *
from .config import *

class Ui():

    def __init__(self,player:Player):
        self.player = player
        # Настройка отображение здоровья
        self.hp_display = Turtle()
        self.hp_display.color('red')
        self.hp_display.penup()
        self.hp_display.hideturtle()
        self.hp_display.goto(-WINDOW_WIDTH/2 + 50,WINDOW_HEIGHT/2 - 50)
        self.update_hp_display()


        #Настройка отображения очков
        self.score_display = Turtle()
        self.score_display.color('green')
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(WINDOW_WIDTH/2 - 50,WINDOW_HEIGHT/2 - 50)
        self.update_score_display()





    def update_hp_display(self):
        '''Отображение хп'''
        hp = self.player._HP
        self.hp_display.clear()
        self.hp_display.write(f"HP:{hp}",align='left',font=('Arial',25,'bold'))


    def update_score_display(self):
        '''Отображение очков'''
        score = self.player.score
        self.score_display.clear()
        self.score_display.write(f"Score:{score}",align='right',font=('Arial',25,'bold'))

    def show_gameover (self):
        '''Отображение конца игры'''
        gameover = Turtle()
        gameover.color("red")
        gameover.penup()
        gameover.hideturtle()
        gameover.write(f"GAME OVER\nScore:{self.player.score}\nPress R to restart",align='center',font=('Arial',50,'bold'))


