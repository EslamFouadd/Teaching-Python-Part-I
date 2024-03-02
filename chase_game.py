import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chase Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define player and enemy positions
player_x = 50
player_y = 50
enemy_x = 700
enemy_y = 500

# Set game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player based on arrow key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Update enemy position (chase player)
    if player_x < enemy_x:
        enemy_x -= 1
    elif player_x > enemy_x:
        enemy_x += 1
    if player_y < enemy_y:
        enemy_y -= 1
    elif player_y > enemy_y:
        enemy_y += 1

    # Draw player and enemy
    pygame.draw.rect(screen, BLACK, (player_x, player_y, 50, 50))
    pygame.draw.rect(screen, BLACK, (enemy_x, enemy_y, 50, 50))

    # Update display
    pygame.display.update()

    # Set frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
