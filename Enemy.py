import pygame
import random


class smallEnemy(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/small_enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.bgWidth, self.bgHeight = backGroundSite
        self.speed = 4
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-0.5 * self.bgHeight, 0)

    def reset(self):
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-0.5 * self.bgHeight, 0)

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def getImage(self):
        return self.image


class midEnemy(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/mid_enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.bgWidth, self.bgHeight = backGroundSite
        self.speed = 3
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-1 * self.bgHeight, 0)

    def reset(self):
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-1 * self.bgHeight, 0)

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def getImage(self):
        return self.image


class bigEnemy(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('Image/big_enemy1.png').convert_alpha()
        self.image2 = pygame.image.load('Image/big_enemy2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.bgWidth, self.bgHeight = backGroundSite
        self.speed = 2
        self.status = True
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-2 * self.bgHeight, 0)

    def reset(self):
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-2 * self.bgHeight, 0)

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def setStatus(self):
        self.status = not self.status

    def getImage(self):
        if self.status:
            return self.image1
        else:
            return self.image2

