import pygame
import sys
from button import Button

class Menu:
    def __init__(self):
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.mouseButton = Button(500, 280, 250, 50, "Play with mouse")
        self.keyboardButton = Button(500, 350, 250, 50, "Play with Keyboard")
        self.quitButton = Button(500, 420, 250, 50, "Quit")

        self.easyCheckbox = pygame.Rect(self.width // 2 - 100, 50, 30, 30)
        self.mediumCheckbox = pygame.Rect(self.width // 2, 50, 30, 30)
        self.hardCheckbox = pygame.Rect(self.width // 2 + 100, 50, 30, 30)

        self.checked_easy = True
        self.checked_medium = False
        self.checked_hard = False

    def run(self):
        clock = pygame.time.Clock()
        
        param = ["", 2]
        menu_start = True
        while menu_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.mouseButton.is_clicked(pos):
                        param[0] = "mouse"
                        menu_start = False

                    elif self.keyboardButton.is_clicked(pos):
                        param[0] = "keyboard"
                        menu_start = False

                    elif self.quitButton.is_clicked(pos):
                        param[0] = "quit"
                        menu_start = False

                    elif self.easyCheckbox.collidepoint(pos):
                        self.checked_easy = True
                        self.checked_medium = False
                        self.checked_hard = False
                        param[1] = 2

                    elif self.mediumCheckbox.collidepoint(pos):
                        param[1] = 3
                        self.checked_easy = False
                        self.checked_medium = True
                        self.checked_hard = False

                    elif self.hardCheckbox.collidepoint(pos):
                        param[1] = 4
                        self.checked_medium = False
                        self.checked_easy = False
                        self.checked_hard = True


                if param[0] != "":
                    return param
                
            self.screen.fill((255, 255, 255))
            self.draw_buttons()
            clock.tick(60)

    def draw_buttons(self):
        self.mouseButton.draw(self.screen)
        self.keyboardButton.draw(self.screen)
        self.quitButton.draw(self.screen)

        pygame.draw.rect(self.screen, (255, 0, 0) if self.checked_easy else (0, 0, 255), self.easyCheckbox)
        pygame.draw.rect(self.screen, (255, 0, 0) if self.checked_medium else (0, 0, 255), self.mediumCheckbox)
        pygame.draw.rect(self.screen, (255, 0, 0) if self.checked_hard else (0, 0, 255), self.hardCheckbox)

        pygame.display.flip()

    def handle_button_click(self, message):
        print(message)