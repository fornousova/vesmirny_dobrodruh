import pygame
from settings import spaceship_img, PANEL_HEIGHT

class SpaceShip:
    def __init__(self, x, y):
        self.image = spaceship_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.direction = 0  # Initial direction (in degrees)
        self.lives = 3  # Initial lives

    def move_left(self):
        self.rect.x -= self.speed
        self.update_direction(-90)  # Adjust direction when moving left

    def move_right(self):
        self.rect.x += self.speed
        self.update_direction(90)  # Adjust direction when moving right

    def move_up(self):
        if self.rect.top > PANEL_HEIGHT:
            self.rect.y -= self.speed
        self.update_direction(0)  # Adjust direction when moving up

    def move_down(self):
        self.rect.y += self.speed
        self.update_direction(180)  # Adjust direction when moving down

    def update_direction(self, direction):
        self.direction = direction
        # Flip the image horizontally if moving to the left
        if direction == 90:
            self.image = pygame.transform.flip(spaceship_img, True, False)
        else:
            self.image = spaceship_img

    def draw(self, window):
        # Rotate the image based on the direction
        rotated_image = pygame.transform.rotate(self.image, -self.direction)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        window.blit(rotated_image, rotated_rect.topleft)
