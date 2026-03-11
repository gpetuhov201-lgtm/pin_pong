from pygame import *
from models import *
from random import *
from time import time as t,sleep

window = display.set_mode((700,500))

wall1 = Wall(0,150,'media/images/rocket.png',30,150,2,window)
wall2 = Wall(670,150,'media/images/rocket.png',30,150,2,window)
ball = Ball(50,250,'media/images/ball.png',40,40,0,window)

font.init()
font_counter = font.Font(None,80)
win_font = font.Font(None,80)
win = win_font.render('Победа игрока',True,(16, 230, 45))
start_btn = Button(290,180,'media/images/start.png',150,60,0,window)
finish_btn = Button(290,250,'media/images/quit.png',150,60,0,window)


flag = True
FPS = 60
clock = time.Clock()
sleep_flag = False
game_flag = False
menu_flag = True
while flag:
    if menu_flag:
        display.update()
        window.fill((31, 171, 184))
        start_btn.draw()
        finish_btn.draw()
        if start_btn.check():
            game_flag = True
            menu_flag = False
        if finish_btn.check():
            flag = False
    if game_flag:
        window.fill((31, 171, 184))
        sleep_flag = ball.add_point(wall1,wall2)
        wall1.draw()
        wall2.draw()
        wall1.moving_wasd()
        wall2.moving_arrow()
        ball.draw()
        ball.ball_moving()
        ball.ball_touch(wall1,wall2)
        counter = font_counter.render(str(ball.lose_left_counter) + ':' + str(ball.lose_right_counter),True,(209, 36, 36))
        window.blit(counter,(300,60))
        if ball.lose_right_counter >= 2:
            player = 'справа!'
            win_player = win_font.render(player,True,(16, 230, 45))
            window.blit(win,(100,250))
            window.blit(win_player,(150,300))
            game_flag = False
        if ball.lose_left_counter >= 2:
            player = 'слева!'
            win_player = win_font.render(player,True,(16, 230, 45))
            window.blit(win,(100,250))
            window.blit(win_player,(150,300))
            game_flag = False
        display.update()
        if sleep_flag:
            sleep(1)
    clock.tick(FPS)
    events = event.get()
    for i in events:
        if i.type == QUIT:
            flag = False