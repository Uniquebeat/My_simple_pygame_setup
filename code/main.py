import pygame, sys, time
from setting import *
from world import World


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), pygame.SCALED) # if fullscreen : self.screen = pygame.display.set_mode((width, height), pygame.SCALED | pygame.FULLSCREEN)
        pygame.display.set_caption('Pygame setup')
        self.clock = pygame.time.Clock()
        self.world = World()

    def run(self):
        prev_time = time.time()
        while True:

            dt = time.time() - prev_time
            prev_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill('black')
            self.world.run(dt)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
