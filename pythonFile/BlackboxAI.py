import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CIRCLE_COLOR = (0, 255, 0)
SQUARE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
SQUARE_SIZE = 20
INITIAL_CIRCLE_RADIUS = 20
GROWTH_RATE = 5
ZOOM_OUT_THRESHOLD = 100
ZOOM_OUT_FACTOR = 0.5
MOVE_SPEED = 0.5

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Game")

# Circle properties
circle_pos = [WIDTH // 2, HEIGHT // 2]
circle_radius = INITIAL_CIRCLE_RADIUS
velocity = [0, 0]

# Square properties
squares = []
for _ in range(10):
    squares.append([random.randint(0, WIDTH - SQUARE_SIZE), random.randint(0, HEIGHT - SQUARE_SIZE)])

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_circle():
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(circle_pos[0]), int(circle_pos[1])), int(circle_radius))

def draw_squares():
    for square in squares:
        pygame.draw.rect(screen, SQUARE_COLOR, (square[0], square[1], SQUARE_SIZE, SQUARE_SIZE))

def check_collision(circle_pos, circle_radius, square):
    distance = math.hypot(circle_pos[0] - (square[0] + SQUARE_SIZE // 2), circle_pos[1] - (square[1] + SQUARE_SIZE // 2))
    return distance < (circle_radius + SQUARE_SIZE // 2)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity[0] -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        velocity[0] += MOVE_SPEED
    if keys[pygame.K_UP]:
        velocity[1] -= MOVE_SPEED
    if keys[pygame.K_DOWN]:
        velocity[1] += MOVE_SPEED

    # Update circle position
    circle_pos[0] += velocity[0]
    circle_pos[1] += velocity[1]

    # Apply friction
    velocity[0] *= 0.95
    velocity[1] *= 0.95

    # Keep circle within bounds
    circle_pos[0] = max(circle_radius, min(circle_pos[0], WIDTH - circle_radius))
    circle_pos[1] = max(circle_radius, min(circle_pos[1], HEIGHT - circle_radius))

    # Check for collisions with squares
    for square in squares[:]:
        if check_collision(circle_pos, circle_radius, square):
            squares.remove(square)
            circle_radius += GROWTH_RATE
            score += 1
            # Spawn a new square
            squares.append([random.randint(0, WIDTH - SQUARE_SIZE), random.randint(0, HEIGHT - SQUARE_SIZE)])

    # Zoom out if circle is too large
    if circle_radius > ZOOM_OUT_THRESHOLD:
        circle_radius *= ZOOM_OUT_FACTOR
        for square in squares:
            square[0] *= ZOOM_OUT_FACTOR
            square[1] *= ZOOM_OUT_FACTOR

    # Draw everything
    draw_circle()
    draw_squares()

    # Draw score
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()