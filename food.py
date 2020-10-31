from random import  randint
import pygame
class Food:
    def __init__(self):
        self.x = randint (1,79)
        self.y = randint(1, 58)
        pass

    def draw(self, surface):
        foodsize = 10
        temp = pygame.Rect((self.x * foodsize, self.y * foodsize), (foodsize,foodsize))
        pygame.draw.rect(surface,(0,255,0), temp)
