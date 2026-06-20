from src.event_handler import EventHandler
import os
import pygame
import sys
from src.paths import BG_IMAGE_PATH, BUG_STATICS
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Idle RPG")

bg_image = pygame.image.load(BG_IMAGE_PATH).convert()

bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

bug_image = pygame.image.load(os.path.join(BUG_STATICS, "bug-1.png")).convert_alpha() 
bug_image = pygame.transform.scale(bug_image, ((SCREEN_WIDTH / 12), (SCREEN_HEIGHT / 10)))
clock = pygame.time.Clock()


event = EventHandler()
running = True
while running:

    if event.quit():
        running = False

    screen.blit(bg_image, (0, 0))
    screen.blit(bug_image, ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - y))    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()