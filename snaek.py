import numpy
import sys
import pygame

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
NAN = (0,0)
class Snaek:
    def __init__(self):
        self.lenght = 1
        self.direction = RIGHT
        self.positions = [(50, 50, self.direction), (50,51, RIGHT), (50,52, RIGHT),(50, 53, self.direction), (50,54, RIGHT), (50,55, RIGHT)]
        self.color = (17, 24, 47)
        self.last = (50,55, RIGHT)
        self.lastdirection = self.direction
    def move(self,surface):
        self.positions.insert(0, (self.positions[0][0] + self.direction[0], self.positions[0][1] + self.direction[1], self.direction))
        self.last = self.positions.pop()
        for i in range (0,10):
            self.draw(surface, i)
    def changeDirection(self, direction):
        if (direction == NAN): return;
        if((self.direction == RIGHT) and (direction == LEFT)):
            return
        if ((self.direction == LEFT) and (direction == RIGHT)):
            return
        if ((self.direction == UP) and (direction == DOWN)):
            return
        if (self.direction == DOWN) and (direction == UP):
            return
        self.direction = direction

    def draw(self, surface, i):
        snakesize = 10
        print(self.last)
        self.lastdirection = self.last[2]
        if(self.direction == RIGHT):
            temp = pygame.Rect(((self.positions[0][0] + i/10)*snakesize,self.positions[0][1]*snakesize),(snakesize/10,snakesize))
            pygame.draw.rect(surface,self.color, temp)
        if (self.direction == LEFT):
            temp = pygame.Rect(((self.positions[0][0]+ 1 - (i+1) / 10) * snakesize, self.positions[0][1] * snakesize),(snakesize / 10, snakesize))
            pygame.draw.rect(surface, self.color, temp)
        if (self.direction == UP):
            temp = pygame.Rect(((self.positions[0][0]) * snakesize, (self.positions[0][1] + 1 - (i+1) / 10 )* snakesize),(snakesize , snakesize / 10))
            pygame.draw.rect(surface, self.color, temp)
        if (self.direction == DOWN):
            temp = pygame.Rect(((self.positions[0][0]) * snakesize, (self.positions[0][1] + i / 10 )* snakesize),(snakesize , snakesize / 10))
            pygame.draw.rect(surface, self.color, temp)

        if (self.lastdirection == RIGHT):
            temp = pygame.Rect(((self.last[0] + i / 10) * snakesize, self.last[1] * snakesize),(snakesize / 10, snakesize))
            pygame.draw.rect(surface, (100, 100, 100), temp)
        if (self.lastdirection == LEFT):
            temp = pygame.Rect(((self.last[0] +1 - (i+1) / 10) * snakesize, self.last[1] * snakesize),(snakesize / 10, snakesize))
            pygame.draw.rect(surface, (100, 100, 100), temp)
        if (self.lastdirection == UP):
            temp = pygame.Rect(((self.last[0]) * snakesize, (self.last[1] +1 - (i+1)/ 10) * snakesize),
                               (snakesize, snakesize / 10))
            pygame.draw.rect(surface, (100, 100, 100), temp)
        if (self.lastdirection == DOWN):
            temp = pygame.Rect((self.last[0] * snakesize, (self.last[1] + i / 10) * snakesize),(snakesize, snakesize / 10))
            pygame.draw.rect(surface, (100, 100, 100), temp)



