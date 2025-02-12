import pygame
import random
import math

# Initialize Pygame
pygame.init()

class Game:
    def __init__(self):
        # Window setup
        self.base_width = 800
        self.base_height = 600
        self.width = self.base_width
        self.height = self.base_height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Growing Circle Game")
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 100, 255)
        
        # Player properties
        self.player_radius = 20
        self.player_x = self.width // 2
        self.player_y = self.height // 2
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.5
        self.friction = 0.98
        
        # Game properties
        self.score = 0
        self.squares = []
        self.square_size = 20
        self.zoom_level = 1
        self.spawn_timer = 0
        self.font = pygame.font.Font(None, 36)
        
        # Generate initial squares
        for _ in range(5):
            self.spawn_square()

    def spawn_square(self):
        x = random.randint(0, self.width - self.square_size)
        y = random.randint(0, self.height - self.square_size)
        self.squares.append(pygame.Rect(x, y, self.square_size, self.square_size))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration
        if keys[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration
        if keys[pygame.K_UP]:
            self.velocity_y -= self.acceleration
        if keys[pygame.K_DOWN]:
            self.velocity_y += self.acceleration

    def update(self):
        # Update player position with momentum
        self.velocity_x *= self.friction
        self.velocity_y *= self.friction
        
        self.player_x += self.velocity_x
        self.player_y += self.velocity_y
        
        # Keep player in bounds
        self.player_x = max(self.player_radius, min(self.width - self.player_radius, self.player_x))
        self.player_y = max(self.player_radius, min(self.height - self.player_radius, self.player_y))
        
        # Check collision with squares
        player_rect = pygame.Rect(
            self.player_x - self.player_radius,
            self.player_y - self.player_radius,
            self.player_radius * 2,
            self.player_radius * 2
        )
        
        squares_to_remove = []
        for square in self.squares:
            if player_rect.colliderect(square):
                squares_to_remove.append(square)
                self.score += 10
                self.player_radius += 2
        
        # Remove collected squares
        for square in squares_to_remove:
            self.squares.remove(square)
        
        # Spawn new squares periodically
        self.spawn_timer += 1
        if self.spawn_timer >= 60:  # Spawn every 60 frames
            self.spawn_square()
            self.spawn_timer = 0
        
        # Update zoom based on player size
        target_zoom = max(1, self.player_radius / 20)
        self.zoom_level = 0.95 * self.zoom_level + 0.05 * target_zoom
        
        # Update window size based on zoom
        self.width = int(self.base_width * self.zoom_level)
        self.height = int(self.base_height * self.zoom_level)
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        self.screen.fill(self.BLACK)
        
        # Draw squares
        for square in self.squares:
            scaled_rect = pygame.Rect(
                square.x / self.zoom_level,
                square.y / self.zoom_level,
                self.square_size / self.zoom_level,
                self.square_size / self.zoom_level
            )
            pygame.draw.rect(self.screen, self.RED, scaled_rect)
        
        # Draw player
        scaled_radius = self.player_radius / self.zoom_level
        pygame.draw.circle(
            self.screen,
            self.BLUE,
            (int(self.player_x / self.zoom_level), int(self.player_y / self.zoom_level)),
            int(scaled_radius)
        )
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw size indicator
        size_text = self.font.render(f"Size: {int(self.player_radius)}", True, self.WHITE)
        self.screen.blit(size_text, (10, 50))
        
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.handle_input()
            self.update()
            self.draw()
            clock.tick(60)
        
        pygame.quit()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()