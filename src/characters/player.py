import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # jump
                print("JUMP")
            elif event.key == pygame.K_a:
                # left
                print("LEFT")
            elif event.key == pygame.K_d:
                # right
                print("RIGHT") 
            elif event.key == pygame.K_s:
                # down / crouch
                print("DOWN") 