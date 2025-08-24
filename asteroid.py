
import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def split(self, shot):
        self.kill()
        splitRatio = random.uniform(0.4, 0.6)
        if self.radius >= ASTEROID_MIN_RADIUS * 2:
            a1 = Asteroid(self.position.x, self.position.y, self.radius * splitRatio)
            a2 = Asteroid(self.position.x,self.position.y, self.radius * (1-splitRatio))
            a1.velocity = self.velocity.copy()
            a2.velocity = self.velocity.copy()
            a1.velocity += shot.velocity.rotate(45) * shot.radius / (2 * self.radius * splitRatio)
            a2.velocity -= shot.velocity.rotate(45) * shot.radius / (2 * self.radius * (1 - splitRatio))
