import numpy
import sys

UP = (0,1)
DOWN = (0,-1)
LEFT = (-1,0)
RIGHT = (0,1)

class Snaek:
    def __init__(self):
        self.lenght = 1
        self.positions = [(0, 2)]
        self.positions.insert(0,(3,4))
        self.direction = RIGHT
        self.color = (17, 24, 47)
    def move(self):
        self.positions.insert(0,(self.positions[0]+self.direction[0], self.positions[1]+self.direction[1]))
        self.positions.pop()


