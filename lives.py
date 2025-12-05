import pygame

class Lives(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load('lives.png').convert_alpha()
        self.live_x_start_pos = SCREEN_WIDTH - (self.live_surf.get_size()[0] *2 + 20)  # Position lives at top-right corner
        self.lives = 3  # Starting number of lives
        
    def draw_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            screen.blit(self.live_surf(x,8))

    def update(self):
        self.draw_lives()

        
