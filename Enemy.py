import pygame
import random


class smallEnemy(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/small_enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.bgWidth, self.bgHeight = backGroundSite
        self.speed = 3
        self.active = True
        self.destroyIndex = -1
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy = [
            pygame.image.load('Image/small_enemy_down1.png').convert_alpha(),
            pygame.image.load('Image/small_enemy_down2.png').convert_alpha(),
            pygame.image.load('Image/small_enemy_down3.png').convert_alpha(),
            pygame.image.load('Image/small_enemy_down4.png').convert_alpha()
        ]
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-0.5 * self.bgHeight, 0)

    def reset(self):
        self.active = True
        self.destroyIndex = 0
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-0.5 * self.bgHeight, 0)

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def desStart(self):
        return self.destroyIndex == 0

    def desComplete(self, desChange=False):
        if desChange and not self.active:
            self.destroyIndex += 1
        return self.destroyIndex == 4

    def getImage(self):
        if self.active:
            return self.image
        else:
            return self.destroy[self.destroyIndex]


class midEnemy(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/mid_enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.bgWidth, self.bgHeight = backGroundSite
        self.speed = 2
        self.active = True
        self.destroyIndex = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy = [
            pygame.image.load('Image/mid_enemy_down1.png').convert_alpha(),
            pygame.image.load('Image/mid_enemy_down2.png').convert_alpha(),
            pygame.image.load('Image/mid_enemy_down3.png').convert_alpha(),
            pygame.image.load('Image/mid_enemy_down4.png').convert_alpha()
        ]
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-1 * self.bgHeight, 0)

    def reset(self):
        self.active = True
        self.destroyIndex = 0
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-1 * self.bgHeight, 0)

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def desStart(self):
        return self.destroyIndex == 0

    def desComplete(self, desChange=False):
        if desChange and not self.active:
            self.destroyIndex += 1
        return self.destroyIndex == 4

    def getImage(self):
        if self.active:
            return self.image
        else:
            return self.destroy[self.destroyIndex]


class bigEnemy(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('Image/big_enemy1.png').convert_alpha()
        self.image2 = pygame.image.load('Image/big_enemy2.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.bgWidth, self.bgHeight = backGroundSite
        self.speed = 1
        self.status = True
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)
        self.destroyIndex = 0
        self.destroy = [
            pygame.image.load('Image/big_enemy_down1.png').convert_alpha(),
            pygame.image.load('Image/big_enemy_down2.png').convert_alpha(),
            pygame.image.load('Image/big_enemy_down3.png').convert_alpha(),
            pygame.image.load('Image/big_enemy_down4.png').convert_alpha(),
            pygame.image.load('Image/big_enemy_down5.png').convert_alpha(),
            pygame.image.load('Image/big_enemy_down6.png').convert_alpha()
        ]
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-2 * self.bgHeight, 0)

    def reset(self):
        self.active = True
        self.destroyIndex = -1
        self.rect.left, self.rect.top = random.randint(0, self.bgWidth - self.rect.width),\
                                        random.randint(-2 * self.bgHeight, 0)

    def move(self):
        if self.rect.top < self.bgHeight:
            self.rect.top += self.speed
        else:
            self.reset()

    def setStatus(self):
        self.status = not self.status

    def desStart(self):
        return self.destroyIndex == 0

    def desComplete(self, desChange=False):
        if desChange and not self.active:
            self.destroyIndex += 1
        return self.destroyIndex == 6

    def getImage(self):
        if self.active:
            if self.status:
                return self.image1
            else:
                return self.image2
        else:
            return self.destroy[self.destroyIndex]


