# cohen sutherland line clipping
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

# declare the globals 
global lines, n, clipped_lines
global x_center, y_center, radius, center
global x_min, y_min, x_max, y_max
# clipping window coordinate set
x_min, y_min = 0, 0
x_max, y_max = 200, 100
x_center, y_center = 50, 50
radius = 80
center = [x_center, y_center]
global clip_window
clip_window = [[x_min, y_min], [x_min, y_max], [x_max, y_max], [x_max, y_min]]
global n_intersection
n_intersection = 0


    
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

def clip_circle():
    global center, radius, n_intersection
    global x_min, y_min, x_max, y_max   
    x_c, y_c = center
    accept = False
    while True:
        if x_c + radius < x_min:
            break
        elif x_c - radius > x_max:
            break
        elif y_c - radius > y_max:
            break
        elif y_c + radius < y_min:
            break
        elif x_c + radius < x_max and x_c - radius < x_min:
            accept = True
            break
        # else if there are some intersections
        else:
            if x_c + radius > x_max:
                n_intersection += 1
                x_int = x_max
                cos_theta = (x_max - x_center) / float(radius)
                theta = math.acos(cos_theta)
                rest_theta = 2 * math.pi - theta
                y_int_1 = radius * math.sin(theta)
                y_int_2 = radius * math.sin(rest_theta)
                
                
        
        
    

def draw_circle():
    
    global x_center, y_center, radius
    segments = 500
    glColor3f(1.0, 1.0, 0.0)
    for rad in range(segments):
        theta = 2 * 3.14 * rad / float(segments)
        x_ = radius * math.cos(theta)
        y_ = radius * math.sin(theta)
        glVertex2f(x_ + x_center, y_ + y_center)
    
    
def plot_points():
    global lines, clip_window
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    
    
    # create the window

    for index, each_side in enumerate(clip_window[:-1]):
        dda_line(each_side, clip_window[index + 1])
    dda_line(clip_window[0], clip_window[-1])
    
    # draw the circle using any of the algorithms
    draw_circle()
    
    clip_circle()
    

    
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'line_clipping')
    # read_in()
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()

main()