# sutherland-hodgeman polygon clipping algorithm
#Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from Algorithms.line_algorithm import line_algorithm

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

# we have to create a filled shape

# we'll have to create functions for returning the x and y-intercepts
def x_intercept(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * ( x3 * y4 - y3 * x4)
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    return num // den

def y_intercept(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    
    return num // den

def clip(polygon, x1, y1, x2, y2):
    new_points = [[0, 0]] * len(polygon)
    for i in range(len(polygon)):
        k = (i + 1) % len(polygon)
        ix, iy = polygon[i][0], polygon[i][1]
        kx, ky = polygon[k][0], polygon[k][1]
        
        i_pos = (x2 - x1) * (iy - y1) - (y2 - y1) * (ix - x1)
        k_pos = (x2 - x1) * (ky - y1) - (y2 - y1) * (kx - x1)
        
        if i_pos < 0 and k_pos < 0:
            new_points[len(new_points) - 1][0] = kx
            new_points[len(new_points) - 1][1] = ky
            # new_points.append([0, 0])
        elif i_pos >= 0 and k_pos < 0:
            new_points[len(new_points) - 1][0] = x_intercept(x1, y1, x2, y2, ix, iy, kx, ky)
            new_points[len(new_points) - 1][1] = y_intercept(x1, y1, x2, y2, ix, iy, kx, ky)
            # new_points.append([0, 0])
            new_points[len(new_points) - 1][0] = kx
            new_points[len(new_points) - 1][1] = ky
            
        elif i_pos < 0 and k_pos >= 0:
            new_points[len(new_points) - 1][0] = x_intercept(x1, y1, x2, y2, ix, iy, kx, ky)
            new_points[len(new_points) - 1][1] = y_intercept(x1, y1, x2, y2, ix, iy, kx, ky)
            # new_points.append([0, 0])
        # copying new points to the original array
        poly_size = len(new_points)
        print("poly size is " , poly_size)
        # for i in range(len(new_points) - len(polygon)):
            # polygon.append([0, 0])
        for i in range(poly_size):
            polygon[i][0] = new_points[i][0]
            polygon[i][1] = new_points[i][1]
            print(polygon[i][0], ", " , polygon[i][1])
    return polygon
            
            
            

def cohen_hodge_clip(polygon, clipper):
    for i in range(len(clipper)):
        k = (i + 1) % len(clipper)
        new_polygon = clip(polygon, clipper[i][0], clipper[i][1], clipper[k][0], clipper[k][1])
        
    for j in range(len(new_polygon)  ):
        glColor3f(1.0, 0.0, 1.0)
        glVertex2f(new_polygon[j][0], new_polygon[j][1])
    # for j in range(len(new_polygon) - 1):
    #     line = line_algorithm(new_polygon[j], new_polygon[j + 1])
    #     line.dda_line()
    

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    line_3 = line_algorithm([0, 0], [100, 0])
    line_2 = line_algorithm([100, 0], [100, 100])
    line_1 = line_algorithm([100, 100], [0, 100])
    line_0 = line_algorithm([0, 100], [0, 0])
    P_0 = [0, 0]
    P_1 = [0, 100]
    P_2 = [100, 100]
    P_3 = [100, 0]
    clipper = [P_0, P_1, P_2, P_3]
    
    # implementating a triangle to cut-off
    edge_2 = line_algorithm([150, -50], [-50, 150])
    edge_1 = line_algorithm([-50, 150], [-50, -50])
    edge_0 = line_algorithm([-50, -50], [150, -50])
    t_0 = [-50, -50]
    t_1 = [-50, 150]
    t_2 = [150, -50]
    
    # the edges are declared in clockwise direction
    polygon = [t_0, t_1, t_2]

    
    
    
    # line_0.dda_line()
    # line_1.dda_line()
    # line_2.dda_line()
    # line_3.dda_line()

    
    # edge_0.dda_line()
    # edge_1.dda_line()
    # edge_2.dda_line()
    cohen_hodge_clip(polygon, clipper)
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

