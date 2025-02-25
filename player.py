import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        self.rotation: int = 0
        self.timer: int = 0
        return super().__init__(x, y, PLAYER_RADIUS)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, pygame.Color(
            255, 255, 255), self.triangle(), 2)

    def move(self, dt: int):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt: int):
        self.rotation += dt * PLAYER_TURN_SPEED

    def shoot(self):
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(x=0, y=1).rotate(
            self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt: int):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            
        self.timer -= dt
