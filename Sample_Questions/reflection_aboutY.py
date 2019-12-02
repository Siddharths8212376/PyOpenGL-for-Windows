# reflection about an axis parallel to y
# passing through p = (30, 10)
# therefore line x = 30
# Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from Algorithms.line_algorithm import line_algorithm
# from line_algorithm import line_algorithm

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-350.0, 350.0, -350.0, 350.0)

def draw_triangle(P, Q, R):
    P_Q = line_algorithm(P, Q)
    Q_R = line_algorithm(Q, R)
    R_P = line_algorithm(R, P)
    P_Q.dda_line()
    Q_R.dda_line()
    R_P.dda_line()
    
def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POINTS)
    P = [80, 50]
    Q = [60, 10]
    R = [100, 10]
    draw_triangle(P, Q, R)
    
    # reflection about y_axis + delta change in x
    # x_new = -1 * x + delta
    # draw line x = 30
    delta = 30
    axis = line_algorithm([delta/2, 200], [delta/2, -200])
    glColor3f(1.0, 0.0, 1.0)
    axis.dda_line()

    P_ref = [-1 * P[0] + delta, P[1]]
    Q_ref = [-1 * Q[0] + delta, Q[1]]
    R_ref = [-1 * R[0] + delta, R[1]]
    glColor3f(0.0, 1.0, 1.0)
    draw_triangle(P_ref, Q_ref, R_ref)
    glEnd()
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

