# input_handler.py

from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

import simulation


def keyboard(key, x, y):

    key = key.decode("utf-8")

    if key == "+":
        simulation.increase_speed()

    elif key == "-":
        simulation.decrease_speed()

    elif key == "r":
        simulation.reverse_time()

    elif key == "p":
        simulation.toggle_pause()

    elif key == "q":
        sys.exit()

    elif ord(key) == 27:   # ESC key
        sys.exit()


def draw_text(x, y, text):

    glRasterPos2f(x, y)

    for char in text:
        glutBitmapCharacter(
            GLUT_BITMAP_HELVETICA_18,
            ord(char)
        )


def draw_status():

    speed = simulation.get_speed()
    paused = simulation.is_paused()

    draw_text(-95, 90, f"Speed: {speed:.1f}x")

    if paused:
        draw_text(-95, 80, "PAUSED")
