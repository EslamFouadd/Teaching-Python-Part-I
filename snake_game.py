import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define game properties
snake = [(200, 200), (210, 200), (220, 200)]
snake_direction = RIGHT
food = (random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
        random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

# Define functions
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def move_snake():
    global snake
    new_head = (snake[0][0] + snake_direction[0] * CELL_SIZE,
                snake[0][1] + snake_direction[1] * CELL_SIZE)
    snake = [new_head] + snake[:-1]

def check_collision():
    if (snake[0][0] < 0 or snake[0][0] >= SCREEN_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= SCREEN_HEIGHT or
        snake[0] in snake[1:]):
        return True
    return False

def draw_food():
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def generate_food():
    global food
    food = (random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
            random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

def handle_input(event):
    global snake_direction
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and snake_direction != DOWN:
            snake_direction = UP
        elif event.key == pygame.K_DOWN and snake_direction != UP:
            snake_direction = DOWN
        elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
            snake_direction = LEFT
        elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
            snake_direction = RIGHT

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
        handle_input(event)

    # Move snake
    move_snake()

    # Check collision
    if check_collision():
        running = False

    # Draw elements
    draw_snake()
    draw_food()

    # Check if snake ate food
    if snake[0] == food:
        generate_food()
        snake.append(snake[-1])

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()
sys.exit()
