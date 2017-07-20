import pygame
from Hero import hero
import sys

pygame.init()
pygame.mixer.init()

backGroundSite = (400, 852)
screen = pygame.display.set_mode(backGroundSite)
pygame.display.set_caption('PlaneGame')
backGround = pygame.image.load('Image/background.png').convert()

# 不支持MP3 用 OGG格式
pygame.mixer.music.load('Sound/game_music.ogg')
pygame.mixer.music.set_volume(3)




def main():
    # 产生飞机
    me = hero(backGroundSite)

    # 计时器，判断是否切换我放飞机图片
    timeToChange = 100

    pygame.mixer.music.play(3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #获取键盘输入
        keyPress = pygame.key.get_pressed()
        if keyPress[pygame.K_UP] or keyPress[pygame.K_w]:
            me.moveUp()
        if keyPress[pygame.K_DOWN] or keyPress[pygame.K_s]:
            me.moveDown()
        if keyPress[pygame.K_LEFT] or keyPress[pygame.K_a]:
            me.moveLeft()
        if keyPress[pygame.K_RIGHT] or keyPress[pygame.K_d]:
            me.moveRight()

        timeToChange -= 1
        if timeToChange % 5 == 0:
            me.setStatus()
        if timeToChange == 0:
            timeToChange = 100


        screen.blit(backGround, (0, 0))
        screen.blit(me.getImage(), me.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()



