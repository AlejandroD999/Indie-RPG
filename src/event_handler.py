import pygame
# Event Handling to be moved into player / character class
    # Make it a func for event
class EventHandler:
    def __init__(self):
        pass

    def quit(self):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Space")                            
        except pygame.error as e:
            print(f"Event Error: {e}")
        
        return False
    
    def move_up(self, sprite_y, speed: 5):
        # Transform into translate later (up, down, left, right)
        try:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key == "K_SPACE":
                        return sprite_y + speed
        except pygame.error as e:
            print(f"Event error: {e}")
        
        return 0
                