from ..paths import BUG_STATICS
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.__SCREEN_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.join(BUG_STATICS, "bug-1.png")).convert_alpha())
        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        # Stats
        self.speed = 5
        self.jump_height = 14

        # Jumping
        self.jumping = False
        self.GROUND = self.rect.y
                
        self.gravity = 0.7
        self.y_velocity = 0
        
        self.standing_surface = None
        self.jumping_surface = None

    def update(self):

        if self.jumping:
            self.rect.y -= self.y_velocity
            self.y_velocity -= self.gravity
            
            if self.rect.y >= self.GROUND:
                self.rect.y = self.GROUND
                self.jumping = False
                self.y_velocity = 0 
        
        self.handle_event()
        self.rect.clamp_ip(self.__SCREEN_RECT)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        

    def handle_event(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.jumping:
            self.y_velocity = self.jump_height    
            self.jumping = True
            print("JUMP")

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            
        if keys[pygame.K_d]:
            self.rect.x += self.speed