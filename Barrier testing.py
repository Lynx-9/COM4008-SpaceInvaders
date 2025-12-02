import pygame, sys
from barriers import Barrier

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
screen.fill((30,30,30))

barrier1 = Barrier(450,500)
barrier2 = Barrier(300,500)
barrier3 = Barrier(150,500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    #this creates multiple barriers on screen.
    
    barrier1.blocks_group.draw(screen)
    barrier2.blocks_group.draw(screen)
    barrier3.blocks_group.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

sys.exit()