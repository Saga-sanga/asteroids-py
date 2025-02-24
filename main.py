# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    dt = 0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
