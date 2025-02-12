import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (30, 30, 30)
CIRCLE_COLOR = (0, 255, 0)
SQUARE_COLOR = (255, 0, 0)
INITIAL_RADIUS = 20
SQUARE_SIZE = 20
ZOOM_OUT_THRESHOLD = 100

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ice Movement Game")

# Circle properties
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
velocity_x, velocity_y = 0, 0
radius = INITIAL_RADIUS

# Score
score = 0

# Randomly spawn squares
def spawn_square():
    x = random.randint(0, WIDTH - SQUARE_SIZE)
    y = random.randint(0, HEIGHT - SQUARE_SIZE)
    return pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)

squares = [spawn_square() for _ in range(5)]

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity_x -= 0.5
    if keys[pygame.K_RIGHT]:
        velocity_x += 0.5
    if keys[pygame.K_UP]:
        velocity_y -= 0.5
    if keys[pygame.K_DOWN]:
        velocity_y += 0.5

    # Apply friction for ice movement
    velocity_x *= 0.98
    velocity_y *= 0.98

    # Update circle position
    circle_x += velocity_x
    circle_y += velocity_y

    # Boundaries
    if circle_x - radius < 0:
        circle_x = radius
        velocity_x = -velocity_x
    if circle_x + radius > WIDTH:
        circle_x = WIDTH - radius
        velocity_x = -velocity_x
    if circle_y - radius < 0:
        circle_y = radius
        velocity_y = -velocity_y
    if circle_y + radius > HEIGHT:
        circle_y = HEIGHT - radius
        velocity_y = -velocity_y

    # Check for square collision
    for square in squares[:]:
        if pygame.Rect(square).colliderect(pygame.Rect(circle_x - radius, circle_y - radius, 2 * radius, 2 * radius)):
            squares.remove(square)
            radius += 5
            score += 1
            squares.append(spawn_square())

    # Zoom out if circle becomes too large
    if radius > ZOOM_OUT_THRESHOLD:
        scale_factor = ZOOM_OUT_THRESHOLD / radius
        radius = ZOOM_OUT_THRESHOLD
        for square in squares:
            square.width = int(square.width * scale_factor)
            square.height = int(square.height * scale_factor)
            square.x = int(square.x * scale_factor)
            square.y = int(square.y * scale_factor)
        circle_x = int(circle_x * scale_factor)
        circle_y = int(circle_y * scale_factor)
        WIDTH = int(WIDTH * scale_factor)
        HEIGHT = int(HEIGHT * scale_factor)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, CIRCLE_COLOR, (circle_x, circle_y), radius)
    for square in squares:
        pygame.draw.rect(screen, SQUARE_COLOR, square)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
