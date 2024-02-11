import pygame
from player import Player
from food import Food
from obstacle import Obstacle

class Game:
    def __init__(self, difficulty, mode):
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = 60
        self.difficulty = difficulty
        self.mode = mode
        self.font = pygame.font.Font(None, 24)

        self.score = 0

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
            if self.mode == "keyboard":
                self.player.move_keyboard(keys, self.width, self.height)
            else :
                self.player.move_mouse(self.width, self.height)

            self.score = self.player.check_collision(self.difficulty, self.entities, self.score)

            self.screen.fill((255, 255, 255))
            self.player.draw(self.screen)
            for i in self.entities:
                i.draw(self.screen)

           
            self.create_scorboard()
            pygame.display.flip()

            self.clock.tick(self.fps)
            if keys[pygame.K_q]:
                game_started = False

        pygame.quit()

    def create_scorboard(self):
        text_score = self.font.render("Score : " + str(self.score), 1, (0, 0, 0))
        self.screen.blit(text_score, (20, 20))

        text_speed = self.font.render("Speed : " + str(self.player.speed), 1, (0, 0, 0))
        self.screen.blit(text_speed, (20, 40))

        text_size = self.font.render("Size : " + str(self.player.size), 1, (0, 0, 0))
        self.screen.blit(text_size, (20, 60))

        string_difficulty = ""

        if self.difficulty == 2:
            string_difficulty = "Easy"
        elif self.difficulty == 3:
            string_difficulty = "Medium"
        elif self.difficulty ==4:
            string_difficulty = "Hard"

        text_difficulty = self.font.render("Difficulty : " + string_difficulty, 1, (0, 0, 0))
        self.screen.blit(text_difficulty, (20, 80))