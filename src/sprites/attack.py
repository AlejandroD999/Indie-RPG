from ..paths import ATTACKS 
from ..spritesheet import SpriteSheet
import os
import pygame

class Attack(pygame.sprite.Sprite):
    def __init__(self, attack_name, orientation, pos_x, pos_y):
        super().__init__()
        self.full_attack_name = f"{attack_name}_{orientation}"
        self._orientation = orientation

        self.attack_sheet = SpriteSheet(os.path.join(ATTACKS, attack_name, f"{self.full_attack_name}.png")) 

        self.attack = {}
        self.define_sprites()

        self.frame_count = 0

        self.image = self.attack[self.full_attack_name][0] 
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
    
    def define_sprites(self):
        # Define frames in self.attack 
        self.attack[self.full_attack_name] = []

        for frame in range(len(self.attack_sheet.sprite_frames)):
            attack_frame = self.attack_sheet.parse_sprite(f"{self.full_attack_name}_f{frame}")

            self.attack[self.full_attack_name].append(attack_frame)

    def update(self):
        if self.frame_count >= len(self.attack[self.full_attack_name]):
            self.kill()
            return True

        self.image = self.attack[self.full_attack_name][int(self.frame_count)]
        self.frame_count += 0.5

        return False



