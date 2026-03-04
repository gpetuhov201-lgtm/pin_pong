from pygame import *
from models import *
from random import *
from time import time as t

window = display.set_mode((700,500))

wall1 = Wall(0,60,'media/images/rocket.png',30,150,2,window)
wall2 = Wall(670,60,'media/images/rocket.png',30,150,2,window)


flag = True

FPS = 60
clock = time.Clock()
while flag:
    window.fill((31, 171, 184))
    wall1.draw()
    wall2.draw()
    wall1.moving_wasd()
    wall2.moving_arrow()
    display.update()
    clock.tick(FPS)
    events = event.get()
    for i in events:
        if i.type == QUIT:
            flag = False