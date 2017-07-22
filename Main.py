import pygame
from Hero import hero
from Enemy import smallEnemy, midEnemy, bigEnemy
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


# 将飞机加入碰撞组
def addEnemy(size, group1, group2, number):
    for n in range(number):
        if size == 'small':
            e = smallEnemy(backGroundSite)
        elif size == 'mid':
            e = midEnemy(backGroundSite)
        else:
            e = bigEnemy(backGroundSite)
        group1.add(e)
        group2.add(e)

def main():
    # 产生飞机
    me = hero(backGroundSite)
    enemies = pygame.sprite.Group()
    smallEnemys = pygame.sprite.Group()
    midEnemys = pygame.sprite.Group()
    bigEnemys = pygame.sprite.Group()
    addEnemy('small', smallEnemys, enemies, 15)
    addEnemy('mid', midEnemys, enemies, 5)
    addEnemy('big', bigEnemys, enemies, 3)

    # 计时器，判断是否切换我方飞机图片以及大型敌机图片
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
            # 加上判断存活的语句反而消耗更多资源，故不管死活直接更改，类内会进行判断
            for each in bigEnemys:
                each.setStatus()
        if timeToChange == 0:
            timeToChange = 100

        enemiesDown = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        for each in enemiesDown:
            each.active = False

        screen.blit(backGround, (0, 0))

        # 飞机绘制顺序，大-》中-》小
        for each in bigEnemys:
            if each.active:
                each.move()
            if each.desComplete(timeToChange % 5 == 0):
                each.reset()
            screen.blit(each.getImage(), each.rect)
        for each in midEnemys:
            if each.active:
                each.move()
            if each.desComplete(timeToChange % 5 == 0):
                each.reset()
            screen.blit(each.getImage(), each.rect)
        for each in smallEnemys:
            if each.active:
                each.move()
            if each.desComplete(timeToChange % 5 == 0):
                each.reset()
            screen.blit(each.getImage(), each.rect)
        screen.blit(me.getImage(), me.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()



