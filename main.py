import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from random import uniform


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    astroidField = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000
        screen.fill(pygame.Color(0, 0, 0))
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.is_colliding(player):
                print("Game over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if not asteroid.is_colliding(shot):
                    continue
                asteroid.kill()
                shot.kill()
                if asteroid.radius < ASTEROID_MIN_RADIUS:
                    continue
                angle = uniform(20, 50)
                v1 = asteroid.velocity.rotate(angle)
                v2 = asteroid.velocity.rotate(-angle)
                new_radius = asteroid.radius - ASTEROID_MIN_RADIUS
                a1 = Asteroid(asteroid.position.x,
                              asteroid.position.y, new_radius)
                a2 = Asteroid(asteroid.position.x,
                              asteroid.position.y, new_radius)
                a1.velocity = v1 * 1.2
                a2.velocity = v2 * 1.2

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return
                case _:
                    pass

        pygame.display.flip()


if __name__ == '__main__':
    main()
