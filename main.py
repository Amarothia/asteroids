# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# then importing all from constants.py, player.py, asteroid.py, asteroidfield.py, shot.py
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Player.containers = (group_a, group_b)
    Player.containers = (updatable,drawable) # this should add the player object to the groups
    Asteroid.containers = (asteroids,updatable,drawable) # this ensures every asteroid class object created is in these groups
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable) # shots is crucial in this as without it, there are no shot objects
    player_1 = Player(x,y) # since conatiners exist, player_1 will be added to them automatically
    asteroid_field = AsteroidField()
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: # infinite while loop, break can escape it if desired
        for event in pygame.event.get(): # this is a listener
            if event.type == pygame.QUIT: # this is checking for program close events, like the X on a window
                return # this allows the program to exit out of the main() entirely
        pygame.Surface.fill(screen, color="black")
        updatable.update(delta_time) # changed player_1 to drawable
        for asteroid in asteroids:
            if player_1.checkForCollision(asteroid):
                exit("Game over!")
            for shot in shots:
                if shot.checkForCollision(asteroid):
                    shot.kill()
                    asteroid.kill()
        # drawable.draw(screen) # changed player_1 to updatable
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
