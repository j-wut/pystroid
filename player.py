import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_ACCEL,
    PLAYER_ACCEL,
    PLAYER_TURN_DRAG,
    PLAYER_DRAG,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SHOOT_SPEED,
    PLAYER_CD,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.initx = x
        self.inity = y
        self.rotation = 0
        self.angularV = 0
        self.cd = 0

    def log(self, screen, font):
        text_surface = font.render(f"position: {self.position}", True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        text_surface = font.render(f"v: {self.velocity}", True, (254, 255, 255))
        text_rect = text_surface.get_rect()
        screen.blit(text_surface, (10, 40))

        text_surface = font.render(f"rotation: {self.rotation}", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        screen.blit(text_surface, (10, 70))

        text_surface = font.render(f"angularV: {self.angularV}", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        screen.blit(text_surface, (10, 100))

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate_drag(self, dt):
        self.angularV *= pow(PLAYER_TURN_DRAG, dt)

    def move_drag(self, dt):
        self.velocity *= pow(PLAYER_DRAG, dt)

    def rotate(self, dt):
        self.rotation += self.angularV * dt
        self.rotation %= 360

    def move(self, dt):
        self.position += self.velocity * dt
        self.position = pygame.Vector2(
            self.position[0] % SCREEN_WIDTH, self.position[1] % SCREEN_HEIGHT
        )

    def shoot(self):
        if self.cd <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = (
                pygame.math.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
                + self.velocity
            )
            self.cd = PLAYER_CD

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.angularV -= PLAYER_TURN_ACCEL
        if keys[pygame.K_d]:
            self.angularV += PLAYER_TURN_ACCEL
        self.rotate_drag(dt)
        self.rotate(dt)

        if keys[pygame.K_w]:
            self.velocity += PLAYER_ACCEL * pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_s]:
            self.velocity -= PLAYER_ACCEL * pygame.Vector2(0, 1).rotate(self.rotation)
        self.move_drag(dt)
        self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
        self.cd -= dt
