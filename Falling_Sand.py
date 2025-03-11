# Constants

SCREEN_SIZE = 500
GRID_AMOUNT = 100
GRID_SIZE = SCREEN_SIZE / GRID_AMOUNT

# Variables

running = True
grid = [[0 for i in range(GRID_AMOUNT)] for i in range(GRID_AMOUNT)]

# Libraries

import pygame

from os import environ
from math import floor
from random import randint

environ["SDL_VIDEO_WINDOW_POS"] = "0,0"

pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
pygame.display.set_caption("Falling Sand")

framerateController = pygame.time.Clock()

sandSpriteGroup = pygame.sprite.Group()

# Classes and Functions

def get_pos(pos):
    return int(pos * GRID_SIZE)

def get_which_grid(pos):
    x = pos[0]
    y = pos[1]

    x = floor(x / GRID_SIZE)
    y = floor(y / GRID_SIZE)
    return x,y

def get_drop(gridx):
    gridy = 0
    for y in range(len(grid)):
        if grid[y][gridx] == 0:
            gridy = y
        else:
            break
    return gridy

def go_down(sprite):
    if sprite.gridy < GRID_AMOUNT-1:
        if grid[sprite.gridy+1][sprite.gridx] == 0:
            grid[sprite.gridy][sprite.gridx] = 0
            sprite.gridy += 1
            sprite.rect.y = get_pos(sprite.gridy)
            grid[sprite.gridy][sprite.gridx] = 1
            return True
    return False

def go_left(sprite):
    if sprite.gridy < GRID_AMOUNT and sprite.gridx > 0:
        if grid[sprite.gridy+1][sprite.gridx-1] == 0:
            grid[sprite.gridy][sprite.gridx] = 0
            sprite.gridy += 1
            sprite.gridx -= 1
            sprite.rect.y = get_pos(sprite.gridy)
            sprite.rect.x = get_pos(sprite.gridx)
            grid[sprite.gridy][sprite.gridx] = 1
            return True
    return False

def go_right(sprite):
    if sprite.gridy < GRID_AMOUNT and sprite.gridx < GRID_AMOUNT - 1:
        if grid[sprite.gridy+1][sprite.gridx+1] == 0:
            grid[sprite.gridy][sprite.gridx] = 0
            sprite.gridy += 1
            sprite.gridx += 1
            sprite.rect.x = get_pos(sprite.gridx)
            sprite.rect.y = get_pos(sprite.gridy)
            grid[sprite.gridy][sprite.gridx] = 1
            return True
    return False

class Sand(pygame.sprite.Sprite):
    def __init__(self,gridx,gridy):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(x = get_pos(gridx), y = get_pos(gridy))
        self.gridx = gridx
        self.gridy = gridy
        sandSpriteGroup.add(self)
        grid[gridy][gridx] = 1
    
    def gravity(self):
        fall = go_down(self)

        if not fall:
            if get_drop(self.gridx-1) > get_drop(self.gridx+1) and get_drop(self.gridx-1) > self.gridy:
                go_left(self)
            elif get_drop(self.gridx-1) < get_drop(self.gridx+1) and get_drop(self.gridx+1) > self.gridy:
                go_right(self)
            elif get_drop(self.gridx-1) == get_drop(self.gridx+1) and get_drop(self.gridx-1) > self.gridy:
                if randint(1,2) == 1:
                    go_left(self)
                else:
                    go_right(self)


def make_sand(x, y):
    sand = Sand(x,y)

while running:
    framerateController.tick(GRID_AMOUNT // 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos
            gridx, gridy = get_which_grid(mouse_pos)
            make_sand(gridx,gridy)

    for sand in sandSpriteGroup:
        sand.gravity()

    screen.fill("black")
    sandSpriteGroup.draw(screen)
    pygame.display.update()

pygame.quit()