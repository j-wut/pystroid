# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 30)
    deltaTime = 0
    i = 0
    inc = 1
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    loggable = pygame.sprite.Group()
    Player.containers = (updatable, drawable, loggable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(i,i,i))
        updatable.update(deltaTime)
        for d in drawable:
            d.draw(screen)
        for l in loggable:
            l.log(screen, font)
        pygame.display.flip()
        if i >= 64:
            inc = -1
        elif i <= 0:
            inc = 1
        i += inc
        deltaTime = clock.tick(60)/1000


if __name__ == "__main__":
    main()
