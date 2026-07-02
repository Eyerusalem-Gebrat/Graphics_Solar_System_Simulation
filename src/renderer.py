import pygame
import math

TILT = 0.38


def draw_stars(surface, stars):
    for (x, y, brightness) in stars:
        pygame.draw.circle(surface, (brightness, brightness, brightness), (x, y), 1)


def draw_orbit_ring(surface, cx, cy, orbit_radius):
    segments = 120
    points = []
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = cx + orbit_radius * math.cos(angle)
        y = cy + orbit_radius * math.sin(angle) * TILT
        points.append((int(x), int(y)))
    pygame.draw.polygon(surface, (40, 40, 90), points, 1)


def draw_planet(surface, x, y, radius, color, is_sun=False):
    ix, iy, ir = int(x), int(y), int(radius)

    if is_sun:
        # Glow layers
        for glow in range(5, 0, -1):
            alpha_surf = pygame.Surface(
                (ir * 2 + glow * 14, ir * 2 + glow * 14), pygame.SRCALPHA
            )
            glow_alpha = max(0, 35 - glow * 6)
            pygame.draw.circle(
                alpha_surf,
                (255, 160, 0, glow_alpha),
                (ir + glow * 7, ir + glow * 7),
                ir + glow * 7
            )
            surface.blit(alpha_surf, (ix - ir - glow * 7, iy - ir - glow * 7))

        # Sun core
        pygame.draw.circle(surface, (255, 220, 0), (ix, iy), ir)
        # Bright center
        pygame.draw.circle(surface, (255, 255, 180), (ix, iy), ir // 2)

    else:
        # Base color
        pygame.draw.circle(surface, color, (ix, iy), ir)

        # Highlight top-left
        highlight = (
            min(255, color[0] + 80),
            min(255, color[1] + 80),
            min(255, color[2] + 80)
        )
        pygame.draw.circle(
            surface, highlight,
            (ix - ir // 3, iy - ir // 3),
            max(1, ir // 3)
        )

        # Shadow bottom-right
        shadow_surf = pygame.Surface((ir * 2, ir * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            shadow_surf, (0, 0, 0, 140),
            (ir + ir // 4, ir + ir // 4),
            ir
        )
        surface.blit(shadow_surf, (ix - ir, iy - ir))


def draw_saturn_rings(surface, x, y, radius):
    ix, iy = int(x), int(y)
    for ring_r in range(int(radius * 1.4), int(radius * 2.2), 4):
        points = []
        for i in range(80):
            angle = 2 * math.pi * i / 80
            rx = ix + ring_r * math.cos(angle)
            ry = iy + ring_r * math.sin(angle) * TILT * 0.6
            points.append((int(rx), int(ry)))
        pygame.draw.polygon(surface, (180, 160, 100), points, 1)