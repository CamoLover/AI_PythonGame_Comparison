import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
PLAYER_COLOR = (0, 128, 255)
SQUARE_COLOR = (255, 50, 50)
BG_COLOR = (30, 30, 30)
FONT_COLOR = (255, 255, 255)
MAX_SQUARES = 20
BASE_SQUARE_SIZE = 10
MIN_SCALE = 0.5
BASE_RADIUS = 15

# Setup Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Eater")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = BASE_RADIUS
        self.vel_x = 0
        self.vel_y = 0
        self.acceleration = 0.5
        self.friction = 0.92

    def move(self, dx, dy):
        self.vel_x += dx * self.acceleration
        self.vel_y += dy * self.acceleration

        # Limit maximum speed
        speed = math.hypot(self.vel_x, self.vel_y)
        max_speed = 8 + self.radius/5
        if speed > max_speed:
            scale = max_speed / speed
            self.vel_x *= scale
            self.vel_y *= scale

    def update(self):
        self.vel_x *= self.friction
        self.vel_y *= self.friction
        self.x += self.vel_x
        self.y += self.vel_y

class Game:
    def __init__(self):
        self.player = Player()
        self.squares = []
        self.score = 0
        self.scale = 1.0
        self.camera_x = 0
        self.camera_y = 0
        self.generate_squares()

    def generate_squares(self):
        while len(self.squares) < MAX_SQUARES:
            x = random.randint(-1000, 1000)
            y = random.randint(-1000, 1000)
            self.squares.append((x, y))

    def apply_camera(self, surface):
        scaled_w = int(WIDTH * self.scale)
        scaled_h = int(HEIGHT * self.scale)
        scaled_surface = pygame.transform.scale(surface, (scaled_w, scaled_h))
        
        screen.blit(scaled_surface, (
            -self.camera_x * (self.scale - 1),
            -self.camera_y * (self.scale - 1)
        ))

    def update_camera(self):
        # Center camera on player with smoothing
        target_x = self.player.x - WIDTH//2
        target_y = self.player.y - HEIGHT//2
        self.camera_x += (target_x - self.camera_x) * 0.1
        self.camera_y += (target_y - self.camera_y) * 0.1

        # Update scale based on player size
        self.scale = max(MIN_SCALE, 1 / (1 + self.player.radius / 100))

    def check_collisions(self):
        new_squares = []
        for (sx, sy) in self.squares:
            dx = sx - self.player.x
            dy = sy - self.player.y
            distance = math.hypot(dx, dy)
            
            if distance < self.player.radius + BASE_SQUARE_SIZE:
                self.player.radius += 0.5
                self.score += 10
            else:
                new_squares.append((sx, sy))
        
        self.squares = new_squares
        self.generate_squares()

    def draw(self, surface):
        surface.fill(BG_COLOR)
        
        # Draw squares
        for sx, sy in self.squares:
            pygame.draw.rect(surface, SQUARE_COLOR, 
                (sx - BASE_SQUARE_SIZE//2, sy - BASE_SQUARE_SIZE//2,
                 BASE_SQUARE_SIZE, BASE_SQUARE_SIZE))
        
        # Draw player
        pygame.draw.circle(surface, PLAYER_COLOR,
            (int(self.player.x), int(self.player.y)),
            int(self.player.radius))

        # Draw UI
        score_text = font.render(f"Score: {self.score}", True, FONT_COLOR)
        size_text = font.render(f"Size: {int(self.player.radius)}", True, FONT_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(size_text, (10, 50))

    def run(self):
        game_surface = pygame.Surface((WIDTH, HEIGHT))
        running = True
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Handle input
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT]:
                dx -= 1
            if keys[pygame.K_RIGHT]:
                dx += 1
            if keys[pygame.K_UP]:
                dy -= 1
            if keys[pygame.K_DOWN]:
                dy += 1
            
            self.player.move(dx, dy)
            self.player.update()
            self.check_collisions()
            self.update_camera()
            
            # Drawing
            self.draw(game_surface)
            self.apply_camera(game_surface)
            
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()