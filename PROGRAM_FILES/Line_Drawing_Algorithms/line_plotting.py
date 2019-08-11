#Program to plot a point
from line_algorithms import midpoint_line, dda_line, bresenham_line

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    # plot_midpoint_line(P_init, P_final)
    # plot_midpoint_line([1, 100], [15, 200])
    
    for each_elem in Coordinates:
        # midpoint_line(each_elem[0], each_elem[1])
        # bresenham_line(each_elem[0], each_elem[1])
        dda_line(each_elem[0], each_elem[1])
    glEnd()
    glFlush()


def get_line(Set_Coords):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    global Coordinates
    Coordinates = Set_Coords
    glutCreateWindow(b'basic_line_drawing_algorithms')
    glutDisplayFunc(display)
    init()
    glutMainLoop()





