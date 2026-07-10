from ..paths import BG_IMAGE_PATH
import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.ground_surf = pygame.transform.scale(
                pygame.image.load(BG_IMAGE_PATH).convert(),
                # TODO Make values adaptable
                (1000, 1000))

        self.ground_rect = self.ground_surf.get_rect(topleft = (0, 0))

    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        # Draw ground
        self.center_target(player)

        ground_offset_pos = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset_pos)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)




        
        


