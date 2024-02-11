import pygame
from entity import Entity
from food import Food
from obstacle import Obstacle
import math

class Player(Entity):
    def __init__(self, position, fps):
        super().__init__(40,position, (182, 0, 43))
        self.speed = 100
        self.position = position
        self.gameFps = fps
        
    def move_keyboard(self, keys, screen_width, screen_height):
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:
            dx = -self.speed / self.gameFps
        if keys[pygame.K_RIGHT]:
            dx = self.speed / self.gameFps
        if keys[pygame.K_UP]:
            dy = -self.speed / self.gameFps
        if keys[pygame.K_DOWN]:
            dy = self.speed / self.gameFps


        self.position[0] += dx
        self.position[1] += dy

        self.position[0] = self.position[0] % screen_width
        self.position[1] = self.position[1] % screen_height


    def move_mouse(self, screen_width, screen_height):
        pass

    def eat(self):
        if self.speed < 500:
            self.speed +=5
        if self.size < 200:
            self.size +=2

    def hurt(self, difficulty):
        self.size = self.size // difficulty
        self.speed = self.speed // difficulty

    def check_collision(self, difficulty, other_entities, score):
            for entity in other_entities:
                distance = pygame.math.Vector2(self.position[0] - entity.position[0],
                                            self.position[1] - entity.position[1]).length()

                if distance < self.size + entity.size:
                    if isinstance(entity, Food):
                        self.eat()
                        entity.respawn()
                        score += 1

                    if isinstance(entity, Obstacle):
                        if entity.getSize() < self.size:
                            self.hurt(difficulty)
                            entity.respawn()
                        
            return score
