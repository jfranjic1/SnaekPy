import  pygame

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

        for i in range(0, int(x)):
            for j in range(0, int(y)):
                if(i+j) % 2 == 0:
                    temp = pygame.Rect((i * squareSize, j * squareSize), (x, y))
                    pygame.draw.rect(surface, (100, 100, 100), temp)
                else:
                    temp = pygame.Rect((i * squareSize, j * squareSize), (x, y))
                    pygame.draw.rect(surface, (200, 200, 200), temp)

        while(1):
            clock.tick(10)
            screen.blit(surface,(0,0))
            pygame.display.update()
