import pygame

class Block(pygame.sprite.Sprite): #A block class for the barriers
    def __init__(self,x,y):
        super().__init__() #Initialize the sprite
        self.image = pygame.Surface((10,10)) #Create a 3x3 pixel block
        self.image.fill((0,225,0))
        self.rect = self.image.get_rect(topleft = (x,y)) #Set position of blocks
# Shape in the format of a list of strings
shape = [
    "   XXXXXXXXXXXXXXX  ",       
    "  XXXXXXXXXXXXXXXXX ",
    " XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXX",
    " XXXXXXXXXXXXXXXXXXX",
    " XXXXXX       XXXXXX",
    " XXX             XXX",]
shape = [list(row) for row in shape] #Convert each string to a list of characters

class Barrier:
    def __init__(self, x, y): #A barrier class to create barriers from blocks
        self.blocks_group = pygame.sprite.Group() #Group to hold all the blocks
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col] == "X": #If the character is an X, create a block
                    x_pos = x + col * 3 #calculate x and y position on screen
                    y_pos = y + row * 3
                    block = Block(x_pos,y_pos) 
                    self.blocks_group.add(block) #Add block to the group
