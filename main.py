from pygame import *
from models import *
from random import *
from time import time as t,sleep

window = display.set_mode((700,500))

wall1 = Wall(0,150,'media/images/rocket.png',30,150,2,window)
wall2 = Wall(670,150,'media/images/rocket.png',30,150,2,window)
ball = Ball(50,250,'media/images/ball.png',40,40,0,window)


flag = True

FPS = 60
clock = time.Clock()
sleep_flag = False
while flag:
    window.fill((31, 171, 184))
    sleep_flag = ball.add_point(wall1,wall2)
    wall1.draw()
    wall2.draw()
    wall1.moving_wasd()
    wall2.moving_arrow()
    ball.draw()
    ball.ball_moving()
    ball.ball_touch(wall1,wall2)
    display.update()
    if sleep_flag:
        sleep(1)
    clock.tick(FPS)
    events = event.get()
    for i in events:
        if i.type == QUIT:
            flag = False