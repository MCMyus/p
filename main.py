import sys
import pygame
import pygame_menu
import game as start


def start_menu():
    global name
    menu_theme = pygame_menu.themes.THEME_DARK.copy()
    menu_theme.set_background_color_opacity(0.5)
    surface = pygame.display.set_mode((1280, 720))
    menu = pygame_menu.Menu('Welcome', 1280, 720,
                            theme=menu_theme)
    pygame.mixer.music.load('pr/backsound.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.01)
    player = menu.add.text_input('Name :', default='John Doe')
    menu.add.button('Play', game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    name = player.get_value()
    while True:
        surface.blit(pygame.transform.scale(pygame.image.load('pr/mainback.jpg'), (1280, 720)), (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        if menu.is_enabled():
            menu.update(events)
            menu.draw(surface)
            pygame.display.update()


def game():
    start.game(name, level)


def next_lvl():
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font('pr/Pokemon GB.ttf', 35)
    text = font.render('Loading next LEVEL', 1, (255, 255, 125))
    a = 0
    while True:
        screen.blit(pygame.transform.scale(pygame.image.load('pr/mainback.jpg'), (1280, 720)), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        a += 5
        screen.blit(text, (350, 80))
        if a // 5 == 25:
            start.game(name, level + 1)
        pygame.display.update()
        clock.tick(start.FPS)


def loss(pname, points):
    screen = pygame.display.set_mode((1280, 720))
    r = 0
    file = open('save.txt', mode='a', encoding='UTF-8')
    file.write(f'{pname}, {points}\n')
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
        screen.blit(font.render(str(points), 1, (255, 255, 255)), (10, 660))
        pygame.display.flip()


level = 0
name = ''
if __name__ == '__main__':
    pygame.init()
    start_menu()
