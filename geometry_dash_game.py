import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define game properties
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 4
player_y = SCREEN_HEIGHT // 2
player_velocity = 0
gravity = 0.5
jump_height = 10
obstacle_width = 30
obstacle_height = random.randint(100, 400)
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - obstacle_height
obstacle_velocity = 5
score = 0

# Load game font
font = pygame.font.Font(None, 36)

# Define functions
def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

def draw_obstacle():
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

def move_player():
    global player_y, player_velocity
    player_y += player_velocity
    player_velocity += gravity
    if player_y >= SCREEN_HEIGHT - player_height:
        player_y = SCREEN_HEIGHT - player_height
        player_velocity = 0

def jump():
    global player_velocity
    player_velocity = -jump_height

def check_collision():
    if (player_x + player_width >= obstacle_x and player_x <= obstacle_x + obstacle_width and
        (player_y <= obstacle_y or player_y + player_height >= obstacle_y + obstacle_height)):
        return True
    return False

def update_score():
    global score
    score += 1

def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Set game clock
clock = pygame.time.Clock()

# Set game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    # Move player
    move_player()

    # Draw elements
    draw_player()
    draw_obstacle()
    display_score()

    # Move obstacle
    obstacle_x -= obstacle_velocity
    if obstacle_x + obstacle_width < 0:
        obstacle_x = SCREEN_WIDTH
        obstacle_height = random.randint(100, 400)
        obstacle_y = SCREEN_HEIGHT - obstacle_height
        update_score()

    # Check collision
    if check_collision():
        running = False

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
