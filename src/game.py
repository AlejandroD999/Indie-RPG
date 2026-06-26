from .characters.player import Player
from .config import SCREEN_WIDTH, SCREEN_HEIGHT
from .paths import BG_IMAGE_PATH, BUG_STATICS
import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT) 
        self.screen = pygame.display.set_mode(self.screen_size)        
        self.clock = pygame.time.Clock()
        self.__bg_image = pygame.transform.scale(pygame.image.load(BG_IMAGE_PATH), self.screen_size).convert()
        self.running = True
        pygame.display.set_caption("Ethereal RPG")
                
        self.player = Player(
            10,
            (self.screen_size[1] - (self.screen_size[1] / 4))) 
        
    def handle_events(self):
        ''' Handle all game events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                self.player.handle_event(event, 5)
    
    def draw(self):
        ''' Place elements into screen '''
        self.screen.blit(self.__bg_image, (0, 0))
        self.player.draw(self.screen)        
        pygame.display.flip()

    def run(self):
        
        while self.running:
            self.handle_events()

            self.player.update()

            self.draw()
            self.clock.tick(60)            
        
        pygame.quit()
        sys.exit()