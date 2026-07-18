import pygame
from ..paths import UI_ELEMENTS_PATH 
import os
from ..spritesheet import SpriteSheet

class HealthBar:
    def __init__(self, surface, x, y, w, h, max_hp):
        self.surface = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.spritesheet = SpriteSheet(os.path.join(UI_ELEMENTS_PATH, "health_bar.png"))
        
        self.max_health_img = self.spritesheet.parse_sprite("max_health")
        self.current_health_img = self.spritesheet.parse_sprite("current_health")

        self.hp = max_hp
        self.max_hp = max_hp
        self.max_hp_color = "red"
    
    def update(self, new_hp):
        if self.hp <= 0:
            self.max_hp_color = "#726665"
            return

        self.hp = new_hp


    def draw(self):
        ratio = self.hp / self.max_hp

        pygame.draw.rect(self.surface, self.max_hp_color, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(self.surface, "green", (self.x, self.y, self.w * ratio, self.h))

        
