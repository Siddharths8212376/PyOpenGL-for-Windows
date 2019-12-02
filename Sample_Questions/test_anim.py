
#Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
# from line_algorithm import line_algorithm

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-350.0, 350.0, -350.0, 350.0)


def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    timeSinceStart = glutGet(GLUT_ELAPSED_TIME)
    # glTranslatef(50, 50, 0.0)
    
    glBegin(GL_POINTS)
    segments = 500
    radius = 50
    x_centre, y_centre = 0, 0
    for rad in range(segments):
        theta = 2 * 3.14159 * rad / segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x + x_centre, y + y_centre)

    glEnd()

    glTranslatef(timeSinceStart * 0.002, 200, 0.0)
    
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot_all_points')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()


main()



