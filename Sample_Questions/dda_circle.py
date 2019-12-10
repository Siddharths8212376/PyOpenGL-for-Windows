from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
# initialize the globals
global x_center, y_center, radius
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)
    
def dda_circle(x_c, y_c, radius):
    x = radius
    y = 0
    sx = x
    sy = y
    i = 0
    val = pow(2, i)
    while val < radius:
        i += 1
        val = pow(2, i)
        
    eps = 1 / float(pow(2, i - 1))
    
    x_2 = x + y * eps
    y_2 = y - eps * x_2
    glVertex2f(x_center + x_2, y_center - y_2)
    
    while y - sy < eps or sx - x > eps:
        x = x_2
        y = y_2
        x_2 = x + y * eps
        y_2 = y - eps * x_2
        glVertex2f(x_center + x_2, y_center - y_2)


    
    
def plot_points():
    # access the globals here
    # map and input.split() works only on python3
    
    global x_center, y_center, radius
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    x_c, y_c, rad = x_center, y_center, radius
    dda_circle(x_c, y_c, rad)
    # glVertex2f(x_c, y_c)
    glEnd()
    glFlush()
    
def get_input():  
    global x_center, y_center, radius
    x_center = int(input('enter x_center: '))
    y_center = int(input('enter y_center: '))
    radius = int(input('enter the radius: '))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot')
    get_input()
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()
    
main()