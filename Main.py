import pygame
from Hero import hero
from Bullet import bullet
from Enemy import smallEnemy, midEnemy, bigEnemy
import sys

# 游戏初始化
pygame.init()
pygame.mixer.init()

# 控制飞机数量以及子弹数量
smallEnemyNum = 6
midEnemyNum = 3
bigEnemyNum = 1
bulletNum = 6

# 血槽颜色及分数字体颜色
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# 游戏字体
scoreFont = pygame.font.Font('Font/font.ttc', 36)

# 背景图片及尺寸
backGroundSite = (400, 800)
screen = pygame.display.set_mode(backGroundSite)
pygame.display.set_caption('PlaneGame')
backGround = pygame.image.load('Image/background.png').convert()

# 功能按钮
suspend1 = pygame.image.load('Image/suspend1.png').convert_alpha()
suspend2 = pygame.image.load('Image/suspend2.png').convert_alpha()
continued1 = pygame.image.load('Image/continued1.png').convert_alpha()
continued2 = pygame.image.load('Image/continued2.png').convert_alpha()
pauseRect = suspend1.get_rect()
pauseRect.left, pauseRect.top = 400 - pauseRect.width - 10, 10

# 主菜单相关
gameAgain = pygame.image.load('Image/game_again.png').convert_alpha()
gameAgainRect = gameAgain.get_rect()
gameAgainRect.left, gameAgainRect.top = (400 - gameAgainRect.width) / 2, 300
gameContinue = pygame.image.load('Image/game_continue.png').convert_alpha()
gameContinueRect = gameContinue.get_rect()
gameContinueRect.left, gameContinueRect.top = (400 - gameContinueRect.width) / 2, 400
gameQuit = pygame.image.load('Image/game_quit.png').convert_alpha()
gameQuitRect = gameQuit.get_rect()
gameQuitRect.left, gameQuitRect.top = (400 - gameQuitRect.width) / 2, 500

# 背景音乐，不支持MP3用OGG格式
pygame.mixer.music.load('Sound/game_music.ogg')
pygame.mixer.music.set_volume(3)

# 飞机相关音效
smallEnemyDown = pygame.mixer.Sound('Sound/small_enemy_down.ogg')
smallEnemyDown.set_volume(2)
midEnemyDown = pygame.mixer.Sound('Sound/mid_enemy_down.ogg')
midEnemyDown.set_volume(3)
bigEnemyDown = pygame.mixer.Sound('Sound/big_enemy_down.ogg')
bigEnemyDown.set_volume(3)
bigEnemyFlying = pygame.mixer.Sound('Sound/big_enemy_flying.ogg')
bigEnemyFlying.set_volume(2)

# 等级（难度）提升特效
upgrade = pygame.mixer.Sound('Sound/upgrade.ogg')
upgrade.set_volume(3)

# 将飞机加入相应的碰撞组


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

# 增加飞机速度


def addSpeeds(group):
    for each in group:
        each.addSpeed()


