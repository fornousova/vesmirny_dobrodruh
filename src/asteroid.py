import pygame
import random
from settings import asteroid_img, WIDTH, HEIGHT

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = asteroid_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = random.uniform(-1, 1)  # Random horizontal speed
        self.speed_y = random.uniform(-1, 1)  # Random vertical speed

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Wrap around the screen edges
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT

    def draw(self, window):
        window.blit(self.image, self.rect)

# Function to create a new asteroid
def create_asteroid(asteroids):
    x = random.randrange(WIDTH - 30)
    y = random.randrange(-100, -40)
    asteroid = Asteroid(x, y)
    asteroids.add(asteroid)
