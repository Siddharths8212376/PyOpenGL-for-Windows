from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
from Algorithms.line_algorithm import line_algorithm
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-300, 300, -300, 300)
    # left right bottom top

def draw_polygon(Points):
    for index, point in enumerate(Points[:-1]):
        line = line_algorithm(point, Points[index + 1])
        line.dda_line()
    line = line_algorithm(Points[0], Points[-1])
    line.dda_line()
def perform_clip(clip, clipper):
    x_min = clipper[0][0]
    x_max = clipper[-1][0]
    y_min = clipper[0][1]
    y_max = clipper[1][1]
    for index, point in enumerate(clip[:-1]):
        if point[0] < x_min:
            clipLeft(point[0])
        if point[0] > x_max:
            clipRight(point[0])
       
def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    # glVertex2f(0, 0)
    # let's try polygon clipping
    clipping_window = [[0, 0], [100, 0], [100, 100], [0, 100]]
    # draw_polygon(clipping_window)
    clip_polygon = [[-25, 25], [25, 75], [75, 25], [25, -25]]
    glColor3f(1.0, 1.0, 0.0)
    # draw_polygon(clip_polygon)
    
    perform_clip(clip_polygon, clipping_window)
    glEnd()
    glFlush()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(50, 50)  
    glutCreateWindow(b'test_algorithms')
    glutDisplayFunc(plot_points)
    init()
    glutMainLoop()

main()