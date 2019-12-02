#Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
# from line_algorithm import line_algorithm
global P_in, P_f
P_in, P_f = [0, 0], [100, 100]
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def dda_plot(P_init, P_final):
    
    x_init, y_init = P_init
    x_final, y_final = P_final
    dx = x_final - x_init
    dy = y_final - y_init

    # depending upon the absolute values of dx and dy 
    # choose the number of steps to put pixel as
    steps = int(abs(dx) if abs(dx) > abs(dy) else abs(dy))

    # calculate increment in x and y for each steps
    x_inc = dx / float(steps)
    y_inc = dy / float(steps)
    x, y = x_init, y_init

    # add pixel for each step
    for i in range(steps + 1):
        glVertex2f(x, y)
        x += x_inc
        y += y_inc
        
def take_in():
    x0 = int(input())
    y0 = int(input())
    x1 = int(input())
    y1 = int(input())
    global P_in, P_f
    
    P_in, P_f = [x0, y0], [x1, y1]
    
def plot_points():
    global P_in, P_f
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    P_init, P_final = P_in, P_f

    dda_plot(P_init, P_final)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot_all_points')
    glutDisplayFunc(plot_points)
    take_in()
    init()
    glutMainLoop()


main()

