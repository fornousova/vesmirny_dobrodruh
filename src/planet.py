import pygame
import random
from settings import planet_img, WIDTH, HEIGHT, PANEL_HEIGHT

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = planet_img
        self.rect = self.image.get_rect()
        self.spawn()
        self.angle = 0  # Initial angle

    def spawn(self):
        self.rect.center = (random.randint(30, WIDTH - 30), random.randint(PANEL_HEIGHT + 30, HEIGHT - 30))

    def draw(self, window):
        rotated_planet = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_planet.get_rect(center=self.rect.center)
        window.blit(rotated_planet, rotated_rect.topleft)

    def update(self):
        self.angle += 1  # Increase angle for rotation

def create_planet(planets):
    if len(planets) < 1:  # Ensure only one planet exists at a time
        planet = Planet()
        planets.add(planet)
