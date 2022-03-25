##
## EPITECH PROJECT, 2021
## Untitled (Workspace)
## File description:
## object
##

import pygame
import sources.pong as pong

class Objects:
    def __init__(self):
        self.player = Player()
        self.ball = Ball()
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.player);
        self.sprite_group.add(self.ball);


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = pygame.image.load("./assets/sprites.png")
        rect2 = pygame.rect.Rect(5, 5, 40, 130)
        self.image = image.subsurface(rect2)
        self.image = pygame.transform.scale(self.image, (200, 300))
        self.rect = self.image.get_rect()
    
    def update(self, pong):
        pos = pygame.mouse.get_pos()
        if (pos[0] >= pong.settings.screen_width / 2):
            pos2 = list(pos)
            pos2[0] = pong.settings.screen_width / 2
            pos = tuple(pos2)
        self.rect.center = pos

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = pygame.image.load("./assets/sprites.png")
        rect = pygame.rect.Rect(115, 10, 35, 35)
        self.x = -5
        self.y = 5
        self.image = image.subsurface(rect)
        self.image = pygame.transform.scale(self.image, (190, 190))
        self.rect = self.image.get_rect()
        self.rect.center = tuple((850,450))
    
    def update(self, pong):
        super().__init__()
        pos = self.rect.center;
        new_pos = list(pos)
        new_pos[0] += self.x
        new_pos[1] += self.y
        mouse = pong.objects.sprite_group.sprites()[0].rect.center
        size = pong.objects.sprite_group.sprites()[0].rect.size
        if ((new_pos[1] >= mouse[1] - size[1] / 8 and new_pos[1] <= mouse[1] + size[1] / 8) and
        (new_pos[0] >= mouse[0] - size[0] / 2 and new_pos[0] <= mouse[0] + size[0] / 2)):
            self.y = -(self.y - 1 if self.y < 0 else self.y + 1) if self.y != 0 else self.y
            self.x = -(self.x - 1 if self.x < 0 else self.x + 1) if self.x != 0 else self.x
        if (new_pos[1] >= pong.settings.screen_height or new_pos[1] <= 0 + self.image.get_size()[1] - 10):
            self.y = -(self.y + 2 if self.y < 0 else self.y - 2) if self.y != 0 else self.y
            self.x = self.x + 2 if self.x < 0 else self.x - 2 if self.x > 0 else self.x
        if (new_pos[0] >= pong.settings.screen_width):
            pong.points_p1 += 1
            new_pos = (850, 450)
        if (new_pos[0] <= 0 + self.image.get_size()[0] - 100):
            pong.points_p2 += 1
            new_pos = (850, 450)
        pos = tuple(new_pos)
        self.rect.center = pos
