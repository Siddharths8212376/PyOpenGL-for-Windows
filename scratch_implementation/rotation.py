from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import numpy as np
import time
global anim
global width, height

global x, y
x, y = 100, 100

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

            


def draw_line():
    global x, y
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def rotate_line():
    global theta, x, y
    current_position = [
        [x],
        [y],
        [1]
    ]
    rotation_matrix = [
        [math.cos(theta), -1 * math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ]
    
    updated_position = np.matmul(rotation_matrix, current_position)
    x = updated_position[0][0]
    y = updated_position[1][0]
    
    
def plot_points():
    global x, y, theta
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)


    glPushMatrix()
    draw_line()
    glPopMatrix()
    if theta < 2 * math.pi:
        theta += 0.0001
    else:
        theta = 0
        
    rotate_line()

    
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