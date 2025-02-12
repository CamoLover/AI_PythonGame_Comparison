import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Circle properties
circle_radius = 20
circle_x = width // 2
circle_y = height // 2
circle_speed = 5
circle_x_speed = 0
circle_y_speed = 0
circle_mass = 1  # Mass affects inertia

# Square properties
square_size = 20
squares = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Camera
camera_x = 0
camera_y = 0
zoom_level = 1.0

# Function to generate squares
def generate_square():
    x = random.randint(0, width - square_size)
    y = random.randint(0, height - square_size)
    squares.append(pygame.Rect(x, y, square_size, square_size))

# Generate initial squares
for _ in range(10):
    generate_square()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circle_x_speed -= circle_speed / circle_mass
            if event.key == pygame.K_RIGHT:
                circle_x_speed += circle_speed / circle_mass
            if event.key == pygame.K_UP:
                circle_y_speed -= circle_speed / circle_mass
            if event.key == pygame.K_DOWN:
                circle_y_speed += circle_speed / circle_mass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and circle_x_speed < 0:
                circle_x_speed = 0
            if event.key == pygame.K_RIGHT and circle_x_speed > 0:
                circle_x_speed = 0
            if event.key == pygame.K_UP and circle_y_speed < 0:
                circle_y_speed = 0
            if event.key == pygame.K_DOWN and circle_y_speed > 0:
                circle_y_speed = 0

    # Update circle position (with inertia)
    circle_x += circle_x_speed
    circle_y += circle_y_speed

    # Decelerate the circle
    circle_x_speed *= 0.95  # Friction
    circle_y_speed *= 0.95

    # Keep circle within screen bounds
    if circle_x - circle_radius < 0:
        circle_x = circle_radius
        circle_x_speed = 0
    if circle_x + circle_radius > width:
        circle_x = width - circle_radius
        circle_x_speed = 0
    if circle_y - circle_radius < 0:
        circle_y = circle_radius
        circle_y_speed = 0
    if circle_y + circle_radius > height:
        circle_y = height - circle_radius
        circle_y_speed = 0

    # Check for collisions with squares
    for square in squares[:]:
        if pygame.Rect(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2, circle_radius * 2).colliderect(square):
            squares.remove(square)
            circle_radius += 2
            circle_mass += 0.1
            score += 1
            generate_square()

    # Adjust zoom based on circle size
    zoom_level = max(1.0, 100.0 / circle_radius)  # Zoom out as circle grows
    camera_x = circle_x - width / 2 / zoom_level
    camera_y = circle_y - height / 2 / zoom_level

    # Draw everything
    screen.fill(black)

    # Draw squares
    for square in squares:
        pygame.draw.rect(screen, red, pygame.Rect(
            (square.x - camera_x) * zoom_level,
            (square.y - camera_y) * zoom_level,
            square_size * zoom_level,
            square_size * zoom_level
        ))

    # Draw circle
    pygame.draw.circle(screen, white, (
        (circle_x - camera_x) * zoom_level,
        (circle_y - camera_y) * zoom_level
    ), circle_radius * zoom_level)

    # Display score
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()