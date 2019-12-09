from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import numpy as np
import time
global anim
global width, height

global x0, y0, x1, y1, x2, y2
x0, y0 = -100, -100
x1, y1 = 100, -100
x2, y2 = 0, 100

global theta
theta = 0

anim = 0
width, height = 500, 500

def init():
    global width, height
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-width / 2, width / 2, -height / 2, height / 2)

def idle():
    if anim == 1:
        glutPostRedisplay()
        
# define change state
def change_state():
    global anim
    if anim == 0:
        anim = 1
    else:
        anim = 0

def mouse(btn, state, x, y):
    if btn == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            change_state()

            


def draw_triangle():
    global x0, y0, x1, y1, x2, y2
    glBegin(GL_LINE_LOOP)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glFlush()

def rotate_triangle():
    global theta, x0, y0, x1, y1, x2, y2
    current_position_0 = [
        [x0],
        [y0],
        [1]
    ]
    current_position_1 = [
        [x1],
        [y1],
        [1]
    ]
    current_position_2 = [
        [x2],
        [y2],
        [1]
    ]
    rotation_matrix = [
        [math.cos(theta), -1 * math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ]
    
    updated_position_0 = np.matmul(rotation_matrix, current_position_0)
    updated_position_1 = np.matmul(rotation_matrix, current_position_1)
    updated_position_2 = np.matmul(rotation_matrix, current_position_2)
    x0 = updated_position_0[0][0]
    y0 = updated_position_0[1][0]
    x1 = updated_position_1[0][0]
    y1 = updated_position_1[1][0]
    x2 = updated_position_2[0][0]
    y2 = updated_position_2[1][0]
    
    
def plot_points():
    global theta
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)


    glPushMatrix()
    draw_triangle()
    glPopMatrix()
    if theta < 2 * math.pi:
        theta += 0.0001
    else:
        theta = 0
        
    rotate_triangle()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'rotation')
    glutDisplayFunc(plot_points)

    glutIdleFunc(idle)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()   

main()