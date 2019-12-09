from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import numpy as np
import time
global anim
global width, height
from Algorithms.line_algorithm import line_algorithm
global x_orig, y_orig
x_orig, y_orig = 100, 100
global x0, y0, x1, y1
x0, y0 = 90, 100
x1, y1 = 150, 100
x2 = (x0 + x1 + math.sqrt(3) * (y1 - y0)) / float(2)
y2 = (y0 + y1 + math.sqrt(3) * (x1 - x0)) / float(2)

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
    global x0, y0, x1, y1, x2, y2, x_orig, y_orig
    # glBegin(GL_LINE_LOOP)
    # glVertex2f(x0, y0)
    # glVertex2f(x1, y1)
    # glVertex2f(x2, y2)
    glBegin(GL_POINTS)
    P_0 = line_algorithm([x0, y0], [x1, y1])
    P_1 = line_algorithm([x1, y1], [x2, y2])
    P_2 = line_algorithm([x2, y2], [x0, y0])
    P_0.dda_line()
    P_1.dda_line()
    P_2.dda_line()
    
    a = P_0.return_length()
    b = P_1.return_length()
    c = P_2.return_length()
    s = (a + b + c) / 2
    mid_a = P_0.return_midpoint()
    mid_b = P_1.return_midpoint()
    mid_c = P_2.return_midpoint()
    
    m_a = P_0.return_slope()
    a_x, a_y = mid_a
    # declare and initailize x_center and y_center for the center of the circumcircle
    x_center, y_center = 0, 0
    
    if ( m_a == 0 or m_a == 10000):
        if m_a == 0:
            
            # line is x = mid_a
            normal_a = line_algorithm(mid_a, [a_x, a_y + 100])
            x_center = a_x
            a_normal_m = 'Inf'
            # normal_a_n = line_algorithm(mid_a, [a_x, a_y - 100])
        elif m_a == 10000:
            # line is y = mid_a
            y_center = a_y
            a_normal_m = 'Zero'
            normal_a = line_algorithm(mid_a, [a_x + 100, a_y])
            # normal_a_n = line_algorithm(mid_a, [a_x - 100, a_y])
            
    else:
        # line is y = f(x)
        # y = -1 / ma * x + const_a
        a_normal_m = -1 / m_a
        const_a = a_y - a_normal_m * a_x
        normal_a = line_algorithm(mid_a, [0, const_a])

        
    m_b = P_1.return_slope()
    b_x, b_y = mid_b
    
    if ( m_b == 0 or m_b == 10000):
        if m_b == 0:
            
            # line is x = mid_a
            b_normal_m = 'Inf'
            normal_b = line_algorithm(mid_b, [b_x, b_y + 100])
            x_center = b_x
        elif m_b == 10000:
            b_normal_m = 'Zero'
            normal_b = line_algorithm(mid_b, [b_x + 100, b_y])
            y_center = b_y
            
    else:
        b_normal_m = -1 / m_b
        const_b = b_y - b_normal_m * b_x
        normal_b = line_algorithm(mid_b, [0, const_b])
        
    m_c = P_2.return_slope()
    c_x, c_y = mid_c

    if ( m_c == 0 or m_c == 10000):
        if m_c == 0:
            
            # line is x = mid_a
            normal_c = line_algorithm(mid_c, [c_x, c_y + 100])
        elif m_c == 10000:
            normal_c = line_algorithm(mid_c, [c_x + 100, c_y])
            
    else:
        c_normal_m = -1 / m_c
        const_c = c_y - c_normal_m * c_x
        normal_c = line_algorithm(mid_c, [0, const_c])
    
    glColor3f(1.0, 0.0, 1.0)
    # normal_a.dda_line()
    # normal_b.dda_line()
    # normal_c.dda_line()
    # take the intersection of mid_a and mid_b and find the coordinates for the point
    # that will serve as the center for the circumcircle
    if isinstance(a_normal_m, float) and isinstance(b_normal_m, float):
        # do x_center and y_center calculation
        x_center = (const_b - const_a) / (a_normal_m - b_normal_m)
        y_center = a_normal_m * x_center + const_a
        
    if (a_normal_m == 'Inf' or a_normal_m == 'Zero') and isinstance(b_normal_m, float):
        # calculate x_c and y_cs
        if a_normal_m == 'Inf':
            x_center = a_x
            y_center = b_normal_m * x_center + const_b
        elif a_normal_m == 'Zero':
            y_center = a_y
            x_center = 1 / b_normal_m * (y_center - const_b)
    elif (b_normal_m == 'Inf' or b_normal_m == 'Zero') and isinstance(a_normal_m, float):
        # calculate x_c and y_cs
        if b_normal_m == 'Inf':
            x_center = b_x
            y_center = a_normal_m * x_center + const_a
        elif b_normal_m == 'Zero':
            y_center = b_y
            x_center = 1 / a_normal_m * (y_center - const_a)
    
    print("Central Coordinates for the circumcircle are ", x_center, " ", y_center)
    
    
    # m_b = P_1.return_slope()
    # m_c = P_2.return_slope()

    # b_normal_m = -1 / m_b
    # c_normal_m = -1 / m_c
    
    # # for line a
    # # y = m_new * x + c
    centre = [x_center, y_center]
    glEnd()
    glFlush()
    
    x_orig, y_orig = x_center, y_center

def rotate_triangle():
    global theta, x0, y0, x1, y1, x2, y2, x_orig, y_orig
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
    translation_to_origin = [
        [1, 0, x_orig],
        [0, 1, y_orig],
        [0, 0, 1]
    ]
    rotation_matrix = [
        [math.cos(theta), -1 * math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ]
    translation_back_to_place = [
        [1, 0, -x_orig],
        [0, 1, -y_orig],
        [0, 0, 1]
    ]
    transformation_1 = np.matmul(translation_to_origin, rotation_matrix)
    transformation = np.matmul(transformation_1, translation_back_to_place)
    
    updated_position_0 = np.matmul(transformation, current_position_0)
    updated_position_1 = np.matmul(transformation, current_position_1)
    updated_position_2 = np.matmul(transformation, current_position_2)
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