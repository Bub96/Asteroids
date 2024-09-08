import pygame
from constants import *
from player import *

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    player1 =Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = Clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()