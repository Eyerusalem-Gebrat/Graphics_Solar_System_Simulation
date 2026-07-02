from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import simulation
import input_handler
from solar_system import draw_solar_system


# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAME_TIME = 16  


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(-250, 250, -250, 250, -1, 1)

    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_solar_system(
        simulation.get_time(),
        simulation.get_speed()
    )

    input_handler.draw_status()

    glutSwapBuffers()


def timer(value):
    simulation.update(0.016)
    glutPostRedisplay()
    glutTimerFunc(FRAME_TIME, timer, 0)


def main():

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"2D Solar System Simulation")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(input_handler.keyboard)
    glutTimerFunc(FRAME_TIME, timer, 0)
    glutMainLoop()


if __name__ == "__main__":
    main()
