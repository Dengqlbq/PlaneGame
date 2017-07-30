import pygame


class bullet(pygame.sprite.Sprite):

    def __init__(self, heroPositon):
        self.image1 = pygame.image.load('Image/normal_bullet.png').convert_alpha()
        self.image2 = pygame.image.load('Image/advanced_bullet.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.mask = pygame.sprite.from_surface(self.image1)
        self.active = True
        self.speed = 10
        self.rect.left, self.rect.top = heroPositon

    def move(self):
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed

    def reset(self, heroPosition):
        self.active = True
        self.rect.left, self.rect.top = heroPosition

    def getImage(self, normal):
        if normal:
            return self.image1
        else:
            return self.image2




