import math
from OpenGL.GL import *


def draw_circle(x, y, radius, color, filled=True):

    glColor3f(*color)

    segments = 64

    if filled:
        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(x, y)

        for i in range(segments + 1):
            angle = 2 * math.pi * i / segments

            glVertex2f(
                x + radius * math.cos(angle),
                y + radius * math.sin(angle)
            )

        glEnd()

    else:
        glBegin(GL_LINE_LOOP)

        for i in range(segments):
            angle = 2 * math.pi * i / segments

            glVertex2f(
                x + radius * math.cos(angle),
                y + radius * math.sin(angle)
            )

        glEnd()


def draw_orbit_ring(radius, color=(0.4, 0.4, 0.4)):
    draw_circle(
        0,
        0,
        radius,
        color,
        filled=False
    )


def draw_sun(x, y, radius):

    draw_circle(
        x,
        y,
        radius * 1.4,
        (1.0, 0.8, 0.2),
        filled=True
    )

    draw_circle(
        x,
        y,
        radius,
        (1.0, 1.0, 0.0),
        filled=True
    )


def draw_body(body):

    if body.name.lower() == "sun":
        draw_sun(
            0,
            0,
            body.radius
        )

    else:
        draw_circle(
            0,
            0,
            body.radius,
            body.color,
            filled=True
        )
