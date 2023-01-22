import os
import random

import pygame as pg

original_image = pg.image.load(os.path.join("image/meteor.png"))
image = pg.transform.scale(original_image, (50, 50))


class Meteor:
    def __init__(self, win):
        self.x = random.randrange(0, 900)
        self.y = random.randrange(-1000, 0)
        self.hitbox = (self.x, self.y, 50, 50)
        self.platno = win

    def pohyb(self):
        self.y += 3
        if self.y > 880:
            self.reset()

    def draw(self):
        self.hitbox = (self.x, self.y, 50, 50)
        self.platno.blit(image, (self.hitbox))

    def hit(self):
        print('hit')
        pass

    def reset(self):
        self.y = random.randrange(-1000, 0)
        self.x = random.randrange(0, 900)
