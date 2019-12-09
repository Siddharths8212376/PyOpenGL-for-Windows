from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import numpy as np
import time
global anim
global width, height
from Algorithms.circle_algorithms import circle_algorithms
global x0, y0, x1, y1, x2, y2
x0, y0 = 0, 100
x1, y1 = 100, 0
x2, y2 = -100, 0
global origin_x, origin_y
origin_x, origin_y = 0, 0
global radius
radius = 50
global theta
theta = 0

anim = 0
width, height = 500, 500
global t_x, t_y, dx, dy
t_x, t_y = 50,0
dx, dy = 0, 0

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

def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()
  
def draw_circle():
    global origin_x, origin_y, radius
    
    segments = 500
    for rad in range(segments):
        angle = 2 * 3.14159 * rad / float(segments)
        x_ = radius * math.cos(angle)
        y_ = radius * math.cos(angle)
        set_pixel(x_  + origin_x , y_ + origin_y )

def dda_line(P_init, P_final):
    x_init, y_init = P_init
    x_final, y_final = P_final
    
    dx = x_final - x_init
    dy = y_final - y_init
    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    x_inc, y_inc = dx / float(steps) , dy / float(steps)
    x, y = x_init, y_init
    for i in range(int(steps) + 1):
        set_pixel(x, y)
        x += x_inc
        y += y_inc


def draw_triangle():
    global x0, y0, x1, y1, x2, y2
    global origin_x, origin_y
    glBegin(GL_LINES)
    
    glVertex2f(origin_x, origin_y)
    glVertex2f(x0, y0)
    
    glVertex2f(origin_x, origin_y)
    glVertex2f(x1, y1)

    glVertex2f(origin_x, origin_y)
    glVertex2f(x2, y2)
    
    glEnd()
    glFlush()



def rotate_and_translate():
    global theta, x0, y0, x1, y1, x2, y2, dx, dy
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
    translation_matrix = [
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ]
    transformation_matrix = np.matmul(translation_matrix, rotation_matrix)
    
    updated_position_0 = np.matmul(transformation_matrix, current_position_0)
    updated_position_1 = np.matmul(transformation_matrix, current_position_1)
    updated_position_2 = np.matmul(transformation_matrix, current_position_2)
    x0 = updated_position_0[0][0]
    y0 = updated_position_0[1][0]
    x1 = updated_position_1[0][0]
    y1 = updated_position_1[1][0]
    x2 = updated_position_2[0][0]
    y2 = updated_position_2[1][0]
    
    
def plot_points():
    global theta, origin_x, origin_y, t_x, t_y, dx, dy
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)


    glPushMatrix()
    draw_triangle()
    glBegin(GL_POINTS)
    circle = circle_algorithms(100, origin_x, origin_y)
    circle.bresenham_circle()
    glEnd()
    glFlush()
    
    if dx <= abs(t_x) or dy <= abs(t_y):
        if t_x == 0 or t_y == 0:
            if t_x == 0:
                # dx += 0
                dy += 0.001
            else:
                # dy += 0
                dx += 0.001
        if t_x < 0 and t_y > 0:
            dx -= 0.001
            dy += 0.001
        elif t_y < 0 and t_x > 0:
            dy -= 0.001
            dx += 0.001
        elif t_x < 0 and t_y < 0:
            dy -= 0.001
            dx -= 0.001
        elif t_x > 0 and t_y > 0:
            dx += 0.001
            dy += 0.001
    origin_x += dx
    origin_y += dy
    
    if theta < 2 * math.pi:
        theta += 0.0001
    else:
        theta = 0
    
    
    rotate_and_translate()
    glPopMatrix()
    

    
    # draw_circle()


    
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