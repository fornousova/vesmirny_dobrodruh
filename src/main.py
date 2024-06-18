import pygame
import random
import sys
from settings import *
from spaceship import SpaceShip
from asteroid import create_asteroid, Asteroid
from planet import create_planet
from bonus import create_bonus, Star, Heart
from button import Button

# Increase spawn rate
spawn_rate = 50

# Initialize game variables
spaceship = SpaceShip(WIDTH // 2, HEIGHT - 100)
asteroids = pygame.sprite.Group()
planets = pygame.sprite.Group()
stars = pygame.sprite.Group()
bonuses = pygame.sprite.Group()
score = 0
font = pygame.font.Font(None, 36)

# Create the planet and star immediately after initializing the game
create_planet(planets)
create_bonus(bonuses)

# Start screen function
def start_screen():
    button = Button(WIDTH // 2, HEIGHT // 2, "Start Game", restart_font)

    while True:
        WINDOW.blit(background_img, (0, 0))  # Blit background image
        button.draw(WINDOW)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    return  # Exit the start screen and begin the game

# Game over screen function
def game_over_screen(score):
    button = Button(WIDTH // 2, HEIGHT // 2 + 80, "Restart Game", restart_font)
    while True:
        WINDOW.blit(background_img, (0, 0))  # Blit background image
        game_over_text = custom_font.render("Game Over", True, (75, 0, 130))
        score_text = final_score_font.render(f"Final score {score}", True, YELLOW)
        
        # Calculate positions for centering the text
        game_over_text_x = (WIDTH - game_over_text.get_width()) // 2
        game_over_text_y = HEIGHT // 3
        
        score_text_x = (WIDTH - score_text.get_width()) // 2
        score_text_y = game_over_text_y + game_over_text.get_height()   # 20 pixels below "Game Over" text

        WINDOW.blit(game_over_text, (game_over_text_x, game_over_text_y))
        WINDOW.blit(score_text, (score_text_x, score_text_y))
        button.draw(WINDOW)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    return True  # Exit the game over screen and restart the game

# Function to render the top panel
def render_top_panel(lives, score, fuel):
    panel_height = 40
    pygame.draw.rect(WINDOW, (0, 0, 0), (0, 0, WIDTH, panel_height))

    lives_text = info_font.render(f"Lives: {lives}", True, WHITE)
    score_text = info_font.render(f"Score: {score}", True, WHITE)

    if fuel < 5:
        fuel_text_color = RED
    else:
        fuel_text_color = WHITE

    fuel_text = info_font.render(f"Fuel: {int(fuel)}", True, fuel_text_color)

    WINDOW.blit(lives_text, (10, 5))
    WINDOW.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 5))
    WINDOW.blit(fuel_text, (WIDTH - fuel_text.get_width() - 10, 5))

# Game loop
def game_loop():
    global spaceship, asteroids, planets, bonuses, score, game_over, time_remaining

    spaceship = SpaceShip(WIDTH // 2, HEIGHT - 100)
    asteroids = pygame.sprite.Group()
    planets = pygame.sprite.Group()
    bonuses = pygame.sprite.Group()
    score = 0
    game_over = False
    time_limit = 15  # Initial time limit in seconds
    time_remaining = time_limit

    create_planet(planets)
    create_bonus(bonuses)

    running = True
    clock = pygame.time.Clock()

    while running:
        # Blit background image
        WINDOW.blit(background_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spaceship.rect.left > 0:
            spaceship.move_left()
        if keys[pygame.K_RIGHT] and spaceship.rect.right < WIDTH:
            spaceship.move_right()
        if keys[pygame.K_UP] and spaceship.rect.top > 0:
            spaceship.move_up()
        if keys[pygame.K_DOWN] and spaceship.rect.bottom < HEIGHT:
            spaceship.move_down()

        if not game_over:
            if random.randrange(spawn_rate) == 0:
                create_asteroid(asteroids)

            for asteroid in asteroids:
                asteroid.move()
                asteroid.draw(WINDOW)
                if asteroid.rect.top > HEIGHT:
                    asteroids.remove(asteroid)

            for planet in planets:
                planet.update()  # Update planet's rotation angle
                planet.draw(WINDOW)
                if pygame.sprite.collide_rect(spaceship, planet):
                    planets.remove(planet)
                    score += 1
                    create_planet(planets)  # Create a new planet
                    # Reset the time remaining
                    time_remaining = time_limit
                    bonus_sound.play()  # Play bonus sound

            for bonus in bonuses:
                bonus.update()  # Update bonus's rotation angle
                bonus.draw(WINDOW)
                if pygame.sprite.collide_rect(spaceship, bonus):
                    bonuses.remove(bonus)
                    if isinstance(bonus, Heart):  # Check if the bonus is Heart
                        bonus.add_life(spaceship)  # Add life if the bonus is Heart
                    else:
                        score += 1
                    create_bonus(bonuses)  # Create a new bonus
                    bonus_sound.play()  # Play bonus sound

            if pygame.sprite.spritecollide(spaceship, asteroids, True):
                spaceship.lives -= 1  # Reduce lives when colliding with asteroid
                collision_sound.play()  # Play collision sound
                if spaceship.lives <= 0:
                    game_over = True

            # Reduce time remaining
            time_remaining -= 1 / 60  # Subtract elapsed time since last frame
            if time_remaining <= 0:
                spaceship.lives -= 1  # Reduce lives when fuel runs out
                if spaceship.lives <= 0:
                    game_over = True
                else:
                    time_remaining = time_limit  # Reset the time remaining

        spaceship.draw(WINDOW)

        # Render the top panel
        render_top_panel(spaceship.lives, score, time_remaining)

        if game_over:
            if game_over_screen(score):
                # Reset game variables and restart the game
                spaceship = SpaceShip(WIDTH // 2, HEIGHT - 100)
                asteroids = pygame.sprite.Group()
                planets = pygame.sprite.Group()
                bonuses = pygame.sprite.Group()
                score = 0
                time_remaining = time_limit
                create_planet(planets)
                create_bonus(bonuses)
                game_over = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Show the start screen before the game starts
start_screen()

# Start the game loop
game_loop()
