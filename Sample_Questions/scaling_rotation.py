# prove that scaling and rotation are not commutative 
# graphically
# program to plot a point
# they are the same only if sx = sy

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from Algorithms.line_algorithm import line_algorithm

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-350.0, 350.0, -350.0, 350.0)

def draw_figure(P, Q, R):
    P_Q = line_algorithm(P, Q)
    Q_R = line_algorithm(Q, R)
    R_P = line_algorithm(R, P)

    lines = [P_Q, Q_R, R_P]
    for line in lines:
        line.dda_line()
    

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_POINTS)
    segments = 500


    # get initail figure
    P = [0, 0]
    Q = [50,50]
    R = [100, 0]
    P_ = [0, 0]
    Q_ = [50,50]
    R_ = [100, 0]
    Copy = [P_, Q_, R_]
    Points = [P, Q, R]
    draw_figure(P, Q, R)
    s_x, s_y = 2, 0.5
    
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(P[0], P[1])
    
    # scaling followed by rotation
    
    theta = math.pi / 6
    # for point in Points:
    #     rad = point[0]
    #     rad_ = point[1]
    #     point[0] =  s_x * rad * math.cos(theta) - s_y * rad * math.sin(theta)
    #     point[1] = s_x * rad_ * math.sin(theta) + s_y * rad_ * math.cos(theta)
    # glColor3f(0, 0, 1)
    # draw_figure(Points[0], Points[1], Points[2])
    
    for point in Points:
        rad = point[0]
        rad_ = point[1]
        point[0] = s_x * rad * math.cos(theta) - s_y * rad_ * math.sin(theta)
        point[1] = s_y * rad_
    glColor3f(0, 0, 1)
    draw_figure(Points[0], Points[1], Points[2])        
    glColor3f(1.0, 0.0, 0.0)
    # glVertex2f(Points[0][0], Points[0][1])
    
    # # rotation followed by scaling

    for point in Copy:
        rad = point[0]
        rad_ = point[1]
        point[0] = s_x * rad * math.cos(theta) - s_x * rad_ * math.sin(theta)
        point[1] = s_y * rad_
    glColor3f(1, 1, 0)
    draw_figure(Copy[0], Copy[1], Copy[2])       
    glColor3f(1.0, 0.0, 0.0)
    # glVertex2f(Copy[0][0], Copy[0][1])
    # for point in Copy:
    #     rad = point[0]
    #     rad_ = point[1]
    #     point[0] =  s_x * rad * math.cos(theta) - s_x * rad * math.sin(theta)
    #     point[1] = s_y * rad_ * math.sin(theta) + s_y * rad_ * math.cos(theta)
    # glColor3f(1, 1, 0)
    # draw_figure(Copy[0], Copy[1], Copy[2])
    
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'plot_all_points')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()


main()

