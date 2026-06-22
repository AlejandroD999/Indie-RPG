import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def event_handler(self):
        for event in pygame.event.get():
            if event.type() == pygame.QUIT:
                return True
            elif event.type() == pygame.KEYDOWN:
                if pygame.key == "K_SPACE":
                    # jump
                    print("JUMP")
                elif pygame.key == "K_a":
                    # left
                    print("LEFT")
                elif pygame.key == "K_d":
                    # right
                    print("RIGHT") 
                elif pygame.key == "K_s":
                    # down / crouch
                    print("DOWN") 