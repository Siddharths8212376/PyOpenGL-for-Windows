# circumcircle of a triangle
# draw a spiral
segments = 360
#Program to plot a point
# how to find the center then?

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

from Algorithms.line_algorithm import line_algorithm
from Algorithms.circle_algorithms import circle_algorithms

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def draw_triangle(a_line, b_line, c_line):

    a_line.dda_line()
    b_line.dda_line()
    c_line.dda_line()

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    # draw the triangle first
    P_0 = line_algorithm([0, 0], [100, 100])
    P_1 = line_algorithm([100, 100], [200, 0])
    P_2 = line_algorithm([0, 0], [200, 0])
    draw_triangle(P_0, P_1, P_2)
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
    radius = (a * b * c) / (math.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c)))
    circumcircle = circle_algorithms(radius, x_center, y_center)
    glColor3f(0.0, 1.0, 1.0)
    circumcircle.parameteric_circle()
    
    
        
    # # for line b
    # # y = m_new * x + c
    # b_x, b_y = mid_b
    # const_b = b_y - b_normal_m * b_x
    # normal_b = line_algorithm(mid_b, [0, const_b])
    
        
    # # for line x
    # # y = m_new * x + c
    # c_x, c_y = mid_c
    # const_c = c_y - c_normal_m * c_x
    # normal_c = line_algorithm(mid_c, [0, const_c])
    
    

    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot_all_points')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()


main()

# change the centre too