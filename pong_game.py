import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define paddle properties
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
paddle1_x = 50
paddle1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x = SCREEN_WIDTH - 50 - PADDLE_WIDTH
paddle2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Define ball properties
BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

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

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collision with paddles
    if (
        paddle1_x + PADDLE_WIDTH > ball_x > paddle1_x
        and paddle1_y + PADDLE_HEIGHT > ball_y > paddle1_y
    ) or (
        paddle2_x < ball_x < paddle2_x + PADDLE_WIDTH
        and paddle2_y + PADDLE_HEIGHT > ball_y > paddle2_y
    ):
        ball_dx *= -1

    # Check for collision with walls
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_dy *= -1

    # Check for scoring
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - BALL_SIZE:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_dx *= -1

    # Draw paddles and ball
    pygame.draw.rect(screen, BLACK, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, BLACK, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, BLACK, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
