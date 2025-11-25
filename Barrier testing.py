import pygame, sys
from barriers import Barrier

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
screen.fill((30,30,30))

barrier = Barrier()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    barrier.blocks_group.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)