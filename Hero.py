import pygame


class hero(pygame.sprite.Sprite):

    def __init__(self, backGroundSite):
        self.image1 = pygame.image.load('Image/hero1.png').convert_alpha()
        self.image2 = pygame.image.load('Image/hero2.png').convert_alpha()
        self.status = True
        self.speed = 10
        self.rect = self.image1.get_rect()
        self.bgWidth, self.bgHeight = backGroundSite
        self.rect.left, self.rect.top = (self.bgWidth - self.rect.width)/2, self.bgHeight - self.rect.height - 60

    def getImage(self):
        if self.status:
            return self.image1
        else:
            return self.image2

    def setStatus(self):
        self.status = not self.status

     #移动方法中可能移动后超出范围

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= 10
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.bgHeight - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.bgHeight - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.bgWidth:
            self.rect.right += 10
        else:
            self.rect.right = self.bgWidth