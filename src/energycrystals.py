# energycrystals.py

import pygame
import random
from settings import ENERGY_CRYSTAL_IMAGE, SCREEN_WIDTH, SCREEN_HEIGHT


class EnergyCrystal(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load(ENERGY_CRYSTAL_IMAGE).convert_alpha()

        # Resize the crystal to make it visible
        self.image = pygame.transform.scale(self.image, (40, 40))  # Set a larger size (e.g., 40x40)

        self.rect = self.image.get_rect(
            center=(random.randint(0, screen_width), -50)  # Spawn just above the screen
        )
        self.speed = 1  # Slower fall speed for the energy crystals

    def update(self):
        # Make the energy crystal fall from top to bottom
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove crystal if it goes off-screen
