import pygame, sys
from player import Player  

class Game:
    def __init__(self):
        player_sprite = Player((SCREEN_WIDTH / 2,SCREEN_HEIGHT),SCREEN_WIDTH,2)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)
        # update all sprites and draws all sprites

if __name__ == '__main__':
    pygame.init()
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 600
    screen = pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH])
    clock = pygame.time.Clock() # to slow down the speed of movement
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill([0,0,0]) # black background
        game.run()
        
        pygame.display.flip()
        clock.tick(60)