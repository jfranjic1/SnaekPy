import  pygame
import snaek
import food

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
NAN = (0,0)
ADD = (69,69)
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
        temp = pygame.Rect((0,0),(800,10))
        pygame.draw.rect(surface, (0, 0, 0), temp)
        temp = pygame.Rect((0, 590), (800, 10))
        pygame.draw.rect(surface, (0, 0, 0), temp)
        temp = pygame.Rect((0, 0), (10, 800))
        pygame.draw.rect(surface, (0, 0, 0), temp)
        temp = pygame.Rect((790, 0), (10, 800))
        pygame.draw.rect(surface, (0, 0, 0), temp)
        s = snaek.Snaek()
        f= food.Food()
        f.draw(surface)
        while(1):
            clock.tick(20)
            s.changeDirection(self.keypress())
            try:
                s.move(surface)
            except:
                self.gameOver(surface,s.counter)
            if(s.ateFood(f.x,f.y)):
                s.addItem()
                while not s.foodValid(f.x,f.y):
                    f= food.Food()
                    if(s.foodValid(f.x, f.y)):
                        f.draw(surface)
                        break

            screen.blit(surface,(0,0))
            pygame.display.update()

    def keypress(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: return UP
                if event.key == pygame.K_DOWN: return DOWN
                if event.key == pygame.K_LEFT: return LEFT
                if event.key == pygame.K_RIGHT: return RIGHT
                if event.key == pygame.K_SPACE: return ADD
                return NAN
        return NAN

    def gameOver(self,surface,score):
        temp = pygame.Rect((0,0), (800,600))
        pygame.draw.rect(surface,(100,100,100), temp)
        text1 = "gg unlucky"
        text2 = "Your score is: " + str(score)
        font_type = pygame.font.get_default_font()
        color = (255,0, 0)
        size = 60
        text1 = str(text1)
        font = pygame.font.Font(font_type, size)
        text1 = font.render(text1, True, color)
        text2 = str(text2)
        text2 = font.render(text2, True, color)
        surface.blit(text1, (230, 200))
        surface.blit(text2, (160, 300))
