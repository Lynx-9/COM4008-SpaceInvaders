import pygame

class Block(pygame.sprite.Sprite): #A block class for the barriers
    def __init__(self,size,color,x,y):
        super().__init__()
        self.image = pygame.Surface([size,size])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x,y))
# Shape in the format of a list of strings
SHAPE = [
    "  XXXXXXXX  ",       
    " XXXXXXXXXX ",
    "XXXXXXXXXXXX",
    "XXXXXXXXXXXX",
    "XXXXXXXXXXXX",
    "XXX"   "XXX",
    "XX"     "XX",]