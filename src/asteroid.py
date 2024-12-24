# asteroid.py

import pygame
import random
from settings import ASTEROID_IMAGE, INITIAL_ASTEROID_SIZE, ASTEROID_FALL_SPEED

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load(ASTEROID_IMAGE).convert_alpha()
        self.size = random.randint(INITIAL_ASTEROID_SIZE - 10, INITIAL_ASTEROID_SIZE + 10)  # Randomize size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(
            center=(random.randint(0, screen_width), random.randint(-100, -40))
        )
        self.speed = random.randint(ASTEROID_FALL_SPEED - 2, ASTEROID_FALL_SPEED + 2)  # Randomize speed

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()
