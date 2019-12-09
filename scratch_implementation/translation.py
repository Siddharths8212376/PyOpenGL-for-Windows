from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import numpy as np
import time
global anim
global width, height
global x, y, dx, dy
# decides whether animation should play or not
x, y = 0, 0

# define the translation matrix
global t_x, t_y
t_x, t_y = 200, 80
global TranslationMatrix, PositionMatrix
TranslationMatrix = [
    [1, 0, t_x],
    [0, 1, t_y],
    [0, 0, 1]
]
PositionMatrix = [
    [x],
    [y],
    [1]
]
# initailly animation is disabled
anim = 0
width, height = 500, 500
x, y = 0, 0
dx, dy = 0.0, 0.0
# extra fns to be added
# idle - decides what to do when anim = 1
# glutPostRedisplay()
# mouse function
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
            print x, y
            
def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def draw_figure(x, y):
    global dx, dy
    radius = 20
    # create the circle
    segments = 50
    

    for rad in range(segments):
        theta = 2 * 3.14159 * rad / segments
        x_ = radius *  math.cos(theta)
        y_ = radius *  math.sin(theta)
        set_pixel(x_ + x , y_ + y )

def read_in():
    global t_x, t_y
    t_x = int(input('translation x '))
    t_y = int(input('translation y '))
def plot_points():
    global x, y, dx, dy, t_x, t_y, TranslationMatrix, PositionMatrix
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    # create a ball 
    # translate it on mouse click
    # if dx <= t_x and dy <= t_y:
    #     dx += 1
    #     dy += 1
    # x += dx
    # y += dy
    current_position = [
        [x], 
        [y],
        [1]
    ]
    translation = [
        [1, 0, dx],
        [0, 1, dy], 
        [0, 0, 1]
    ]
    pos_update = np.matmul(translation, current_position)

    if dx <= abs(t_x) or dy <= abs(t_y):
        if t_x == 0 or t_y == 0:
            if t_x == 0:
                # dx += 0
                dy += 1
            else:
                # dy += 0
                dx += 1
        if t_x < 0 and t_y > 0:
            dx -= 1
            dy += 1
        elif t_y < 0 and t_x > 0:
            dy -= 1
            dx += 1
        elif t_x < 0 and t_y < 0:
            dy -= 1
            dx -= 1
        elif t_x > 0 and t_y > 0:
            dx += 1
            dy += 1
    x_update, y_update = pos_update[0][0], pos_update[1][0]
    glPushMatrix()
    draw_figure(x_update, y_update)
    glPopMatrix()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'ball_translation')
    glutDisplayFunc(plot_points)
    read_in()
    # glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()   

main()