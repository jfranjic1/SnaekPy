import  pygame
import snaek

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
NAN = (0,0)
class Game:
    def __init__(self):
        print("got called")

    def play(self):
        pygame.init()
        x = 800
        y = 600
        squareSize = 10
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((x, y), 0, 32)
        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()
        temp = pygame.Rect((0,0),(800,600))
        pygame.draw.rect(surface,(100,100,100),temp)

        s = snaek.Snaek()

        while(1):
            clock.tick(20)
            s.changeDirection(self.keypress())
            s.move(surface)
            screen.blit(surface,(0,0))
            pygame.display.update()

    def keypress(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: return UP
                if event.key == pygame.K_DOWN: return DOWN
                if event.key == pygame.K_LEFT: return LEFT
                if event.key == pygame.K_RIGHT: return RIGHT
                return NAN

        return NAN