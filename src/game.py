from .paths import BG_IMAGE_PATH, BUG_STATICS
import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen_size = (900, 500)
        self.screen = pygame.display.set_mode(self.screen_size)        
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Ethereal RPG")
        self.__bg_image = pygame.transform.scale(pygame.image.load(BG_IMAGE_PATH), self.screen_size).convert()

    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.blit(self.__bg_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)            
        
        pygame.quit()
        sys.exit()