import sys
import pygame
import pygame_menu
import random
import game as start


def game():
    start.Game(player.get_value())

def loss(pname, points):
    screen = pygame.display.set_mode((1280, 720))
    r = 0
    file = open('save.txt', mode='a', encoding='UTF-8')
    file.write(f'\n{pname}, {points}')
    while True:
        pygame.time.Clock().tick(120)
        r += 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        font = pygame.font.Font('pr/Pokemon GB.ttf', 55)
        if r > 255:
            sys.exit()
        losstext = font.render('Loss', 1, (r, 0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load('pr/mainback.jpg'), (1280, 720)), (0, 0))
        screen.blit(losstext, (540, 360))
        screen.blit(font.render(pname, 1, (255, 255, 255)), (10, 560))
        screen.blit(font.render(str(points),  1, (255, 255, 255)), (10, 660))
        pygame.display.flip()




if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((1280, 720))
    menu = pygame_menu.Menu('Welcome', 1280, 720,
                            theme=pygame_menu.themes.THEME_DARK)
    player = menu.add.text_input('Name :', default='John Doe', )
    menu.add.button('Play', game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    surface.blit(pygame.image.load('pr/mainback.jpg'), (0, 0))

    menu.mainloop(surface)
