#Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

list_of_num = []
for i in range(250):
    list_of_num.append(i)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)


def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    for each_elem in list_of_num:
        glVertex(each_elem, -75.0)
        glVertex(-each_elem, -75.0)
    radius = 75
    segments = 500
    x_init, y_init = 0.0, 0.0
    for x_dist in range(5):
        for rad in range(segments):
            theta = 2 * 3.14159 * rad / segments
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            glVertex(x + x_dist * 10, y + y_init)
    # make a freaking cuboid out of points

    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot_all_points')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()


main()

