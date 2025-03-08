from turtle import *
from random import randint
class Hero(Turtle):
    def __init__(self, x, y, c = 'red', s = 'square'):
        super().__init__()
        self.penup()
        self.speed(10)
        self.color(c)
        self.shape(s)
        self.goto(x,y)

    def move_up(self):
        sprite.setheading(90)
        sprite.forward(10)

    def move_down(self):
        sprite.setheading(270)
        sprite.forward(10)

    def move_right(self):
        sprite.setheading(0)
        sprite.forward(10)

    def move_left(self):
        sprite.setheading(180)
        sprite.forward(10)

    def change_angle(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

        angle = self.towards(self.x_end, self.y_end)# float
        self.setheading(angle)

    def move(self):
        self.forward(10)
        if self.distance(self.x_end, self.y_end) <= 10:
            #self.change_angle(self.x_end, self.y_end, self.x_start, self.y_start)
            self.change_angle(self.x_end, self.y_end, randint(-200,200), randint(-200,200))

    def bumb(self, hero):
        if self.distance(hero.xcor(), hero.ycor()) < 30:
            return True
        else:
            return False


finish = Hero(200,220, 'green', 'triangle')
sprite = Hero(-50, -200, 'blue', 'turtle')
enemy1 = Hero(-200,50)
enemy1.change_angle(-200,50, 200, 50)
enemy2 = Hero(200,-50)
enemy2.change_angle(200,-50, randint(-200,200), randint(-200,200))

screen = sprite.getscreen()
screen.listen()

screen.onkey(sprite.move_up, 'Up')
screen.onkey(sprite.move_down, 'Down')
screen.onkey(sprite.move_right, 'Right')
screen.onkey(sprite.move_left, 'Left')

game = True
while game:
    enemy1.move()
    enemy2.move()   
    if sprite.bumb(finish):
        game = False
done()
