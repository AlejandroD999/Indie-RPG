from ..paths import ATTACKS 
from ..spritesheet import SpriteSheet
import os
import pygame

class Attack(pygame.sprite.Sprite):
    def __init__(self, attack_name, orientation, central_body_rect, width, height):
        super().__init__()
        self.full_attack_name = f"{attack_name}_{orientation}"

        self.central_body = central_body_rect
        self.attack_size = (width, height)
        self.orientation = orientation
        self.pos = [self.central_body.x, self.central_body.y]

        
        self.attack_sheet = SpriteSheet(os.path.join(ATTACKS, attack_name, f"{self.full_attack_name}.png")) 
        self.attack = {}
        self.define_sprites()

        self.frame_count = 0

        self.image = self.attack[self.full_attack_name][0] 
        self.rect = self.image.get_rect()
        self.center_attack()
        self.rect.topleft = self.pos 

    def center_attack(self):
        # TODO Fix actual image (temporary offsets)

        OFFSETS = {
                "up": (-20, -50),
                "down": (-20, 25),
                "left": (-90, -15),
                "right": (45, -15),
                }

        if self.orientation == "up":
            self.rect.midbottom = self.central_body.midtop

        elif self.orientation == "down":
            self.rect.midtop = self.central_body.midtop

        elif self.orientation == "left":
            self.rect.midright = self.central_body.midleft


        elif self.orientation == "right":
            self.rect.midleft = self.central_body.midright

        dx, dy = OFFSETS[self.orientation]
        self.pos[0] += dx
        self.pos[1] += dy

    def define_sprites(self):
        # Define frames in self.attack 
        self.attack[self.full_attack_name] = []

        for frame in range(len(self.attack_sheet.sprite_frames)):
            attack_frame = self.attack_sheet.parse_sprite(f"{self.full_attack_name}_f{frame}")
            attack_frame = pygame.transform.scale(attack_frame, self.attack_size)
            self.attack[self.full_attack_name].append(attack_frame)

    def update(self):
        if self.frame_count >= len(self.attack[self.full_attack_name]):
            self.kill()
            return True
        
        self.image = self.attack[self.full_attack_name][int(self.frame_count)]
        self.frame_count += 0.25

        return False



