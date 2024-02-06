import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, position):
        super().__init__(40,position, (182, 0, 43))
        self.speed = 5
        
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.position[0] += self.speed
        if keys[pygame.K_UP]:
            self.position[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.position[1] += self.speed


    def update(self):
        pass