import sys
import pygame
import random
import main

WIDTH = 1280
HEIGHT = 720
FPS = 240

pygame.init()


def game(pname):
    class Text:
        def __init__(self, sc):
            self.font = pygame.font.Font('pr/Pokemon GB.ttf', 35)
            self.font2 = pygame.font.Font('pr/Pokemon GB.ttf', 35)
            self.point = 0
            self.sc = sc
            self.check = self.font.render(str(self.point), 1, (10, 50, 0))

        def update(self):
            self.sc.blit(self.check, (10, 50))

        def pointadd(self):
            self.point += 10
            self.check = self.font.render(str(self.point), 1, (10, 50, 0))

        def give(self):
            return self.point

    class Win:
        def __init__(self, bg):
            self.image = bg
            self.cam_x = 0

        def update(self):
            if pygame.key.get_pressed()[pygame.K_d]:
                self.cam_x -= 3
            if self.cam_x < -1280:
                self.cam_x = 0
            screen.blit(self.image, (self.cam_x, 0))
            screen.blit(self.image, (self.cam_x + 1280, 0))

    class Pull(pygame.sprite.Sprite):
        def __init__(self, n):
            pygame.sprite.Sprite.__init__(self)
            self.nap = n
            self.image = pygame.transform.scale(pygame.image.load('pr/Arrow.png'), (50, 50))
            self.rect = self.image.get_rect()
            self.rect.center = player.rect.center

        def update(self):
            if self.nap == 'r':
                self.rect.x += 10
            else:
                self.rect.x -= 10
            if self.rect.right > WIDTH + 100 or self.rect.right < 0:
                self.kill()

    class Zomb(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('pr/zomb.png'), (70, 120))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(1280, 1600), 630)
            self.count = 0

        def update(self):
            if pygame.key.get_pressed()[pygame.K_d]:
                self.rect.x -= 3
            self.rect.x -= 1

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.y > HEIGHT - 100:
                self.rect.top = HEIGHT - 100
            if self.rect.y < 0:
                self.rect.top = 0

            self.image = zdviz[self.count // 6]
            self.count += 1
            if self.count == 36:
                self.count = 0

    class Player(pygame.sprite.Sprite):
        def __init__(self, bg):
            pygame.sprite.Sprite.__init__(self)
            self.keys = []
            self.nap = ''
            self.image = bg
            self.jump = 0
            self.jbol = True
            self.count = 0
            self.rect = self.image.get_rect()
            self.rect.center = (10, 650)

        def update(self):
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_a]:
                self.rect.x -= 5
                self.nap = 'l'
            if self.keys[pygame.K_d]:
                self.rect.x += 5
                self.nap = 'r'
            if self.keys[pygame.K_SPACE] and self.jump <= 20 and self.jbol:
                self.jump += 1
                self.rect.y -= 5
                if self.jump == 20:
                    self.jbol = False
            elif self.jump:
                self.jump -= 1
                self.rect.y += 5
                if self.jump == 0:
                    self.jbol = True

            self.image = br

            if self.rect.right > WIDTH - 300:
                self.rect.right = WIDTH - 300
            if self.rect.left < 0:
                self.rect.left = 0

        def anim(self):
            self.keys = pygame.key.get_pressed()
            if self.count > 56:
                self.count = 0
            if self.keys[pygame.K_d]:
                self.image = dviz[self.count // 8]
                self.count += 1
            if self.keys[pygame.K_a]:
                self.image = ldviz[self.count // 8]
                self.count += 1

        def shoot(self):
            if self.nap == 'r':
                pull = Pull('r')
            else:
                pull = Pull('l')
            all_sprites.add(pull)
            pulls.add(pull)

    size = WIDTH, HEIGHT
    name = pname
    dviz = [pygame.transform.scale(pygame.image.load(f'Archer/_0{i}.png'), (60, 70)) for i in range(1, 9)]
    ldviz = [pygame.transform.scale(pygame.image.load(f'ArcherL/_0{i}.png'), (60, 70)) for i in range(1, 9)]
    zdviz = [pygame.transform.scale(pygame.image.load(f'Zombie/{i}.png'), (70, 120)) for i in range(1, 7)]
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    pulls = pygame.sprite.Group()
    point = Text(screen)
    back = Win(pygame.transform.scale(pygame.image.load('pr/back.png'), (1280, 720)))
    br = pygame.image.load('pr/perc.png')
    br = pygame.transform.scale(br, (50, 70))
    player = Player(br)
    zombs = pygame.sprite.Group()
    for i in range(random.randint(1, 10)):
        zombs.add(Zomb())
    clock = pygame.time.Clock()
    all_sprites.add(player)
    all_sprites.add(zombs)
    running = True
    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot()
        hits = pygame.sprite.spritecollide(player, zombs, False)
        if hits:
            main.loss(name, point.give())
        hitsp = pygame.sprite.groupcollide(zombs, pulls, True, True)
        if hitsp:
            point.pointadd()
        if not zombs.sprites():
            for _ in range(random.randint(1, 15)):
                zombs.add(Zomb())
                all_sprites.add(zombs)
        back.update()
        point.update()
        player.anim()
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
    sys.exit()
