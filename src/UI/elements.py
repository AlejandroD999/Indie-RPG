import pygame

class Button:
    def __init__(self, image, pos):
        self.image = image
        self.rect = self.image.get_rect(topleft=(int(pos[0]), int(pos[1])))
        self.pos = pos

    def get_img(self):
        return self.image
    
    def get_rect(self):
        return self.rect
    
    def get_pos(self):
        return self.pos 
