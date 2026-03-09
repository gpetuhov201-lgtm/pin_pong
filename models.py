from pygame import *

class Character(sprite.Sprite):
    def __init__(self,x,y,outfit,w,h,speed,window):
        super().__init__()
        self.window = window
        self.speed = speed
        self.image = transform.scale(image.load(outfit),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        self.window.blit(self.image,(self.rect.x, self.rect.y))


class Wall(Character):
    def moving_wasd(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= self.window.get_size()[1] - self.rect.h:
            self.rect.y += self.speed
    def moving_arrow(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= self.window.get_size()[1] - self.rect.h:
            self.rect.y += self.speed


class Ball(Character):
    speed_x = 3
    speed_y = 3
    win_left_counter = 0
    win_right_counter = 0
    def ball_moving(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def ball_touch(self,wall1,wall2):
        if self.rect.y <= 0 or self.rect.y >= self.window.get_size()[1] - self.rect.h:
            self.speed_y *= -1
        if self.rect.colliderect(wall1.rect) or self.rect.colliderect(wall2.rect):
            self.speed_x *= -1
    def add_point(self,wall1,wall2):
        if self.rect.x <= 0:
            self.win_left_counter += self.start_point(wall1,wall2)
            return True
        if self.rect.x >= self.window.get_size()[0] - self.rect.w:
            self.win_right_counter += self.start_point(wall1,wall2)
            return True
    def start_point(self,wall1,wall2):
        self.rect.x = self.window.get_size()[0]/2 - self.rect.w
        self.rect.y = self.window.get_size()[1]/2 - self.rect.h
        self.speed_x = 3
        self.speed_y = 3
        wall1.rect.y = self.window.get_size()[1]/2 - self.rect.h
        wall2.rect.y = self.window.get_size()[1]/2 - self.rect.h

        return 1
