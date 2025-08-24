# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 30)
    deltaTime = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    loggable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable, loggable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(deltaTime)
        for d in drawable:
            d.draw(screen)
        for l in loggable:
            l.log(screen, font)

        for a in asteroids:
            for s in shots:
                if s.check_collision(a):
                    s.kill()
                    a.split(s)
            if player.check_collision(a):
                return "GAME OVER!"

        pygame.display.flip()
        deltaTime = clock.tick(60)/1000


if __name__ == "__main__":
    print(main())
