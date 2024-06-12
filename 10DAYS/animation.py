import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cinematic Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# Fonts
title_font = pygame.font.Font(None, 74)
cast_font = pygame.font.Font(None, 48)

# Movie and cast details
movie_name = "Batman Vs Superman"
cast = ["Starring..","Ben Affleck", "Henry Cavill"]

def draw_text(text, font, color, center):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    screen.blit(text_surface, text_rect)

def main():
    clock = pygame.time.Clock()
    running = True
    start_time = time.time()
    fade_duration = 2  # Duration for the fade effect (seconds)

    while running:
        screen.fill(BLACK)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Fade-in effect
        if elapsed_time < fade_duration:
            alpha = min(255, int(255 * (elapsed_time / fade_duration)))
        else:
            alpha = 255

        # Title and cast display timing
        if elapsed_time < 3:
            title_alpha = alpha
            cast_alpha = 0
        elif elapsed_time < 6:
            title_alpha = max(0, 255 - int(255 * ((elapsed_time - 3) / fade_duration)))
            cast_alpha = alpha
        else:
            title_alpha = 0
            cast_alpha = 255

        # Draw title
        title_surface = title_font.render(movie_name, True, GOLD)
        title_surface.set_alpha(title_alpha)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 4))

        # Draw cast
        for i, member in enumerate(cast):
            cast_surface = cast_font.render(member, True, WHITE)
            cast_surface.set_alpha(cast_alpha)
            screen.blit(cast_surface, (WIDTH // 2 - cast_surface.get_width() // 2, HEIGHT // 2 + i * 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
