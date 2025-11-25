import pygame

class Block(pygame.sprite.Sprite): #A block class for the barriers
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((3,3))
        self.image.fill((0,225,0))
        self.rect = self.image.get_rect(topleft = (x,y))
# Shape in the format of a list of strings
shape = [
    "  XXXXXXXX  ",       
    " XXXXXXXXXX ",
    "XXXXXXXXXXXX",
    "XXX      XXX",
    "XX        XX",]
shape = [list(row) for row in shape] #Convert each string to a list of characters

class Barrier:
    def __init__(self):
        self.blocks_group = pygame.sprite.Group()
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col] == "X":
                    x = col * 3
                    y = row * 3
                    block = Block(x,y)
                    self.blocks_group.add(block) #Add block to the group
