import pygame
from ..paths import UI_ELEMENTS_PATH 
import os
from ..spritesheet import SpriteSheet

# TODO Make healthbar disapper when entity dead

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, w, h, max_hp, entity = None):
        super().__init__()
        self.surface = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.entity = entity
        
        self.spritesheet = SpriteSheet(os.path.join(UI_ELEMENTS_PATH, "health_bar.png"))
        
        self.max_health_img = self.spritesheet.parse_sprite("max_health")
        self.current_health_img = self.spritesheet.parse_sprite("current_health")

        self.hp = max_hp
        self.max_hp = max_hp
        self.max_hp_color = "red"
    
    def update(self, new_hp):
        self.hp = max(new_hp, 0)

        if self.entity:
            self.x = self.entity.rect.centerx - self.w // 2
            self.y = self.entity.rect.top - 10

        if self.hp <= 0:
            self.max_hp_color = "#726665"
            return
        


    def draw(self, camera=None):
        ratio = self.hp / self.max_hp

        if camera:
            self.x = self.x - camera.offset.x
            self.y = self.y - camera.offset.y

        pygame.draw.rect(self.surface, self.max_hp_color, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(self.surface, "green", (self.x, self.y, self.w * ratio, self.h))

        
