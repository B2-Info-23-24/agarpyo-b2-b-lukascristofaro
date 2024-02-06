from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color

    @abstractmethod
    def update(self):
        pass
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position[0], self.position[1]), 25)

