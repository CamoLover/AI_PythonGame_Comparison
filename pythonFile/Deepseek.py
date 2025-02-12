import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Eater")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player properties
player_radius = 20
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 0.5
player_dx, player_dy = 0, 0
friction = 0.95

# Squares properties
square_size = 20
squares = []
square_spawn_rate = 50  # Lower is faster

# Score
score = 0
font = pygame.font.Font(None, 36)

# Zoom factor
zoom_factor = 1.0

def spawn_square():
    x = random.randint(0, WIDTH - square_size)
    y = random.randint(0, HEIGHT - square_size)
    squares.append(pygame.Rect(x, y, square_size, square_size))

def draw_player():
    pygame.draw.circle(screen, BLUE, (int(player_x), int(player_y)), int(player_radius * zoom_factor), 0)

def draw_squares():
    for square in squares:
        pygame.draw.rect(screen, RED, (square.x * zoom_factor, square.y * zoom_factor, square_size * zoom_factor, square_size * zoom_factor))

def check_collisions():
    global player_radius, score, zoom_factor
    for square in squares[:]:
        if math.hypot(player_x - square.x, player_y - square.y) < player_radius:
            squares.remove(square)
            player_radius += 2
            score += 1
            if player_radius > 50:
                zoom_factor = max(0.5, zoom_factor - 0.05)

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def reset_game():
    global player_radius, player_x, player_y, player_dx, player_dy, score, zoom_factor, squares
    player_radius = 20
    player_x, player_y = WIDTH // 2, HEIGHT // 2
    player_dx, player_dy = 0, 0
    score = 0
    zoom_factor = 1.0
    squares = []

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement with ice-like physics
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_dx -= player_speed
    if keys[pygame.K_RIGHT]:
        player_dx += player_speed
    if keys[pygame.K_UP]:
        player_dy -= player_speed
    if keys[pygame.K_DOWN]:
        player_dy += player_speed

    player_dx *= friction
    player_dy *= friction
    player_x += player_dx
    player_y += player_dy

    # Keep player within screen bounds
    player_x = max(player_radius, min(WIDTH - player_radius, player_x))
    player_y = max(player_radius, min(HEIGHT - player_radius, player_y))

    # Spawn squares randomly
    if random.randint(0, square_spawn_rate) == 0:
        spawn_square()

    # Check for collisions
    check_collisions()

    # Draw everything
    draw_player()
    draw_squares()
    draw_score()

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()