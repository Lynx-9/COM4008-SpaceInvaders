import pygame, sys
from player import Player 

class Game:
    def __init__(self):
        player_sprite = Player((SCREEN_WIDTH / 2,SCREEN_HEIGHT),SCREEN_WIDTH,2)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    #health and score set up
        self.lives =  3
        self.lives_image = pygame.image.load('lives.png').convert_alpha()
        self.image = pygame.transform.scale(self.lives_image, (30, 30))  # Resize the image for lives display
        self.life_x_start_pos = SCREEN_WIDTH - (self.lives_image.get_size()[0] *2 + 20)  # Position lives at top-right corner

    def draw_lives(self):
        for life in range(self.lives - 1):
            x = self.life_x_start_pos + (life * (self.image.get_size()[0] + 10))
            screen.blit(self.image, (x,8))

    def run(self):
        self.player.update()
        
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.draw_lives()
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