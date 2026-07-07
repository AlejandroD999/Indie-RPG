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
        
        self.data_path = self.filename.replace('png', 'json')
        self.data = self.load_meta_data(self.data_path)
        self.sprite_frames = self.data["frames"]
        

    def load_meta_data(self, path: str):

        try:
            with open(path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Failed to load Meta Data: {f}")
            return None
            
        return data

        
    def get_sprite(self, x, y, w, h):
        # Load image from rectangle

        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sheet, (0, 0), (x, y, w, h))
        
        return sprite


    def parse_sprite(self, name):
        sprite = self.sprite_frames[name]['frame']
        
        x,y,w,h = sprite['x'], sprite['y'], sprite['w'], sprite['h']
        img = self.get_sprite(x, y, w, h)

        return img


