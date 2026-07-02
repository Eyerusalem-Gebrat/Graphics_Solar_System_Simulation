import math
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_orbit_ring(radius, color=(0.4, 0.4, 0.4)):
    """
    Draw a flat circular orbital ring in 3D (XY plane) with lighting disabled.
    """
    glDisable(GL_LIGHTING)
    glColor3f(*color)

    segments = 128
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        glVertex3f(radius * math.cos(angle), radius * math.sin(angle), 0.0)
    glEnd()

    glEnable(GL_LIGHTING)


def draw_sun(radius):
    """
    Draw the Sun as a luminous, unshaded body (corona and core spheres).
    """
    glDisable(GL_LIGHTING)

    # Luminous Sun corona (outer glow)
    glColor3f(1.0, 0.8, 0.2)
    glutSolidSphere(radius * 1.2, 32, 32)

    # Luminous Sun core
    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(radius, 32, 32)

    glEnable(GL_LIGHTING)


def draw_body(body):
    """
    Draw a celestial body (Sun, regular planet, or Saturn with its custom rings).
    """
    name_lower = body.name.lower()

    if name_lower == "sun":
        draw_sun(body.radius)

    elif name_lower == "saturn":
        # Draw Saturn sphere
        glEnable(GL_LIGHTING)
        glColor3f(*body.color)
        glutSolidSphere(body.radius, 32, 32)

        # Draw Saturn's rings (dusty flat disc in XY plane)
        glDisable(GL_LIGHTING)
        glColor3f(0.75, 0.70, 0.55)
        segments = 64
        # Draw multiple concentric rings to simulate a solid/textured ring structure
        for r_factor in [1.35, 1.45, 1.55, 1.65, 1.75, 1.85]:
            glBegin(GL_LINE_LOOP)
            for i in range(segments):
                angle = 2 * math.pi * i / segments
                glVertex3f(body.radius * r_factor * math.cos(angle), body.radius * r_factor * math.sin(angle), 0.0)
            glEnd()
        glEnable(GL_LIGHTING)

    else:
        # Standard planet or moon
        glEnable(GL_LIGHTING)
        glColor3f(*body.color)
        glutSolidSphere(body.radius, 32, 32)

