import pygame
import sys
from settings import *
from spaceship import Spaceship
from asteroid import Asteroid
from energycrystals import EnergyCrystal

pygame.init()

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Scavenger")
clock = pygame.time.Clock()

# Load sounds
pygame.mixer.music.load(BACKGROUND_MUSIC)
pygame.mixer.music.play(-1)
clash_sound = pygame.mixer.Sound(CLASH_SOUND)

# Create groups
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
crystals = pygame.sprite.Group()

# Create spaceship
spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(spaceship)

# Variables
running = True
last_crystal_spawn = pygame.time.get_ticks()  # Timestamp for crystal spawning
hearts = 3
start_time = pygame.time.get_ticks()  # Track the starting time for the timer
game_over = False  # Flag to indicate if the game is over
elapsed_time_at_gameover = 0  # Store the time when the game is over

# Replay button
button_font = pygame.font.Font(None, 48)
replay_button = pygame.Rect((SCREEN_WIDTH // 2 - 100), (SCREEN_HEIGHT // 2 + 50), 200, 50)

while running:
    screen.fill((30, 30, 30))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            # Check if the replay button is clicked
            if replay_button.collidepoint(event.pos):
                # Reset game state
                hearts = 3
                spaceship.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
                all_sprites.empty()
                asteroids.empty()
                crystals.empty()
                all_sprites.add(spaceship)
                start_time = pygame.time.get_ticks()
                game_over = False
                elapsed_time_at_gameover = 0  # Reset the elapsed time

    if not game_over:
        # Spawn asteroids
        if len(asteroids) < 10:
            asteroid = Asteroid(SCREEN_WIDTH)
            all_sprites.add(asteroid)
            asteroids.add(asteroid)

        # Spawn crystals every 10 seconds
        current_time = pygame.time.get_ticks()
        if current_time - last_crystal_spawn > CRYSTAL_SPAWN_INTERVAL:  # Every 10 seconds
            crystal = EnergyCrystal(SCREEN_WIDTH)  # Pass width to spawn at random x
            all_sprites.add(crystal)
            crystals.add(crystal)
            last_crystal_spawn = current_time  # Reset spawn timer

        # Check collisions with asteroids
        if pygame.sprite.spritecollide(spaceship, asteroids, True):
            clash_sound.play()
            hearts -= 1
            if hearts == 0:
                game_over = True  # Set the game over flag
                elapsed_time_at_gameover = pygame.time.get_ticks() - start_time  # Store the time when game ends

        # Check collisions with energy crystals
        crystal_collision = pygame.sprite.spritecollide(spaceship, crystals, True)
        if crystal_collision:
            spaceship.speed += 0.3  # Increase spaceship speed by 0.3 after collecting the crystal
            print(f"Crystal collected! New spaceship speed: {spaceship.speed}")  # Debugging line

        # Update and draw sprites
        all_sprites.update()  # Update all sprites
        all_sprites.draw(screen)

        # Display hearts
        font = pygame.font.Font(None, 36)
        heart_text = font.render(f"Hearts: {hearts}", True, (255, 0, 0))
        screen.blit(heart_text, (10, 10))

        # Display time while game is running
        if not game_over:
            elapsed_time = pygame.time.get_ticks() - start_time
            minutes = (elapsed_time // 1000) // 60
            seconds = (elapsed_time // 1000) % 60
            timer_text = font.render(f"{minutes:02}:{seconds:02}", True, (255, 255, 255))
            screen.blit(timer_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 40))

    else:
        # Display Game Over message
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        # Display the time at the end (static, no longer updating)
        minutes = (elapsed_time_at_gameover // 1000) // 60
        seconds = (elapsed_time_at_gameover // 1000) % 60
        time_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, (255, 255, 255))
        screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, SCREEN_HEIGHT // 2))

        # Display replay button
        pygame.draw.rect(screen, (0, 255, 0), replay_button)
        replay_button_text = button_font.render("Replay", True, (0, 0, 0))
        screen.blit(replay_button_text, (replay_button.x + replay_button.width // 2 - replay_button_text.get_width() // 2,
                                         replay_button.y + replay_button.height // 2 - replay_button_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
