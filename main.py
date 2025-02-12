# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# then importing all from constants.py
from constants import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: # infinite while loop, break can escape it if desired
        for event in pygame.event.get(): # this is a listener
            if event.type == pygame.QUIT: # this is checking for program close events, like the X on a window
                return # this allows the program to exit out of the main() entirely
        pygame.Surface.fill(screen, color="black")
        pygame.display.flip()
        delta_time = game_clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
