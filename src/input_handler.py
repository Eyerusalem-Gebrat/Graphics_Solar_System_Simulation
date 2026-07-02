import sys
import pygame
import simulation


def handle_keys(event):
    if event.type != pygame.KEYDOWN:
        return

    key = event.key

    if key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
        simulation.increase_speed()
    elif key in (pygame.K_MINUS, pygame.K_KP_MINUS):
        simulation.decrease_speed()
    elif key in (pygame.K_r, pygame.K_RSHIFT):
        simulation.reverse_time()
    elif key == pygame.K_p:
        simulation.toggle_pause()
    elif key in (pygame.K_q, pygame.K_ESCAPE):
        pygame.quit()
        sys.exit(0)