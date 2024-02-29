import sys
import pygame
import pygame_menu
import random
import game as start


def loss():
    screen = pygame.display.set_mode((1280, 720))
    r = 0
    while True:
        pygame.time.Clock().tick(240)
        r += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        font = pygame.font.Font('pr/Pokemon GB.ttf', 55)
        if r == 255:
            sys.exit()
        losstext = font.render('Loss', 1, (r, 0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load('pr/mainback.jpg'), (1280, 720)), (0, 0))
        screen.blit(losstext, (540, 360))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    loss()