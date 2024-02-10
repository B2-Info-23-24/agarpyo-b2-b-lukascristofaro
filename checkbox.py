import pygame

class Checkbox:
    def __init__(self, x, y, size, checked=False, color=(200, 200, 200), check_color=(0, 0, 0), border_color=(0, 0, 0), border_width=2, text=""):
        self.rect = pygame.Rect(x, y, size, size)

        self.checked = checked
        self.color = color
        self.check_color = check_color
        self.border_color = border_color


        self.border_width = border_width
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
        pygame.draw.rect(screen, self.color, self.rect)


        if self.checked:
            pygame.draw.line(screen, self.check_color, self.rect.topleft, self.rect.bottomright, 3)
            pygame.draw.line(screen, self.check_color, self.rect.topright, self.rect.bottomleft, 3)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, (0, 0, 0))


        text_rect = text.get_rect(midleft=(self.rect.right + 10, self.rect.centery))
        screen.blit(text, text_rect)

    def toggle(self):
        self.checked = not self.checked

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)