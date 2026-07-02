import os
import pygame

class SpriteSheet:
    def __init__(self, file_path):

        try:
            self.sheet = pygame.image.load(file_path).convert()
        except pygame.error as e:
            print(f"Unabel to load sprite sheet image: {e}") 
            raise SystemExit(e)
        
    def image_at(self, rectangle, color_key = None):
        # Load image from rectangle
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)

        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pygame.RLEACCEL)
        
        return
    
    def images_at(self, rects, colorkey = None):

        return [self.image_at(rect, colorkey) for rect in rects]
    
    def load_strip(self, rect, image_count, colorkey = None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]

        return self.images_at(tups, colorkey)


