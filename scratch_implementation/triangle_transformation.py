from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

global anim, x0, y0, x1, y1, x2, y2, radius
global x_center, y_center, a
x_center, y_center = 50, 50
anim = 0
x0, y0 = 0, 0
x1, y1 = 100, 100
global rad
rad = 0
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)

# idle function
def idle():
    if anim == 1:
        glutPostRedisplay()
def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()
# dda line function
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

def draw_triangle(x0, y0, x1, y1):
    global x_center, y_center
    a = math.sqrt((y1 - y0) ** 2 + (x1 - x0) ** 2)
    print a
    x2 = (x0 + x1 + math.sqrt(3) * (y1 - y0)) / float(2)
    y2 = (y0 + y1 + math.sqrt(3) * (x1 - x0)) / float(2)
    print x2, y2
    P1 = [x0, y0]
    P2 = [x1, y1]
    P3 = [x2, y2]
    dda_line(P1, P2)
    dda_line(P2, P3)
    dda_line(P3, P1)
    
    # x_center = x0 + a / float(2)
    # y_center = a / float(2 * math.sqrt(3))
    # radius = a ** 3 / float(math.sqrt((3 * a ** 4))
# def draw_fig():
#     global x0, y0, x1, y1, x2, y2
#     dda_line([x0, y0], [x1, y1])
#     dda_line([x1, y1], [x2, y2])
#     dda_line([x2, y2], [x0, y0])

# def update_pos():
#     global x0, y0, x1, y1, x2, y2, rad, x_center, y_center
    
#     theta = 2 * 3.14159 * rad 
#     x0 = x0 * math.cos(theta)
#     y0 = y0 * math.sin(theta)
#     x1 = x1 * math.cos(theta)
#     y1 = y1 * math.sin(theta)
#     x2 = x2 * math.cos(theta)
#     y2 = y2 * math.sin(theta)
    
    
def rotate_triangle():
    global x0, y0, x1, y1, rad, x_center, y_center
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    # draw_triangle(x0, y0, x1, y1)
    rad += 0.001
    glPushMatrix()
    # update_pos()
    draw_triangle(x_center + x0, y_center + y0, x_center + x1, y_center + y1)
    glPopMatrix()
    if rad == 1:
        rad = 0
    theta = 2 * 3.14159 * rad
    x0 = (x0 - x_center) * math.cos(theta) - (y0 - y_center) * math.sin(theta)
    y0 = (y0 - y_center) * math.cos(theta) - (x0 - x_center) * math.cos(theta)
    
    x1 = (x1 - x_center) * math.cos(theta) - (y1 - y_center) * math.sin(theta)
    y1 = (y1 - y_center) * math.cos(theta) - (x1 - x_center) * math.cos(theta)
    # a = math.sqrt((y1 - y0) ** 2 + (x1 - x0) ** 2)
    # x0 = a / (float(math.sqrt(3)) * math.cos(theta))
    # y0 = a / (float(math.sqrt(3)) * math.sin(theta))

def change_state():
    global anim
    if anim == 0:
        anim = 1
    else:
        anim = 0

def mouse(btn, state, x, y):
    y = 500 - y
    if btn == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            change_state()
            
def user_input():
    global x0, y0, x1, y1
    x0 = int(input('enter xo'))
    y0 = int(input('enter yo'))
    x1 = int(input('enter x1'))
    y1 = int(input('enter y1'))
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'rotate_triangle')
    user_input()
    glutDisplayFunc(rotate_triangle)
    glutMouseFunc(mouse)
    glutIdleFunc(idle)
    
    init()
    glutMainLoop()   

main()