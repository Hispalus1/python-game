import pygame as pg
import os

original_image = pg.image.load(os.path.join("image/postava.png"))
image = pg.transform.scale(original_image, (25, 25))


class Player():
    def __init__(self, x, y, win):
        self.rect = pg.Rect(x, y, 25, 25)
        self.x = x
        self.y = y
        self.platno = win
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.hitbox = (self.x, self.y, 25, 25)
        self.speed = 4

    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)
        win.blit(image, (self.x, self.y))

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and self.x >= 0:
            self.velX = -self.speed
        if self.right_pressed and self.x <= 874:
            self.velX = self.speed
        if self.up_pressed and self.y >= 0:
            self.velY = -self.speed
        if self.down_pressed and self.y <= 874:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.hitbox = (self.x, self.y, 25, 25)

        self.rect = pg.Rect(self.hitbox)
