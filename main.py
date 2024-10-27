import pygame
import sys
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
        
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    player_ship = Player(x,y)
    asteroidfield = AsteroidField()

    #game loop
    while 1 == 1:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for each in drawable:
            each.draw(screen)
        for each in updatable:
            each.update(dt)
        for each in asteroids:
            if each.collision(player_ship):
                print("Game over!")
                sys.exit()

        pygame.display.flip()

    
if __name__ == "__main__":
    main()