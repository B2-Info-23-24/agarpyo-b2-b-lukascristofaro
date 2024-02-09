from entity import Entity
import pygame
import random


class Obstacle(Entity):
    def __init__(self):
        self.size = self.random_size()
        self.coordinate = self.randomCoordinate()
        super().__init__(self.size, self.coordinate, (54, 115, 225))

    def getSize(self):
        return self.size
    
    def random_size(self):
        return random.randint(40, 150)
    
    def randomCoordinate(self):
        x = random.randint(0, 1280)
        y = random.randint(0, 720)
        return (x, y)
    def respawn(self):
        self.size = self.random_size()
        self.position = self.randomCoordinate()
