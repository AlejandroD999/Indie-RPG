from src.event_handler import EventHandler
import pygame
import sys
from src import BG_IMAGE_PATH
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Idle RPG")

bg_raw = pygame.image.load(BG_IMAGE_PATH).convert()

screen_size = screen.get_size()
bg_image = pygame.transform.scale(bg_raw, screen_size)

clock = pygame.time.Clock()

event = EventHandler()
running = True
while running:

    if event.quit():
        running = False
            
    screen.blit(bg_image, (0, 0))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()