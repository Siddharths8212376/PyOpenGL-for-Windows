#Program to plot a point

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from line_algorithm import line_algorithm

# defining min_max boundaries
x_min, y_min = 4, 4
x_max, y_max = 100, 100
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

# define the get-pixel and set-pixel functions
def set_pixel(x, y, color_code):
    glColor3fv(color_code)
    glVertex2i(x, y)

def get_pixel(x, y, pixels):
    glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_UNSIGNED_BYTE, None)
    
    
def boundary_fill(x, y, fill_color, boundary_color):
    in_color = [1, 0, 0]
    # get_pixel(x, y, in_color)
    # if get_pixel(x, y, in_color)
    if ((in_color[0] != boundary_color[0] and (in_color[1]) != boundary_color[1] and (in_color[2]) != boundary_color[2]) and (in_color[0] != fill_color[0] and (in_color[1]) != fill_color[1] and (in_color[2]) != fill_color[2])):
        set_pixel(x, y, fill_color)
        boundary_fill(x + 1, y, fill_color, boundary_color)
        boundary_fill(x - 1, y, fill_color, boundary_color)
        boundary_fill(x, y + 1, fill_color, boundary_color)
        boundary_fill(x, y - 1, fill_color, boundary_color)
    
def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    min = [x_min, y_min]
    max = [x_max, y_max]
    X = [x_max, y_min]
    Y = [x_min, y_max]
    min_X = line_algorithm(min, X)
    min_Y = line_algorithm(min, Y)
    max_X = line_algorithm(max, X)
    max_Y = line_algorithm(max, Y)
    min_X.dda_line()
    min_Y.dda_line()
    max_X.dda_line()
    max_Y.dda_line()
    boundary_fill((x_max + x_min) / 2, (y_max + y_min) / 2, [0, 1, 0], [1, 0, 0])
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