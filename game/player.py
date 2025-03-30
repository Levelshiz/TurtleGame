from turtle import *
from .config import *
import math


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.speed (0) #отключаем анимацию движения
        tracer(0,0)    #отключаем анимацию поворота
        self.setheading(90)
        self._HP = MAX_HP
        self._speed = PLAYER_SPEED



        #Вектор движения
        self.dx = 0
        self.dy = 0



    def update_movement_vector(self, direction, state):
        """Обновляет вектор движения в зависимости от нажатия/отпускания клавиш."""
        last_vector = [self.dx, self.dy]

        if direction == "up":
            self.dy = 1 if state == "press" else 0
        elif direction == "down":
            self.dy = -1 if state == "press" else 0
        elif direction == "left":
            self.dx = -1 if state == "press" else 0
        elif direction == "right":
            self.dx = 1 if state == "press" else 0

        if last_vector != [self.dx, self.dy]:
            self.update_heading()
    def update_heading(self):
        if self.dx != 0 or self.dy != 0:
            angle = math.degrees(math.atan2(self.dy, self.dx))
            self.setheading(angle)

    def setup_keyboard_bindings(self, screen):
        """Привязывает клавиши к обновлению вектора движения."""
        screen.onkeypress(lambda: self.update_movement_vector("up", "press"), MOVE_UP)
        screen.onkeyrelease(lambda: self.update_movement_vector("up", "release"), MOVE_UP)
        screen.onkeypress(lambda: self.update_movement_vector("down", "press"), MOVE_DOWN)
        screen.onkeyrelease(lambda: self.update_movement_vector("down", "release"), MOVE_DOWN)
        screen.onkeypress(lambda: self.update_movement_vector("left", "press"), MOVE_LEFT)
        screen.onkeyrelease(lambda: self.update_movement_vector("left", "release"), MOVE_LEFT)
        screen.onkeypress(lambda: self.update_movement_vector("right", "press"), MOVE_RIGHT)
        screen.onkeyrelease(lambda: self.update_movement_vector("right", "release"), MOVE_RIGHT)
        screen.listen()


    def move (self):
        """Создаёт границы экрана"""
        if self.dx == 0 and self.dy == 0: return

        self.forward(self._speed)
        if self.xcor() > WINDOW_WIDTH / 2:
            self.goto(-WINDOW_WIDTH / 2, self.ycor())
        if self.xcor() < -WINDOW_WIDTH / 2:
            self.goto(WINDOW_WIDTH / 2, self.ycor())
        if self.ycor() > WINDOW_WIDTH / 2:
            self.goto(self.xcor(), -WINDOW_HEIGHT / 2)
        if self.ycor() < -WINDOW_HEIGHT / 2:
            self.goto(self.xcor(), WINDOW_HEIGHT / 2)
        self.check_food(self.food)




    def check_food(self,food):
        """Проверяет расстояние до еды и добавляет скорость"""


        if self.distance(food) < 10 :
            self.food.change_position()
            self._HP += 10
            if self._HP > MAX_HP:
                self._HP = MAX_HP
            print(f'{self._HP}/{MAX_HP}')





    def take_damage(self,damage):
        """Получение урона"""
        if damage > 0 and self._HP > 0:
            self._HP -= damage
            print (f'Осталось здоровья:{self._HP}/{MAX_HP}')
            if self._HP <= 0:
                print ("Черепащка умерла")
