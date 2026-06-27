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

        # Jumping
        self.jumping = False
        self.GROUND = self.rect.y
                
        self.gravity = 0.8
        self.y_velocity = 0
        self.jump_height = 16 

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
        

        self.rect.clamp_ip(self.__SCREEN_RECT)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        

    def handle_event(self, event, speed):
        # TODO change into pygame.key.get_pressed() and move to update()        
        if event.key == pygame.K_SPACE and not self.jumping:
            self.y_velocity = self.jump_height    
            self.jumping = True
            print("JUMP")

        elif event.key == pygame.K_a:
            # left
            self.rect.x -= speed

        elif event.key == pygame.K_d:
            # right
            self.rect.x += speed

        elif event.key == pygame.K_s:
            # down / crouch
            print("DOWN") 