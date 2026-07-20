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
        self.pos = [pos_x, pos_y]
        self.size = size
        self.orientation = "right"

        self.player = player

        # Enemy Stats
        self.hp = 20
        self.speed = 2

        self.image = pygame.image.load(os.path.join(BUGS_STATICS, "larva.png"))

        if len(self.size) > 1:
            self.image = pygame.transform.scale(self.image, self.size)

        self.original_image = self.image
        self.image_left = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.hitbox = self.rect.copy()
        self.rect.topleft = self.pos 
    
    def check_collision(self):
            
        attack = self.player.player_attack

        if attack: 
            if self.player.attacking and self.rect.colliderect(attack.rect):
                self.hp -= self.player.damage / 10 

    def persecute_player(self):

        

        if self.rect.x < self.player.rect.x:
            self.orientation = "right"
            self.rect.x += self.speed

        if self.rect.x > self.player.rect.x:
            self.orientation = "left"
            self.rect.x -= self.speed

        if self.rect.y < self.player.rect.y:
            self.rect.y += self.speed

        if self.rect.y > self.player.rect.y:
            self.rect.y -= self.speed
                 
        self.hitbox.center = self.rect.center

    def update(self):

        if self.hp <= 0:
            self.kill()

        if self.hitbox.colliderect(self.player.hitbox):

            overlap_rect = self.hitbox.clip(self.player.hitbox)

            print("Enemy", self.hitbox)
            print("Player", self.player.hitbox)
            print("Overlap", overlap_rect) 

            if overlap_rect.width < overlap_rect.height:
                if self.rect.centerx < self.player.rect.centerx:
                    self.rect.right = self.player.rect.left
                else:
                    self.rect.left = self.player.rect.right
            else:
                if self.rect.centery < self.player.rect.centery:
                    self.rect.bottom = self.player.rect.top
                else:
                    self.rect.top = self.player.rect.bottom
        


        self.check_collision()
        
        if self.orientation == "left":
            self.image = self.image_left 
        else:
            self.image = self.original_image 

        self.persecute_player()



