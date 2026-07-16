import pygame
import os
from ..paths import BUGS_STATICS

class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, pos_x, pos_y, size):
        """
        player: Class
        pos_x, pos_y: int
        size: tuple -> (width, height)
        """
        super().__init__()

        self.size = size
        self.player = player

        # Enemy Stats
        self.health = 20

        self.image = (pygame.image.load(os.path.join(BUGS_STATICS, "larva.png")))

        if len(self.size) > 1:
            self.image = pygame.transform.scale(self.image, self.size)

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    
    def check_collision(self):
        attack = self.player.player_attack

        if attack: 
            if self.player.attacking and self.rect.colliderect(attack.rect):
                self.health -= self.player.damage / 10 

    def persecute_player(self):
        pass

    def update(self):
        if self.health <= 0:
            self.kill()
        print(self.health)
        self.check_collision()
