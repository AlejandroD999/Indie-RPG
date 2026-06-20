import sys
import pygame
import random
from src import BG_IMAGE_PATH

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Idle RPG")

bg_raw = pygame.image.load(BG_IMAGE_PATH).convert()

screen_size = screen.get_size()
bg_image = pygame.transform.scale(bg_raw, screen_size)

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.blit(bg_image, (0, 0))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()