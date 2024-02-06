import pygame
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))

           # Créer une instance de joueur
        player_size = (50, 50)
        player_position = [self.width // 2, self.height // 2]
        self.player = Player(player_position)
        self.clock = pygame.time.Clock()


    def mainLoop(self):
        game_started = True
        while game_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_started = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.screen.fill((255, 255, 255))
            self.player.draw(self.screen)


            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

game = Game()
game.mainLoop()