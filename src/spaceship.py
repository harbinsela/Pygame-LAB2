import pygame
from settings import SPACESHIP_IMAGE, SPACESHIP_SPEED

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(SPACESHIP_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize the spaceship
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 60))
        self.speed = SPACESHIP_SPEED  # Set initial speed from settings

    def update(self):
        # Get keys inside the update method
        keys = pygame.key.get_pressed()

        # Move spaceship based on keys
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < pygame.display.get_surface().get_height():
            self.rect.y += self.speed
