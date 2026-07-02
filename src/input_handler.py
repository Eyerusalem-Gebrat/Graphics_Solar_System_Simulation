# input_handler.py

import math
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import OpenGL.GLUT

import simulation


# 3D Camera Global Parameters
camera_distance = 450.0
camera_pitch = 45.0
camera_yaw = -45.0
camera_target = [0.0, 0.0, 0.0]

# Mouse State variables
last_x = 0
last_y = 0
active_button = None


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
        import os
        os._exit(0)


def mouse_click(button, state, x, y):
    global last_x, last_y, active_button, camera_distance

    if state == GLUT_DOWN:
        last_x = x
        last_y = y
        active_button = button

        # Scroll wheel zooms on buttons 3 (up) and 4 (down) in GLUT
        if button == 3:  # Scroll Up -> Zoom In
            camera_distance = max(20.0, camera_distance - 20.0)
            glutPostRedisplay()
        elif button == 4:  # Scroll Down -> Zoom Out
            camera_distance = min(1500.0, camera_distance + 20.0)
            glutPostRedisplay()
    else:
        active_button = None


def mouse_motion(x, y):
    global last_x, last_y, active_button, camera_pitch, camera_yaw, camera_distance

    dx = x - last_x
    dy = y - last_y

    last_x = x
    last_y = y

    # Left mouse drag rotates/orbits
    if active_button == GLUT_LEFT_BUTTON:
        camera_yaw += dx * 0.25
        camera_pitch = max(-85.0, min(85.0, camera_pitch + dy * 0.25))
        glutPostRedisplay()

    # Right mouse drag zooms
    elif active_button == GLUT_RIGHT_BUTTON:
        camera_distance = max(20.0, min(1500.0, camera_distance + dy * 1.0))
        glutPostRedisplay()


def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(
            OpenGL.GLUT.GLUT_BITMAP_HELVETICA_18,
            ord(char)
        )


def draw_status():
    speed = simulation.get_speed()
    paused = simulation.is_paused()

    # Switch to 2D Orthographic HUD projection
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    # Using a -100 to 100 ortho coordinate system
    glOrtho(-100, 100, -100, 100, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Set text color to white
    glColor3f(1.0, 1.0, 1.0)

    # Top-left status
    draw_text(-95, 90, f"Speed: {speed:.1f}x")
    if paused:
        draw_text(-95, 80, "PAUSED")

    # Top HUD controls (Three-column layout at the top)
    draw_text(-35, 90, "Mouse Controls:")
    draw_text(-35, 82, "  Left Drag  : Rotate Camera")
    draw_text(-35, 74, "  Right Drag : Zoom Camera")

    draw_text(35, 90, "Keyboard Controls:")
    draw_text(35, 82, "  P      : Toggle Pause")
    draw_text(35, 74, "  R      : Reverse Time")
    draw_text(35, 66, "  +/-    : Speed Up/Down")
    draw_text(35, 58, "  Q      : Quit")

    # Restore 3D projection and modelview matrices
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)

