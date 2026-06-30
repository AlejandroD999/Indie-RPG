import pygame
import sys

class MainMenu():
    def __init__(self, app):
        self.app = app

        self.play_rect = pygame.Rect(50, 10, 50, 100)

    def mouse_collision(self, mouse_pos, object):
        return object.collidepoint(mouse_pos)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.mouse_collision(mouse_pos, self.play_rect):
                    self.app.change_screen(self.app.game)
                    return
    def update(self):
        pass

    def draw(self):
        self.app.screen.fill((0, 0, 0))
        
        pygame.draw.rect(self.app.screen, (255, 0, 0), self.play_rect)

        pygame.display.flip()
