# Space Adventurer

This is a simple 2D space adventure game where you control a spaceship, avoid asteroids, collect bonuses, and gain points by touching planets. The game includes background music and sound effects for collisions, bonuses, and mouse clicks.

## Requirements

- Python 3
- Pygame

## Installation

1. Install Pygame:
    ```bash
    pip install pygame
    ```

2. Download the game files and ensure you have the following directory structure:
    ```
    src/
        media/
            background.mp3
            collision.wav
            bonus.wav
            mouse_click.mp3
    img/
        pozadi.png
        spaceship.png
        basteroid.png
        planetka.png
        hvezda.png
        srdce.png
    fonts/
        ARCADEClassic.TTF
        StarShield.ttf
    ```

## How to Play

1. Run the game:
    ```bash
    python game.py
    ```

2. On the start screen, click "Start Game" to begin.

3. Use the arrow keys to move the spaceship:
    - Left arrow: Move left
    - Right arrow: Move right
    - Up arrow: Move up
    - Down arrow: Move down

4. **Objective**:
    - Avoid asteroids: Asteroids move randomly across the screen. If you collide with them, you lose a life.
    - Collect bonuses: There are two types of bonuses:
        - Stars: Increase your score.
        - Hearts: Increase your lives (up to a maximum of 3).
    - Touch planets: Touching a planet increases your score and resets the fuel.

5. **Game Mechanics**:
    - **Lives**: You start with 3 lives. You lose a life when you collide with an asteroid or run out of time.
    - **Score**: Your score increases by 1 for each planet you touch and each star you collect.
    - **Fuelr**: You have a limited amount of time to touch a planet. If the timer runs out, you lose a life.  The timer resets each time you touch a planet.

6. The game ends when you run out of lives. The final score is displayed on the game over screen. Click "Restart Game" to play again.

## Code Overview

- **SpaceShip class**: Handles the spaceship's movement, direction, and lives.
- **Asteroid class**: Represents asteroids that the spaceship needs to avoid.
- **Planet class**: Represents planets that the spaceship needs to touch to score points.
- **Bonus class**: Represents bonuses like stars and hearts. Hearts increase the spaceship's lives.
- **Button class**: Manages buttons on the start and game over screens.

## Functions

- `start_screen()`: Displays the start screen.
- `game_over_screen(score)`: Displays the game over screen and shows the final score.
- `render_top_panel(lives, score, fuel)`: Renders the top panel with lives, score, and fuel information.
- `game_loop()`: The main game loop that handles game logic and rendering.

## Assets

- Background music: `background.mp3`
- Sound effects: `collision.wav`, `bonus.wav`, `mouse_click.mp3`
- Images: `pozadi.png`, `spaceship.png`, `basteroid.png`, `planetka.png`, `hvezda.png`, `srdce.png`
- Fonts: `ARCADEClassic.TTF`, `StarShield.ttf`

Enjoy the game!
