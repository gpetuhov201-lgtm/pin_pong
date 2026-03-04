from pygame import *
from models import *
from random import *
from time import time as t

window = display.set_mode((700,500))
window.fill((31, 171, 184))




flag = True

FPS = 60
clock = time.Clock()
while flag:
    display.update()
    clock.tick(FPS)
    events = event.get()
    for i in events:
        if i.type == QUIT:
            flag = False