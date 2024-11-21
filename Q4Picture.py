# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import sys
import pygame
# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Q4Picture - Beach Scene")

# Define colors
SKY_BLUE = (135, 206, 235)
YELLOW = (255, 223, 0)
OCEAN_BLUE = (0, 105, 148)
SAND_COLOR = (238, 214, 175)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with sky color
    screen.fill(SKY_BLUE)

    # Draw the sun (circle)
    pygame.draw.circle(screen, YELLOW, (700, 100), 60)

    # Draw the ocean (rectangle)
    pygame.draw.rect(screen, OCEAN_BLUE, (0, 300, WIDTH, 200))

    # Draw the sand (rectangle)
    pygame.draw.rect(screen, SAND_COLOR, (0, 500, WIDTH, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()