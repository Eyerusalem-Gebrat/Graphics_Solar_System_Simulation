# solar_system.py

import math

from OpenGL.GL import *

from celestial_body import sun
from render import draw_body, draw_orbit_ring


def render_body(body, sim_time, speed_multiplier):
    """
    Recursively render a celestial body and its children.
    """

    glPushMatrix()

    # Draw orbit path (skip Sun)
    if body.orbit_radius > 0:
        draw_orbit_ring(body.orbit_radius)

    # Orbit angle
    angle = sim_time * body.orbit_speed * speed_multiplier

    # Orbit position
    x = math.cos(angle) * body.orbit_radius
    y = math.sin(angle) * body.orbit_radius

    glTranslatef(x, y, 0)

    # Self rotation
    rotation = sim_time * body.rotation_speed
    glRotatef(rotation, 0, 0, 1)

    # Draw body
    draw_body(body)

    # Draw moons / child bodies
    for child in body.children:
        render_body(
            child,
            sim_time,
            speed_multiplier
        )

    glPopMatrix()


def draw_solar_system(sim_time, speed_multiplier):
    """
    Start rendering from the Sun.
    """

    render_body(
        sun,
        sim_time,
        speed_multiplier
    )
