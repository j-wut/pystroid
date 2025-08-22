# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    deltaTime = 0
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(i%255,i%255,i%255))
        pygame.display.flip()
        i += 1
        deltaTime = clock.tick(60)


if __name__ == "__main__":
    main()
