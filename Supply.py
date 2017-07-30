import pygame
import random


class bomb(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        self.image = pygame.image.load('Image/bomb.png').convert_alpha()
        self.active = False
        self.speed = 1
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.bgWidth, self.bgHeight = backGroundSite
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width), 0 - self.rect.height

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = False
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width), 0 - self.rect.height

    def getImage(self):
        return self.image


class missile(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        self.image = pygame.image.load('Image/missile.png').convert_alpha()
        self.active = False
        self.speed = 1
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.bgWidth, self.bgHeight = backGroundSite
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width), 0 - self.rect.height

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = False
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width), 0 - self.rect.height

    def getImage(self):
        return self.image
