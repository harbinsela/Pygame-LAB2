### Overview
The player controls a spaceship, avoids asteroids, collects energy crystals, and survives as long as possible. The goal is to collect crystals to increase your spaceship's speed while avoiding collisions with asteroids. The game ends when all hearts are lost, and the time played is displayed.

### How to Play
1. **Controls:**
   - Use the arrow keys (Left, Right, Up, Down) to move the spaceship.
   - Avoid asteroids falling from the top of the screen.
   - Collect energy crystals to increase your spaceship’s speed.

2. **Objective:**
   - Survive as long as possible by avoiding asteroids and collecting crystals.
   - The game ends when all hearts are lost (colliding with too many asteroids).

3. **Game Over:**
   - The game ends when the player loses all hearts.
   - The total play time is displayed with a "Game Over!" message, and a replay button allows restarting the game.

### Game Features
- **Asteroid Spawning:** Asteroids randomly spawn from the top and fall at varying speeds and sizes.
- **Crystal Spawning:** Crystals spawn every 10 seconds, and collecting them increases the spaceship’s speed.
- **Timer:** A countdown starts when the game begins and stops when the game ends, showing how long the player survived.
- **Hearts:** The player starts with 3 hearts. Each collision with an asteroid reduces the number of hearts. The game ends when all hearts are lost.
- **Replay:** When the game ends, a replay button is displayed to restart the game.

### Implementation Summary
- **Main Loop:** Handles player input, updates the screen, checks for collisions, and updates the game state (e.g., timer, hearts).
- **Spaceship Class:** Handles spaceship movement and collision detection with asteroids and crystals.
- **Asteroid Class:** Represents falling asteroids and removes them when they go off-screen or collide with the spaceship.
- **Energy Crystal Class:** Handles spawning of crystals, their movement, and collision with the spaceship.
- **Settings:** Contains game configuration (screen size, speed, sound, etc.).
- **Sounds:** Background music plays continuously, and a sound effect plays on asteroid collision.
