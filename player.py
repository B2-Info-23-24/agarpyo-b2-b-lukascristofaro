import pygame
from entity import Entity
from food import Food
from obstacle import Obstacle

class Player(Entity):
    def __init__(self, position, fps):
        super().__init__(40,position, (182, 0, 43))
        self.speed = 100
        self.position = position
        self.gameFps = fps
        
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed / self.gameFps
        if keys[pygame.K_RIGHT]:
            self.position[0] += self.speed / self.gameFps
        if keys[pygame.K_UP]:
            self.position[1] -= self.speed / self.gameFps
        if keys[pygame.K_DOWN]:
            self.position[1] += self.speed / self.gameFps

    def eat(self):
        if self.speed < 500:
            self.speed +=5
        if self.size < 200:
            self.size +=2

    def hurt(self, difficulty):
        self.size = self.size // difficulty
        self.speed = self.speed // difficulty

    def check_collision(self, difficulty, other_entities):
            for entity in other_entities:
                distance = pygame.math.Vector2(self.position[0] - entity.position[0],
                                            self.position[1] - entity.position[1]).length()

                if distance < self.size + entity.size:
                    if isinstance(entity, Food):
                        self.eat()
                        entity.respawn()

                    if isinstance(entity, Obstacle):
                        if entity.getSize() < self.size:
                            self.hurt(difficulty)
                            entity.respawn()
                        

