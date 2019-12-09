from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import time
import numpy as np
global anim
global width, height
global x, y, dx, dy
global draw_circum
draw_circum = True
# decides whether animation should play or not
x, y = 0, 0

# define the translation matrix
global t_x, t_y
t_x, t_y = 200, 80
global TranslationMatrix, PositionMatrix
# acceleration due to gravity
global g
g = 9.81
# initial velocity and theta in radians
global theta, u, angle, circum_radius
circum_radius = 80
angle = 0
u = 50
theta = 3.14159 / float(6)
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

def create_base():
    global circum_radius
    segments = 500
    x_c, y_c = 0, 0
    for rad in range(segments):
        theta = 2 * 3.14159 * rad / float(segments)
        x_ = (circum_radius - 20) * math.cos(theta)
        y_ = (circum_radius - 20)* math.sin(theta)
        set_pixel(x_ + x_c , y_ + y_c)
def draw_figure(x, y):
    global dx, dy
    radius = 20
    # create the circle
    segments = 200
    for rad in range(segments):
        theta = 2 * 3.14159 * rad / float(segments)
        x_ = radius *  math.cos(theta)
        y_ = radius *  math.sin(theta)
        set_pixel(x_ + x , y_ + y )
def read_in():
    global t_x, t_y
    t_x = int(input('translation x '))
    t_y = int(input('translation y '))
def plot_points():
    global x, y, dx, dy, t_x, t_y, TranslationMatrix, PositionMatrix, draw_circum
    global g, u, theta, angle, circum_radius
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    # create a ball 
    if angle < 2 * math.pi:
        angle += 0.1
    else:
        angle = 0
    # add the circular path
    dx = circum_radius * math.cos(angle)
    dy = circum_radius * math.sin(angle)
    # if draw_circum is True:
    create_base()
        # draw_circum = False
    glColor3f(1.0, 0.0, 1.0)
    glPushMatrix()
    # draw_figure(x_update, y_update)
    time.sleep(0.04)
    draw_figure(dx, dy)
    glPopMatrix()
    # glutSwapBuffers()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'ball_translation')
    glutDisplayFunc(plot_points)
    # read_in()
    # glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()   

main()