# bezier curve with n control points
# and degree = 3 as it's a cubic bezier curve
# Program to plot a point

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
    glBegin(GL_POINTS)
    P_0 = [-50, 0]
    P_1 = [100, 0]
    P_2 = [-100, 100]
    P_3 = [50, 100]
    P_4 = [-50, 0]
    P_5 = [-100, 0]
    P_6 = [100, 100]
    P_7 = [50, 100]
    
    Points = [P_0, P_1, P_2, P_3]
    Opp_Points = [P_4, P_5, P_6, P_7]
    glColor3f(0.0, 0.0, 1.0)
    for P in Opp_Points:
        glVertex2f(P[0], P[1])
    for P in Points:
        glVertex2f(P[0], P[1])
    glColor3f(0.0, 1.0, 0.0)
    for k in range(0, 100):
        t = 0.01 * k
        B_x = ((1 - t) ** 3 * P_0[0]) + (3 * (1 - t) ** 2 * t * P_1[0]) + (3 * (1 - t) * t ** 2 * P_2[0]) + (t ** 3 * P_3[0])
        B_y = ((1 - t) ** 3 * P_0[1]) + (3 * (1 - t) ** 2 * t * P_1[1]) + (3 * (1 - t) * t ** 2 * P_2[1]) + (t ** 3 * P_3[1])
        glVertex2f(B_x, B_y)
    glColor3f(1.0, 0.0, 1.0)
    
    for k in range(0, 100):
        t = 0.01 * k
        B_x_opp = ((1 - t) ** 3 * P_4[0]) + (3 * (1 - t) ** 2 * t * P_5[0]) + (3 * (1 - t) * t ** 2 * P_6[0]) + (t ** 3 * P_7[0])
        B_y_opp = ((1 - t) ** 3 * P_4[1]) + (3 * (1 - t) ** 2 * t * P_5[1]) + (3 * (1 - t) * t ** 2 * P_6[1]) + (t ** 3 * P_7[1])
        glVertex2f(B_x_opp, B_y_opp)
    
        
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

