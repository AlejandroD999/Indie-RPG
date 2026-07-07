import json
import os
import pygame

class SpriteSheet:
    def __init__(self, filename):
        self.filename = filename

        try:
            self.sheet = pygame.image.load(self.filename).convert()
        except pygame.error as e:
            print(f"Unable to load sprite sheet image: {e}") 
            raise SystemExit(e)
        
        self.meta_data_path = self.filename.replace('png', 'json')
        self.meta_data = self.load_meta_data(self.meta_data_path)

    def load_meta_data(self, meta_data: str):

        try:
            with open(meta_data, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Failed to load Meta Data: {f}")
            return None
            
        return data

        
    def get_sprite(self, rectangle, color_key = None):
        # Load image from rectangle
        # Rect -> x,y,w,h

        rect = pygame.Rect(rectangle)
        sprite = pygame.Surface(rect.size).convert()
        sprite.blit(self.sheet, (0, 0), rect)

        if color_key is not None:
            if color_key == -1:
                color_key = sprite.get_at((0, 0))
            sprite.set_colorkey(color_key)
        
        return sprite

