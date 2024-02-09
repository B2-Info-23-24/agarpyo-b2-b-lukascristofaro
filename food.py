import pygame
from entity import Entity
import random
from abc import ABC, abstractmethod


class Food(Entity):
    def __init__(self):
        super().__init__(20, self.randomCoordinate(), (244, 211, 0))

    def respawn(self):
        self.position = self.randomCoordinate()

    def randomCoordinate(self):
        x = random.randint(0, 1280)
        y = random.randint(0, 720)
        return (x, y)
    
