# This Python file contains the start of my Pygame learning

# Import the pygame module, which provides functionality for creating games and multimedia applications.
import pygame

# Initialize the pygame library.
pygame.init()

# Define the width and height of the game screen.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Create the game screen surface with the specified dimensions.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption (title) of the game window.
pygame.display.set_caption("Basic drawing")

# Initialize a variable 'run' to True. This will be used to control the game loop.
run = True

# Start the game loop.
while run:
    # Fill the screen with white color (255, 255, 255).
    screen.fill((255, 255, 255))
    '''
    # Experiments:
    # surface, color (red), x and y coordinates, width and height, width of rectangle, corners
    pygame.draw.rect(screen, (255, 0, 0), (200, 100, 150, 150), width=5, border_radius= 40)

    pygame.draw.rect(screen, (125, 125, 0), (300, 250, 100, 100), border_top_left_radius=75, border_bottom_right_radius=30 )
    '''
    # notice that instead of 'width=10' we just type '10'
    # pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75, 10)
    # pygame.draw.circle(screen, (255, 255, 0), (300, 200), 75, draw_top_right=True, draw_bottom_left=True)

    # Returning circles for equal values of width and height
    # pygame.draw.ellipse(screen, (0, 100, 255), (250, 150, 80, 150), 10)
    pygame.draw.arc(screen, (0, 255, 255), (250, 150, 60, 150), 0, 3.14, width=10)



    # Iterate through the list of pygame events.
    for event in pygame.event.get():
        # Check if the event type is QUIT, which is triggered when the user tries to close the window.
        if event.type == pygame.QUIT:
            # Set 'run' to 'False', to exit the game loop.
            run = False

    # Update the game display to show the changes made in this iteration.
    pygame.display.flip()

# Quit the pygame library and close the game window.
pygame.quit()