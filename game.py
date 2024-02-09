import pygame
from player import Player
from food import Food
from obstacle import Obstacle

class Game:
    def __init__(self, difficulty):
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = 60
        self.difficulty = difficulty

        self.player_position = [self.width // 2, self.height // 2]
        self.player = Player(self.player_position, self.fps)
        self.clock = pygame.time.Clock()


        self.entities = [Food() for _ in range([5, 3, 2][difficulty - 2])]
        self.entities.extend([Obstacle() for _ in range([2, 3, 4][difficulty - 2])])


    def mainLoop(self):
        game_started = True
        while game_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_started = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            self.player.check_collision(self.difficulty, self.entities)

            self.screen.fill((255, 255, 255))
            self.player.draw(self.screen)
            for i in self.entities:
                i.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(self.fps)

        pygame.quit()