import pygame

class EventHandler:
    def __init__(self):
        pass

    def quit(self):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                
        except pygame.error as e:
            print(f"Event Error: {e}")
        
        return False
    
