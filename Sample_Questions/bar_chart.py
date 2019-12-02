# program to plot a pie chart for a given set of data

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time
from Algorithms.line_algorithm import line_algorithm
from Algorithms.circle_algorithms import circle_algorithms
sys.setrecursionlimit(1500)
# defining min_max boundaries
x_min, y_min = 4, 4
x_max, y_max = 100, 100
radius = 50
old_color = [0, 0, 0]  
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

# define the get-pixel and set-pixel functions
def set_pixel(x, y, color_code):
    glBegin(GL_POINTS)
    glColor3fv(color_code)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def get_pixel(x, y, pixels):
    glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_UNSIGNED_BYTE, None)
    

def flood_fill(x, y, fill_color, old_color):
    data_values = [3, 5, 10, 20, 15]
    data_values = [x * 10 for x in data_values]
    width = 20
    red = [1, 0, 0]
    green = [0, 1, 0]
    blue = [0, 0, 1]
    yellow = [1, 1, 0]
    pink = [0, 1, 1]
    set_colors = [red, green, blue, yellow, pink]
    displacement = 0
    for x in range(200):
        set_pixel(x - 10, 0, set_colors[0])
        set_pixel(-10, x, set_colors[0])
    for index,value in enumerate(data_values):
        for w in range(width):
            for h in range(value):
                set_pixel(w + 2*displacement, h, set_colors[index])
        displacement += width
        

 

def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)

    glEnd()
    glFlush()
    flood_fill(0 , 0 , [0, 1, 0], old_color)


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
