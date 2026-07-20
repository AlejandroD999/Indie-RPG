from ..paths import BG_IMAGE_PATH
import os
import pygame

# TODO Modify player movement
# TODO Fix surface size (no vectors) & make it my way
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.offset = pygame.math.Vector2()

        self.ground_surf = pygame.transform.scale(
                pygame.image.load(os.path.join(BG_IMAGE_PATH, "beginner_ground.png")).convert(),
                (
                    self.display_surface.get_size()[0] * 1.5,
                    self.display_surface.get_size()[1] * 1.5,
                ))

        self.ground_rect = self.ground_surf.get_rect(topleft = (0, 0))

    def bind_target(self, surface_rect, target_rect):
        target_rect.x = max(0, min(target_rect.x, surface_rect.width - target_rect.width)) 
        target_rect.y = max(0, min(target_rect.y, surface_rect.height - target_rect.height))

    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

        self.offset.x = max(0, min(self.offset.x, self.ground_rect.width - self.display_surface.get_width()))
        self.offset.y = max(0, min(self.offset.y, self.ground_rect.height - self.display_surface.get_height()))

        self.bind_target(self.ground_rect, target.rect)

    def custom_draw(self, player):

        self.center_target(player)
        self.display_surface.blit(self.ground_surf, (-self.offset.x, -self.offset.y))

        for sprite in self.sprites():
            if player.hitbox.colliderect(sprite.hitbox) and sprite != player:
                # TODO Handle player & sprite overlap 
                return
            self.display_surface.blit(sprite.image, (sprite.rect.x - self.offset.x, sprite.rect.y - self.offset.y))


        
        


