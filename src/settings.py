import pygame

# Initialize Pygame
pygame.init()

# Initialize the mixer for background music
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load('src/music/background.mp3')
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
collision_sound = pygame.mixer.Sound('src/music/collision.wav')
bonus_sound = pygame.mixer.Sound('src/music/bonus.wav')
mouse_click_sound = pygame.mixer.Sound('src/music/mouse_click.mp3')

# Set up the game window
WIDTH = 800
HEIGHT = 600
PANEL_HEIGHT = 40  # Height of the top panel
GAME_HEIGHT = HEIGHT - PANEL_HEIGHT  # Adjusted game height
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Adventurer")

# Load background image
background_img = pygame.image.load('src/img/pozadi.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (218, 165, 32)

custom_font = pygame.font.Font("src/fonts/ARCADEClassic.TTF", 100)
restart_font = pygame.font.Font("src/fonts/ARCADEClassic.TTF", 70)
final_score_font = pygame.font.Font("src/fonts/ARCADEClassic.TTF", 40)
info_font = pygame.font.Font("src/fonts/StarShield.ttf", 30)

# Load images
spaceship_img = pygame.image.load('src/img/spaceship.png')
spaceship_img = pygame.transform.scale(spaceship_img, (60, 80))

asteroid_img = pygame.image.load('src/img/basteroid.png')
asteroid_img = pygame.transform.scale(asteroid_img, (50, 50))

planet_img = pygame.image.load('src/img/planetka.png')
planet_img = pygame.transform.scale(planet_img, (70, 50))

star_img = pygame.image.load('src/img/hvezda.png')
star_img = pygame.transform.scale(star_img, (50, 50))

heart_img = pygame.image.load('src/img/srdce.png')
heart_img = pygame.transform.scale(heart_img, (50, 50))
