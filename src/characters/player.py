from ..paths import PLAYER_STATICS
from .spritesheet import SpriteSheet
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.SCREEN_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.PLAYER_SIZE = (self.SCREEN_RECT.w // 12, self.SCREEN_RECT.h // 6)
        
        self.running_sheet = SpriteSheet(os.path.join(PLAYER_STATICS, "knight_running.png")) 
                
        self.player_actions = {
            "idle_right": [],
            "idle_left": [],
            "running_right": [],
            "running_left": []
        } 

        self.define_sprites()
        
        self.idle_counter = 0

        # Stats
        self.speed = 5
        self.dash_speed = self.speed * 2
        self.jump_height = 14


        # Running
        self.running = False
        self.running_sprite = 0
        self.running_frames_speed = self.speed / (self.speed * 5) 

        
        #  Dash & Orientation
        self.orientation = "right"

        self.dashing = False
        self.dash_duration = 10
        self.dash_timer = 0

        self.image = self.player_actions["idle_right"][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        # Jumping
        self.jumping = False
        self.GROUND = self.rect.y

        self.gravity = 0.7
        self.y_velocity = 0

    
    def define_sprites(self):
        
        idle_image = pygame.transform.scale(
                pygame.image.load(os.path.join(PLAYER_STATICS, "knight_idle.png")),
                (self.PLAYER_SIZE[0], self.PLAYER_SIZE[1]))

        self.player_actions["idle_right"].append(idle_image)
        self.player_actions["idle_left"].append(pygame.transform.flip(idle_image, True, False))

        for frame in range(len(self.running_sheet.sprite_frames)):
            player_frame = self.running_sheet.parse_sprite(f"knight_running_f{frame}")
            player_frame = pygame.transform.scale(player_frame, (self.PLAYER_SIZE[0], self.PLAYER_SIZE[1]))

            self.player_actions["running_right"].append(player_frame)
            self.player_actions["running_left"].append(pygame.transform.flip(player_frame, True, False))



    def update(self):

        keys = pygame.key.get_pressed()
        self.running = False 
        
        if self.jumping:
            self.rect.y -= self.y_velocity
            self.y_velocity -= self.gravity
            
            if self.rect.y >= self.GROUND:
                self.rect.y = self.GROUND
                self.jumping = False
                self.y_velocity = 0 

        if self.dashing:
            if self.orientation == "right":
                self.rect.x += self.dash_speed

            elif self.orientation == "left":
                self.rect.x -= self.dash_speed

            self.dash_timer -= 1

            if self.dash_timer <= 0:
                self.dashing = False         

        # Basic Movement        

        if keys[pygame.K_a]:
            self.orientation = "left"
            self.rect.x -= self.speed
            self.running = True 

        if keys[pygame.K_d]:
            self.orientation = "right"    
            self.rect.x += self.speed
            self.running = True 

        if self.running:
            self.update_running()

        else:
            if self.orientation == "right":
                self.image = self.player_actions["idle_right"][0]
                
            elif self.orientation == "left":
                self.image = self.player_actions["idle_left"][0]


        self.rect.clamp_ip(self.SCREEN_RECT)

    def update_running(self):
        self.running_sprite += self.running_frames_speed 

        if self.running_sprite >= len(self.player_actions["running_right"]):
            self.running_sprite = 0

        if self.orientation == "right":
            self.image = self.player_actions["running_right"][int(self.running_sprite)]

        elif self.orientation == "left":
            self.image = self.player_actions["running_left"][int(self.running_sprite)]



    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        

    def handle_event(self, event):
        # TODO Implement Attack

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.jumping:
                self.y_velocity = self.jump_height    
                self.jumping = True
        
            if event.key == pygame.K_LSHIFT and not self.dashing:
                self.dashing = True
                self.dash_timer = self.dash_duration

    def test(self):
        pass

