import numpy
import sys
import food
import pygame

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
NAN = (0,0)
ADD = (69,69)
class Snaek:
    def __init__(self):
        self.lenght = 1
        self.direction = RIGHT
        self.positions = [(50, 50, self.direction), (50,51, RIGHT), (50,52, RIGHT)]#,(50, 53, self.direction), (50,54, RIGHT), (50,55, RIGHT)]
        self.color = (17, 24, 47)
        self.last = (50,52, RIGHT)
        self.counter = 3
        self.lastdirection = self.direction
    def move(self,surface):
        if(self.ateIteself(self.positions[0][0] + self.direction[0], self.positions[0][1] + self.direction[1])):raise
        if (self.offLimit(self.positions[0][0] + self.direction[0], self.positions[0][1] + self.direction[1])): raise
        self.positions.insert(0, (self.positions[0][0] + self.direction[0], self.positions[0][1] + self.direction[1], self.direction))
        self.last = self.positions.pop()
        for i in range (0,10):
            self.draw(surface, i)
    def changeDirection(self, direction):
        if (direction == NAN or direction == ADD): return;
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

            temp = pygame.Rect(((self.positions[0][0]) * snakesize, (self.positions[0][1] + 1 - (i+1) / 10 )* snakesize),(snakesize , snakesize / 10))
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
    def addItem(self):
        self.positions.insert(1,self.positions[0])

    def ateFood(self, x, y):
        if(self.positions[0][0] == x and self.positions[0][1] == y):
            self.counter+=1
            return True

        return False

    def foodValid(self, x, y):
        for temp in self.positions:
            if (temp[0] == x and temp[1] == y): return False
            return True

    def ateIteself(self, x, y):
        snakesize = 10
        print("called")
        for temp in self.positions:
            if(temp[0] == x and temp[1] == y): return True
        return False

    def offLimit(self, x,y):
        if(x<1 or x>79 or y<1 or y > 58):return True
        return False



