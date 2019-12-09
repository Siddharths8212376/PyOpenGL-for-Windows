# cohen sutherland line clipping
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

# declare the globals 
global lines, n, clipped_lines
global x_min, y_min, x_max, y_max
# clipping window coordinate set
x_min, y_min = 0, 0
x_max, y_max = 100, 200
n = 0
lines = []
clipped_lines = []

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# compute the code
def compute_code(x, y):
    
    # find the region code T, B, R, L

    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
        
    return code

# clipping
def cohen_sutherland_clip(P_init, P_final, clip_window):
    global clipped_lines
    x_init, y_init = P_init
    x_final, y_final = P_final

    code_init = compute_code(x_init, y_init)
    code_final = compute_code(x_final, y_final)
    
    accept = False
    
    while True:
        
        # if both endpoints lie inside
        if code_init == 0 and code_final == 0:
            accept = True
            break
        # if both endpoints are outside
        elif code_init & code_final != 0:
            break
        
        # some part lies inside
        # select the side that's outside
        if code_init != 0:
            code_out = code_init
        else:
            code_out = code_final
            
        x, y = 1.0, 1.0
        # find the intersection
        m = (y_final - y_init) / float(x_final - x_init)
        c = y_init - m * x_init
        if code_out & TOP:
            y = y_max
            x = 1 / float(m) * (y - c)
        
        elif code_out & BOTTOM:
            y = y_min
            x = 1 / float(m) * (y - c)
        
        elif code_out & LEFT:
            x = x_min 
            y = m * x + c
        
        elif code_out & RIGHT:
            x = x_max
            y = m * x + c
            
        # now intersection point is found
        # we replace point outside window
        # with the intersection point
        
        if code_out == code_init:
            x_init = x
            y_init = y
            code_init = compute_code(x_init, y_init)
        
        else:
            x_final = x
            y_final = y
            code_final = compute_code(x_final, y_final)
            
    P_in = x_init, y_init
    P_f = x_final, y_final
    if accept:
        return P_in, P_f
    else:
        return None
    
def dda_line(P_init, P_final):
    x_init, y_init = P_init
    x_final, y_final = P_final
    
    dx = x_final - x_init
    dy = y_final - y_init
    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    x_inc, y_inc = dx / float(steps) , dy / float(steps)
    x, y = x_init, y_init
    for i in range(int(steps) + 1):
        glVertex2f(x, y)
        x += x_inc
        y += y_inc

def read_in():
    
    global lines, n, clipped_lines
    n = int(input('Enter the number of lines: '))
    for i in range(n):
        x0 = int(input('Enter x_0: '))
        y0 = int(input('Enter y_0: '))
        x1 = int(input('Enter x_1: '))
        y1 = int(input('Enter y_1: '))
        lines.append([[x0, y0], [x1, y1]])
           
    
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)
    
def plot_points():
    global lines
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    
    # specify code

    clip_window = [[x_min, y_min], [x_min, y_max], [x_max, y_max], [x_max, y_min]]
    for index, each_side in enumerate(clip_window[:-1]):
        dda_line(each_side, clip_window[index + 1])
    dda_line(clip_window[0], clip_window[-1])
    
    # specify the clipping line coordinates
    glColor3f(1.0, 1.0, 0.0)
    for line in lines:
        # print line[0]
        # print line[1]
        dda_line(line[0], line[1])
        
    # showing the clipped lines   
    glColor3f(1.0, 0.0, 1.0)    
    for line in lines:
        new_line = cohen_sutherland_clip(line[0], line[1], clip_window)
        dda_line(new_line[0], new_line[1])
    
    # # showing the clipped lines

    # for line in clipped_lines:
    #     dda_line(line[0], line[1])
    
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'line_clipping')
    read_in()
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()

main()