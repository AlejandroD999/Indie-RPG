import sys
import pygame
import random
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Idle RPG")

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((0, 0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()