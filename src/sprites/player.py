from ..paths import PLAYER_STATICS
from ..spritesheet import SpriteSheet
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT
from .attack import Attack
import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, camera, pos_x, pos_y):
        super().__init__()
        self.SCREEN_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.PLAYER_SIZE = (self.SCREEN_RECT.w // 20, self.SCREEN_RECT.h // 10)
        self.running_sheet = SpriteSheet(os.path.join(PLAYER_STATICS, "knight_running.png")) 
        
        self.camera = camera

        self.player_actions = {
            "idle_right": [],
            "idle_left": [],
            "running_right": [],
            "running_left": []
        } 
        self.define_sprites()

        # Counters
        self.idle_counter = 0

        # Stats
        self.speed = 5
        self.dash_speed = self.speed * 2


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

        # Attack
        self.attacking = False
   
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
        self.speed = 5


        if self.attacking:
            self.speed /= 2 

        # Attacking
        if self.attacking:
            # TODO turn player idle or attack animations
            if self.player_attack.update():
                self.attacking = False
            
        # Dash
        if self.dashing:
            # TODO Dash animations 
            if self.orientation == "up":
                self.rect.y -= self.dash_speed

            if self.orientation == "right":
                self.rect.x += self.dash_speed

            if self.orientation == "down":
                self.rect.y += self.dash_speed

            if self.orientation == "left":
                self.rect.x -= self.dash_speed

            self.dash_timer -= 1

            if self.dash_timer <= 0:
                self.dashing = False         


        # Basic Movement        
        if keys[pygame.K_w]:
            self.orientation = "up"
            self.rect.y -= self.speed
            self.running = True

        if keys[pygame.K_s]:
            self.orientation = "down"
            self.rect.y += self.speed
            self.running = True

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
            # TODO Idle up & down

            if self.orientation == "right":
                self.image = self.player_actions["idle_right"][0]
                
            elif self.orientation == "left":
                self.image = self.player_actions["idle_left"][0]


    def update_running(self):
        self.running_sprite += self.running_frames_speed 

        if self.running_sprite >= len(self.player_actions["running_right"]):
            self.running_sprite = 0
        
        if self.orientation == "up" or self.orientation == "down":
            # Placeholder until up and down animations
            self.image = self.player_actions["running_right"][int(self.running_sprite)]
            return
        self.image = self.player_actions[f"running_{self.orientation}"][int(self.running_sprite)]


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not self.dashing:
                self.dashing = True
                self.dash_timer = self.dash_duration

            if event.key == pygame.K_k and not self.attacking:
                self.player_attack = Attack(
                        "slash",
                        self.orientation,
                        self.rect,
                        self.PLAYER_SIZE[0] * 2,
                        self.PLAYER_SIZE[1] * 2
                        ) 
                self.camera.add(self.player_attack)
                self.attacking = True

    def test(self):
        pass

