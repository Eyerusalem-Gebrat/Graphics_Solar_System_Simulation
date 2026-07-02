import pygame
import sys
import random

import simulation
from solar_system import draw_solar_system
from input_handler import handle_keys
from renderer import draw_stars

WIDTH, HEIGHT = 1920, 1080
FPS = 60


def generate_stars(width, height, count=300):
    stars = []
    for _ in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        brightness = random.randint(100, 255)
        stars.append((x, y, brightness))
    return stars


def draw_status(surface, font, speed, paused):
    surface.blit(
        font.render(f"Speed: {speed:.1f}x", True, (255, 255, 255)), (20, 20)
    )
    surface.blit(
        font.render(
            "Controls:  +/-  Speed  |  P  Pause  |  R  Reverse  |  Q  Quit",
            True, (180, 180, 180)
        ), (20, 50)
    )
    if paused:
        surface.blit(font.render("PAUSED", True, (255, 80, 80)), (20, 80))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Solar System Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 22)

    # True center of screen
    cx = screen.get_width() // 2
    cy = screen.get_height() // 2

    stars = generate_stars(screen.get_width(), screen.get_height(), 300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                handle_keys(event)

        dt = clock.tick(FPS) / 1000.0
        simulation.update(dt)

        screen.fill((5, 5, 15))
        draw_stars(screen, stars)

        draw_solar_system(
            screen, cx, cy,
            simulation.get_time(),
            simulation.get_speed()
        )

        draw_status(screen, font, simulation.get_speed(), simulation.is_paused())
        pygame.display.flip()


if __name__ == "__main__":
    main()