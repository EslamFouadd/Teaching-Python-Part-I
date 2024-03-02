import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Your Own Adventure")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define player position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Define item position
item_x = 400
item_y = 300

# Define variable to track item capture
captured_items = 0

# Load player and item images
player_image = pygame.image.load("player.png")
item_image = pygame.image.load("item.png")

# Set game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Move player towards mouse pointer
    player_x += (mouse_x - player_x) / 20
    player_y += (mouse_y - player_y) / 20

    # Draw player and item
    screen.blit(player_image, (player_x - 25, player_y - 25))
    screen.blit(item_image, (item_x - 25, item_y - 25))

    # Check for item capture
    distance = ((player_x - item_x) ** 2 + (player_y - item_y) ** 2) ** 0.5
    if distance < 25:
        captured_items += 1
        print("Item captured! Total:", captured_items)
        item_x = 1000  # Move item off screen

    # Update display
    pygame.display.update()

    # Set frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
