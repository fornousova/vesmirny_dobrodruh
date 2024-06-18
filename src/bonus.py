import pygame
import random
from settings import star_img, heart_img, WIDTH, PANEL_HEIGHT, HEIGHT

class Bonus(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def spawn(self):
        self.rect.center = (random.randint(30, WIDTH - 30), random.randint(PANEL_HEIGHT + 30, HEIGHT - 30))

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        pass

class Star(Bonus):
    def __init__(self):
        super().__init__(star_img)
        self.angle = 0  # Initial angle

    def update(self):
        self.angle += 1  # Increase angle for rotation

class Heart(Bonus):
    def __init__(self):
        super().__init__(heart_img)
        self.angle = 0  # Initial angle

    def add_life(self, spaceship):
        if spaceship.lives < 3:
            spaceship.lives += 1  # Add one life when collected

def create_bonus(bonuses):
    bonus_types = [Star, Heart]
    existing_bonus_types = {type(bonus) for bonus in bonuses}

    if len(existing_bonus_types) == 0:  # If no bonuses exist, add both
        for bonus_type in bonus_types:
            bonus = bonus_type()
            bonus.spawn()
            bonuses.add(bonus)
    elif len(existing_bonus_types) == 1:  # If only one type of bonus exists, add the missing one
        missing_bonus_type = next(bonus_type for bonus_type in bonus_types if bonus_type not in existing_bonus_types)
        bonus = missing_bonus_type()
        bonus.spawn()
        bonuses.add(bonus)
