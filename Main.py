import pygame
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((480, 852))
pygame.display.set_caption('PlaneGame')
backGround = pygame.image.load('Image/background.png').convert()

# 不支持MP3 用 OGG格式
pygame.mixer.music.load('Sound/game_music.ogg')
pygame.mixer.music.set_volume(3)


def main():
    pygame.mixer.music.play(3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(backGround, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()



