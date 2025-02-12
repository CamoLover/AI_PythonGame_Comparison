import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (30, 30, 30)
CIRCLE_COLOR = (0, 150, 255)
SQUARE_COLOR = (255, 100, 100)
FONT_COLOR = (255, 255, 255)
ACCELERATION = 0.2
FRICTION = 0.98
INITIAL_RADIUS = 20

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ice Movement Game")

# Initialize variables
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_radius = INITIAL_RADIUS
velocity_x, velocity_y = 0, 0
squares = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), 10) for _ in range(10)]
score = 0
font = pygame.font.Font(None, 36)

def add_squares():
    for _ in range(3):
        squares.append((random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), 10))

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BACKGROUND_COLOR)
    keys = pygame.key.get_pressed()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement logic
    if keys[pygame.K_LEFT]:
        velocity_x -= ACCELERATION
    if keys[pygame.K_RIGHT]:
        velocity_x += ACCELERATION
    if keys[pygame.K_UP]:
        velocity_y -= ACCELERATION
    if keys[pygame.K_DOWN]:
        velocity_y += ACCELERATION

    # Apply friction
    velocity_x *= FRICTION
    velocity_y *= FRICTION

    # Update player position
    player_x += velocity_x
    player_y += velocity_y

    # Handle collisions with screen bounds
    player_x = max(player_radius, min(WIDTH - player_radius, player_x))
    player_y = max(player_radius, min(HEIGHT - player_radius, player_y))

    # Check collisions with squares
    for square in squares[:]:
        sx, sy, s_size = square
        if (sx - player_x) ** 2 + (sy - player_y) ** 2 < (player_radius + s_size) ** 2:
            squares.remove(square)
            player_radius += 2
            score += 1
            add_squares()

    # Dynamic scaling
    scale = max(1, player_radius / INITIAL_RADIUS)
    screen.fill(BACKGROUND_COLOR)
    zoomed_surface = pygame.Surface((WIDTH * scale, HEIGHT * scale))
    zoomed_surface.fill(BACKGROUND_COLOR)

    # Draw squares
    for sx, sy, s_size in squares:
        pygame.draw.rect(zoomed_surface, SQUARE_COLOR, (sx * scale, sy * scale, s_size * scale, s_size * scale))

    # Draw player circle
    pygame.draw.circle(zoomed_surface, CIRCLE_COLOR, (int(player_x * scale), int(player_y * scale)), int(player_radius * scale))
    scaled_surface = pygame.transform.smoothscale(zoomed_surface, (WIDTH, HEIGHT))
    screen.blit(scaled_surface, (0, 0))

    # Draw UI
    score_text = font.render(f"Score: {score}", True, FONT_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