def main():

    # 是否暂停，以及暂停相关按钮图片
    isPause = False
    pauseImage = suspend1

    # 游戏分数以及等级
    score = 0
    level = 1

    # 产生飞机
    me = hero(backGroundSite)
    enemies = pygame.sprite.Group()
    smallEnemys = pygame.sprite.Group()
    midEnemys = pygame.sprite.Group()
    bigEnemys = pygame.sprite.Group()
    addEnemy('small', smallEnemys, enemies, smallEnemyNum)
    addEnemy('mid', midEnemys, enemies, midEnemyNum)
    addEnemy('big', bigEnemys, enemies, bigEnemyNum)

    # 产生子弹
    bulletIndex = 0
    bullets = []
    for i in range(bulletNum):
        bullets.append(bullet(me.rect.midtop))

    # 计时器，判断是否切换我方飞机图片,大型敌机图片以及发射子弹等
    timeToChange = 100

    # 背景音乐开始，游戏主循环开始
    pygame.mixer.music.play(3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pauseRect.collidepoint(event.pos):
                if isPause:
                    pauseImage = suspend1
                else:
                    pauseImage = continued1
                isPause = not isPause
            elif event.type == pygame.MOUSEMOTION:
                if pauseRect.collidepoint(event.pos):
                    if isPause:
                        pauseImage = continued2
                    else:
                        pauseImage = suspend2
                else:
                    if isPause:
                        pauseImage = continued1
                    else:
                        pauseImage = suspend1

        if not isPause:

            # 获取键盘输入
            keyPress = pygame.key.get_pressed()
            if keyPress[pygame.K_UP] or keyPress[pygame.K_w]:
                me.moveUp()
            if keyPress[pygame.K_DOWN] or keyPress[pygame.K_s]:
                me.moveDown()
            if keyPress[pygame.K_LEFT] or keyPress[pygame.K_a]:
                me.moveLeft()
            if keyPress[pygame.K_RIGHT] or keyPress[pygame.K_d]:
                me.moveRight()

            # 提升等级（难度）
            if level == 1 and score > 50000:
                level = 2
                upgrade.play()
                addEnemy('small', smallEnemys, enemies, 3)
                addEnemy('mid', midEnemys, enemies, 2)
                addEnemy('big', bigEnemys, enemies, 1)
            elif level == 2 and score > 200000:
                level = 3
                upgrade.play()
                addSpeeds(enemies)

            timeToChange -= 1
            if timeToChange % 5 == 0:
                me.setStatus()
                # 加上判断存活的语句反而消耗更多资源，故不管死活直接更改，类内会进行判断
                for each in bigEnemys:
                    each.setStatus()

            # 每10帧发射一颗子弹
            if timeToChange % 10 == 0:
                bullets[bulletIndex].reset(me.rect.midtop)
                bulletIndex = (bulletIndex + 1) % bulletNum
            if timeToChange == 0:
                timeToChange = 100

            # 判断我方飞机是否被撞
            enemiesDown = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            for each in enemiesDown:
                each.active = False

            screen.blit(backGround, (0, 0))

            # 判断是否命中敌机
            for each in bullets:
                if each.active:
                    each.move()
                    screen.blit(each.getImage(), each.rect)
                    enemiesHit = pygame.sprite.spritecollide(each, enemies, False, pygame.sprite.collide_mask)
                    if len(enemiesHit) > 0:
                        each.active = False
                        for n in enemiesHit:
                            if n in midEnemys or n in bigEnemys:
                                n.energyFall()
                            else:
                                n.active = False

            # 飞机绘制顺序，大-》中-》小
            for each in bigEnemys:
                if each.active:
                    each.move()
                    # 大飞机出场音效
                    # if each.rect.bottom > 0:
                    #    bigEnemyFlying.play()

                    # 绘制大型敌机血槽
                    pygame.draw.line(screen, black, (each.rect.left, each.rect.top - 5),
                                                    (each.rect.right, each.rect.top - 5),
                                                      2)
                    energyRemain = each.energy / bigEnemy.bigEnergy
                    if energyRemain > 0.3:
                        energyColor = green
                    else:
                        energyColor = red
                    pygame.draw.line(screen, energyColor, (each.rect.left, each.rect.top - 5),
                                                          (each.rect.left + each.rect.width * energyRemain, each.rect.top - 5),
                                                            2)
                else:
                    if each.desStart():
                        bigEnemyFlying.stop()
                        bigEnemyDown.play()
                    if each.desComplete(timeToChange % 5 == 0):
                        bigEnemyDown.stop()
                        score += 10000
                        each.reset()
                screen.blit(each.getImage(), each.rect)

            for each in midEnemys:
                if each.active:
                    each.move()
                    # 绘制中型敌机血槽
                    pygame.draw.line(screen, black, (each.rect.left, each.rect.top - 5),
                                                    (each.rect.right, each.rect.top - 5),
                                                      2)
                    energyRemain = each.energy / midEnemy.midEnergy
                    if energyRemain > 0.3:
                        energyColor = green
                    else:
                        energyColor = red
                    pygame.draw.line(screen, energyColor, (each.rect.left, each.rect.top - 5),
                                                          (each.rect.left + each.rect.width * energyRemain, each.rect.top - 5),
                                                            2)
                else:
                    # 中型飞机摧毁音效未完美
                    if each.desStart():
                        midEnemyDown.play()
                    if each.desComplete(timeToChange % 5 == 0):
                        midEnemyDown.stop()
                        score += 6000
                        each.reset()
                screen.blit(each.getImage(), each.rect)

            for each in smallEnemys:
                if each.active:
                    each.move()
                else:
                    if each.desStart():
                        smallEnemyDown.play()
                    if each.desComplete(timeToChange % 5 == 0):
                        smallEnemyDown.stop()
                        score += 1000
                        each.reset()
                screen.blit(each.getImage(), each.rect)

            screen.blit(me.getImage(), me.rect)
        # 暂停状态显示主菜单
        else:
            screen.blit(backGround, (0, 0))
            screen.blit(gameAgain, gameAgainRect)
            screen.blit(gameContinue, gameContinueRect)
            screen.blit(gameQuit, gameQuitRect)

        scoreText = scoreFont.render('Score:%s' % str(score), True, white)
        screen.blit(scoreText, (0, 0))
        screen.blit(pauseImage, pauseRect)
        pygame.display.flip()


if __name__ == '__main__':
    main()



