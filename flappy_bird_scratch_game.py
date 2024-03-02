import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load images
bird_image = pygame.image.load('bird.png')
bird_rect = bird_image.get_rect()
bird_rect.center = (100, SCREEN_HEIGHT // 2)

pipe_image = pygame.image.load('pipe.png')

# Define bird properties
bird_speed = 0
gravity = 0.25

# Define pipe properties
pipe_width = 50
pipe_gap = 150
pipe_frequency = 1000
last_pipe_time = pygame.time.get_ticks()

pipes = []

def draw_bird():
    screen.blit(bird_image, bird_rect)

def draw_pipes():
    for pipe in pipes:
        screen.blit(pipe_image, pipe)

def generate_pipe():
    pipe_y = random.randint(50, SCREEN_HEIGHT - 250)
    pipes.append(pygame.Rect(SCREEN_WIDTH, pipe_y, pipe_width, SCREEN_HEIGHT))

def move_pipes():
    for pipe in pipes:
        pipe.x -= 2
        if pipe.x <= -pipe_width:
            pipes.remove(pipe)

def check_collision():
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return True
    return False

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = -6

    # Bird movement
    bird_speed += gravity
    bird_rect.y += bird_speed

    # Generate pipes
    if pygame.time.get_ticks() - last_pipe_time > pipe_frequency:
        generate_pipe()
        last_pipe_time = pygame.time.get_ticks()

    # Move pipes
    move_pipes()

    # Check collision
    if check_collision():
        running = False

    # Draw elements
    draw_bird()
    draw_pipes()

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
