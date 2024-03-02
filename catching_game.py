import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catching Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define player position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 50

# Define object properties
object_size = 30
object_speed = 5
objects = []

# Define variable to track score
score = 0

# Load player image
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

# Set game clock
clock = pygame.time.Clock()

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
    player_x += (mouse_x - player_x) / 10

    # Draw player
    screen.blit(player_image, (player_x - player_rect.width / 2, player_y - player_rect.height / 2))

    # Create falling objects
    if random.randint(0, 100) < 5:
        object_x = random.randint(0, SCREEN_WIDTH - object_size)
        object_y = 0
        objects.append([object_x, object_y])

    # Move and draw falling objects
    for obj in objects:
        obj[1] += object_speed
        pygame.draw.rect(screen, BLACK, (obj[0], obj[1], object_size, object_size))

        # Check for collision with player
        if (
            player_x - player_rect.width / 2 < obj[0] < player_x + player_rect.width / 2
            and player_y - player_rect.height / 2 < obj[1] < player_y + player_rect.height / 2
        ):
            objects.remove(obj)
            score += 1
            print("Score:", score)

        # Remove objects that go off-screen
        if obj[1] > SCREEN_HEIGHT:
            objects.remove(obj)

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
