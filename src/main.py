import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import simulation
import input_handler
import math_utils
from solar_system import draw_solar_system


# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Time between frames (milliseconds)
FRAME_TIME = 16      # ~60 FPS


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Enable depth testing for 3D sorting
    glEnable(GL_DEPTH_TEST)

    # Enable lighting
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Set up point light source parameters (dim ambient, bright white diffuse & specular)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.15, 0.15, 0.15, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    # Enable color material tracker so glColor calls apply to sphere materials
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)


def reshape(width, height):
    """
    Handle window resizing to update projection matrix and preserve aspect ratio.
    """
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH = width
    WINDOW_HEIGHT = height

    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Define standard 3D perspective projection
    gluPerspective(45.0, float(width) / float(height), 1.0, 1500.0)

    glMatrixMode(GL_MODELVIEW)


def display():
    """
    Render one frame in 3D.
    """
    # Clear both color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Calculate camera eye position using math_utils
    eye_x, eye_y, eye_z = math_utils.get_camera_position(
        input_handler.camera_pitch,
        input_handler.camera_yaw,
        input_handler.camera_distance,
        input_handler.camera_target
    )

    # Position camera looking at target
    gluLookAt(
        eye_x, eye_y, eye_z,
        input_handler.camera_target[0], input_handler.camera_target[1], input_handler.camera_target[2],
        0.0, 0.0, 1.0  # Z-axis is up since orbits lie in the XY plane
    )

    # Set light source position at origin in world space (inside the Sun)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 0.0, 1.0])

    # Draw the solar system bodies and orbit paths
    draw_solar_system(
        simulation.get_time(),
        simulation.get_speed()
    )

    # Draw 2D HUD status overlay on top of 3D scene
    input_handler.draw_status()

    glutSwapBuffers()


def timer(value):
    """
    Update simulation every frame.
    """
    # Advance simulation
    simulation.update(0.016)

    # Request redraw
    glutPostRedisplay()

    # Register next timer callback
    glutTimerFunc(FRAME_TIME, timer, 0)


def main():
    glutInit()

    # Explicitly request double buffering, RGB colors, and depth buffering
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    glutCreateWindow(b"3D Solar System Simulation")

    init()

    # Register callbacks
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(input_handler.keyboard)
    glutMouseFunc(input_handler.mouse_click)
    glutMotionFunc(input_handler.mouse_motion)

    glutTimerFunc(FRAME_TIME, timer, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()
