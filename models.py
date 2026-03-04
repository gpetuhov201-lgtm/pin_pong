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