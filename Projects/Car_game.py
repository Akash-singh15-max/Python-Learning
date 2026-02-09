import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load assets
car_img = pygame.image.load("images/car.png")  # Load your car image (50x100 px recommended)
car_width, car_height = 50, 100
car_img = pygame.transform.scale(car_img, (car_width, car_height))

# Game variables
clock = pygame.time.Clock()
car_x, car_y = WIDTH // 2 - car_width // 2, HEIGHT - 150
car_speed = 5

# Obstacles
obstacle_width, obstacle_height = 50, 100
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed
    
    # Move obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        score += 1
        obstacle_speed += 0.2  # Increase speed over time
    
    # Collision detection
    if (car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and
            car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y):
        print("Game Over! Final Score:", score)
        running = False
    
    # Draw elements
    screen.blit(car_img, (car_x, car_y))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
