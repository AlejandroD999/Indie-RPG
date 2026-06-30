import pygame
import sys

class MainMenu():
    def __init__(self):
        self.running = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.running:

            self.handle_events()
            self.update()
            self.draw()


        pygame.quit
        sys.exit
