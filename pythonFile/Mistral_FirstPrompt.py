import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Eater Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
player_radius = 20
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_vel = [0, 0]
player_speed = 5
friction = 0.98
score = 0
zoom_level = 1

# Square variables
square_size = 20
square_positions = []

# Font
font = pygame.font.SysFont(None, 36)

def spawn_square():
    x = random.randint(0, SCREEN_WIDTH - square_size)
    y = random.randint(0, SCREEN_HEIGHT - square_size)
    square_positions.append([x, y])

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    global player_pos, player_vel, score, zoom_level, square_positions

    clock = pygame.time.Clock()
    running = True

    # Spawn initial squares
    for _ in range(10):
        spawn_square()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_vel[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_vel[0] += player_speed
        if keys[pygame.K_UP]:
            player_vel[1] -= player_speed
        if keys[pygame.K_DOWN]:
            player_vel[1] += player_speed

        # Apply friction
        player_vel[0] *= friction
        player_vel[1] *= friction

        # Update player position
        player_pos[0] += player_vel[0]
        player_pos[1] += player_vel[1]

        # Keep player within screen bounds
        player_pos[0] = max(player_radius, min(SCREEN_WIDTH - player_radius, player_pos[0]))
        player_pos[1] = max(player_radius, min(SCREEN_HEIGHT - player_radius, player_pos[1]))

        # Check for collisions with squares
        new_square_positions = []
        for square in square_positions:
            if math.sqrt((player_pos[0] - square[0] - square_size / 2) ** 2 + (player_pos[1] - square[1] - square_size / 2) ** 2) < player_radius:
                score += 1
                player_radius += 2
                if player_radius > 50:
                    zoom_level = 0.8
                if player_radius > 100:
                    zoom_level = 0.6
            else:
                new_square_positions.append(square)
        square_positions = new_square_positions

        # Spawn new squares if needed
        if len(square_positions) < 10:
            spawn_square()

        # Draw everything
        screen.fill(WHITE)

        # Draw squares
        for square in square_positions:
            pygame.draw.rect(screen, GREEN, (square[0], square[1], square_size, square_size))

        # Draw player
        pygame.draw.circle(screen, RED, (int(player_pos[0]), int(player_pos[1])), int(player_radius))

        # Draw score
        draw_text(f"Score: {score}", font, BLACK, screen, 10, 10)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
